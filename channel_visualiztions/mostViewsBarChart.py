import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

CSV_PATH = "../channel_data/earthling_ed.csv"
plotTitle = 'Earthling Ed Views and Comments Correlation'
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

# Preferences for Plot
# colors = np.random.rand(COLORS)

# Plotting data from CSV
plt.bar(titles, viewCount)


plt.title(plotTitle)
plt.xticks(rotation=45, ha='right')
plt.xlabel('View Count')
plt.ylabel('Number of Likes')

plt.tight_layout()
# plt.savefig(saveImagePath, dpi = 400)

plt.show()
