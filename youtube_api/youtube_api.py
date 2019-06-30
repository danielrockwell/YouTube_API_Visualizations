'''
    File name: youtube_api.py
    Author: Daniel Rockwell
    Date created: 06/27/2019
    Date last modified: 06/29/2019
    Python Version: 3.7.3
'''

from apiclient.discovery import build
import csv

YOUTUBE_CHANNEL_SEARCH = "Earthling Ed"
CSV_FILE_NAME = "../channel_data/earthling_ed.csv"

api_service_name = "youtube"
api_version = "v3"
api_key = 'SECRET KEY'

youtube = build(api_service_name, api_version, developerKey=api_key)


class Videos:
    def __init__(self, title, id, viewcount, likecount, dislikecount, commentcount):
        self.title = title
        self.id = id
        self.viewcount = viewcount
        self.likecount = likecount
        self.dislikecount = dislikecount
        self.commentcount = commentcount

    def __repr__(self):
        return f'Title: {self.title} ViewCount: {self.viewcount}'


def getChannelID(username):
    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=username,
        type="channel",
        order='viewCount'
    )
    response = request.execute()
    return response['items'][0]['id']['channelId']


def getUploadID(channelID):
    request = youtube.channels().list(
        part="contentDetails",
        id=channelID
    )
    response = request.execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


def getUploadVideoID(uploadID):
    pageToken = None
    videoID, videos = [], []
    while True:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=50,
            playlistId=uploadID,
            pageToken=pageToken
        )
        response = request.execute()
        videoID.append(response['items'])
        pageToken = response.get('nextPageToken', "empty")
        if pageToken is "empty":
            break

    for page in videoID:
        for video in page:
            videos.append(video['contentDetails']['videoId'])

    return videos


def getVidDetails(videoID):
    details = []

    for videos in videoID:
        request = youtube.videos().list(
            part="snippet,statistics",
            id=videos
        )
        response = request.execute()

        title = response['items'][0]['snippet']['title']
        stats = response['items'][0]['statistics']

        obj = Videos(title, response['items'][0]['id'], stats['viewCount'], stats['likeCount'], stats['dislikeCount'],
                     stats['commentCount'])
        details.append(obj)
    return details


def writeToCSV(file, listOfObj):
    csv_header = ['title', 'id', 'viewcount',
                  'likecount', 'dislikecount', 'commentcount']
    with open(file, mode='w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=csv_header)
        csv_writer.writeheader()
        for obj in listOfObj:
            csv_writer.writerow({
                'title': obj.title,
                'id': obj.id,
                'viewcount': obj.viewcount,
                'likecount': obj.likecount,
                'dislikecount': obj.dislikecount,
                'commentcount': obj.commentcount
            })


channelID = getChannelID(YOUTUBE_CHANNEL_SEARCH)
upID = getUploadID(channelID)
videoID = getUploadVideoID(upID)
vidDetails = getVidDetails(videoID)
writeToCSV(CSV_FILE_NAME, vidDetails)
