import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Read data from the file 'Competitive PvP.csv'
data = pd.read_csv('csv\\Competitive PvP.csv', header=None, names=['Name', 'Rarity', 'Type', 'Usage', 'Kills', 'Headshots', 'Image'])
Competitive = data.groupby('Type')[['Usage', 'Kills', 'Headshots']].mean()

# Read data from the file 'Quickplay PvP.csv'
data = pd.read_csv('csv\\Quickplay PvP.csv', header=None, names=['Name', 'Rarity', 'Type', 'Usage', 'Kills', 'Headshots', 'Image'])
Quickplay = data.groupby('Type')[['Usage', 'Kills', 'Headshots']].mean()

# Create a figure with two subplots
fig, axs = plt.subplots(3, 3, figsize=(10, 10))

# Plot the first bar chart in the first subplot
Competitive.plot(kind='bar', ax=axs[0][0])
axs[0][0].set_title('Average Percentages by Weapon Type (Competitive)')
axs[0][0].set_xlabel('Weapon Type')
axs[0][0].set_ylabel('Percentage')
axs[0][0].set_xticklabels(Competitive.index, rotation=45)
axs[0][0].legend(['Usage', 'Kills', 'Headshots'])

# Plot the second bar chart in the second subplot
Quickplay.plot(kind='bar', ax=axs[0][1])
axs[0][1].set_title('Average Percentages by Weapon Type (Quickplay)')
axs[0][1].set_xlabel('Weapon Type')
axs[0][1].set_ylabel('Percentage')
axs[0][1].set_xticklabels(Quickplay.index, rotation=45)
axs[0][1].legend(['Usage', 'Kills', 'Headshots'])

# Create a scatter plot of Kills vs Usage in the third subplot
axs[0][2].scatter(data['Kills'], data['Usage'])
# Set the title and labels
axs[0][2].set_title('Usage vs. Kills (Competative & Quickplay)')
axs[0][2].set_ylabel('Usage')
axs[0][2].set_xlabel('Kills')



# Display the plot
plt.tight_layout()
plt.show()
