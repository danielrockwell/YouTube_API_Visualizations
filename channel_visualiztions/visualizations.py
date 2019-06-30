import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

CSV_PATH = "../channel_data/earthling_ed.csv"
plotTitle = 'Earthling Ed Views and Comments Correlation'
saveImagePath = './plot_images/Earthling_scatter.png'


# Reading Channel Data from CSV
df = pd.read_csv(CSV_PATH).sort_values('viewcount', ascending=False)
COLORS = len(df)
viewCount = df['viewcount']
comments = df['commentcount']
likes = df['likecount']
dislikes = df['dislikecount']

# Style of Plot
# plt.style.use('seaborn')
plt.xkcd()

# Preferences for Plot
colors = np.random.rand(COLORS)

# Plotting data from CSV
plt.scatter(viewCount, likes, c=comments, s=likes **0.43,cmap='PRGn',alpha=0.8, linewidths=.1
            , edgecolors='black')

cbar = plt.colorbar()
cbar.set_label("Number of Comments")

plt.title(plotTitle)
plt.xlabel('View Count')
plt.xscale('log')
plt.yscale('log')

plt.xticks(rotation=20)
plt.ylabel('Number of Likes')

plt.tight_layout()
plt.savefig(saveImagePath, dpi = 400)

plt.show()
