import pandas as pd
import matplotlib.pyplot as plt

# Read data from the file 'data.csv'
data = pd.read_csv('csv\\Competitive PvP.csv', header=None, names=['Name', 'Rarity', 'Type', 'Usage', 'Kills', 'Headshots', 'Image'])

grouped_data = data.groupby('Type')[['Usage', 'Kills', 'Headshots']].mean()

# Plot the data as a bar chart
grouped_data.plot(kind='bar')
plt.title('Average Percentages by Weapon Type')
plt.xlabel('Weapon Type')
plt.ylabel('Percentage')
plt.xticks(rotation=45)
plt.legend(['Usage', 'Kills', 'Headshots'])
plt.show()

print("Done")