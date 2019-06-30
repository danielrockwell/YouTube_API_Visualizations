import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

CSV_PATH = "../channel_data/earthling_ed.csv"
plotTitle = "Earthling Ed's Views and Likes Correlation"
saveImagePath = './plot_images/Earthling_TopViewsBarChart.png'


# Reading Channel Data from CSV
df = pd.read_csv(CSV_PATH).sort_values('viewcount', ascending=False)
df = df[:5]
df["title"] = df["title"].str[:20] + '...'
titles = df['title']
viewCount = df['viewcount']
comments = df['commentcount']
likes = df['likecount']
dislikes = df['dislikecount']

# Style of Plot
# plt.style.use('seaborn')
plt.xkcd()


fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Video Titles')
ax1.set_ylabel('View Count', color=color, fontsize=11)
ax1.bar(titles,viewCount,color=color)
ax1.tick_params(axis='y', labelcolor=color, labelsize=9)
ax1.tick_params(axis='x', labelsize=8)


ax2=ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Like Count',color=color, fontsize=11)
ax2.plot(titles,likes,color=color, marker='_',linewidth='0',linestyle='None',mew=3.9,markersize=30)
ax2.tick_params(axis='y', labelcolor=color,labelsize=9)

fig.patch.set_facecolor('#E0E0E0')
plt.setp(ax1.get_xticklabels(), ha="right",rotation=45)

plt.title(plotTitle,fontdict = {'fontsize' : 20})

fig.tight_layout()
plt.savefig(saveImagePath, dpi = 400)

plt.show()
