import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#Notes to self: Nominal, Ordinal, Nominal,Ratio, Ratio Ratio, N/A(Nominal)
def saveGridElements(data, Name):
    # Create a bar chart of Average % by Type
    Average = data.groupby('Type')[['Usage', 'Kills', 'Headshots']].mean()
    fig, ax = plt.subplots(figsize=(12, 12))
    Average.plot(kind='bar', ax=ax)
    ax.set_title('Avg. % by Type ({})'.format(Name))
    ax.set_xlabel('Weapon Type')
    ax.set_ylabel('Percentage')
    ax.set_xticklabels(Average.index, rotation=tickTitleRoationDegrees)
    ax.legend(['Usage', 'Kills', 'Headshots'])
    plt.savefig(Name + '_Avg_Percentage_by_Type')
    plt.close()

    # Create a scatter plot of Usage vs. Kills
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = list(mcolors.TABLEAU_COLORS.values())
    # Scatter plot the data points with different colors for each weapon type
    type_colors = {}
    for i, t in enumerate(data['Type'].unique()):
        d = data[data['Type'] == t]
        ax.scatter(d['Kills'], d['Usage'], color=colors[i % len(colors)])
        type_colors[t] = colors[i % len(colors)]

    ax.set_title('Usage vs. Kills ({})'.format(Name))
    ax.set_xlabel('Kills')
    ax.set_ylabel('Usage')

    # Add legend with color codes for each weapon type
    legend_handles = []
    for t in type_colors:
        legend_handles.append(ax.scatter([], [], color=type_colors[t], label=t))
    ax.legend(handles=legend_handles)

    plt.savefig(Name+ '_Usage_vs_Kills')
    plt.close()
    
    # Create a boxplot of Rarity vs. Kills
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot([data[data['Rarity']== c]['Kills'] for c in data['Rarity'].unique()])
    ax.set_xticklabels(data['Rarity'].unique())
    ax.set_title('Rarity vs. Kills ({})'.format(Name))
    ax.set_xlabel('Rarity')
    ax.set_ylabel('Kills')
    plt.savefig(Name + '_Rarity_vs_Kills')
    plt.close()

    # Create a heatmap of Avg. Kills by Rarity & Type
    heatmap_data = data.groupby(['Rarity', 'Type'])[['Kills', 'Headshots']].mean().reset_index()
    heatmap_data_pivot = heatmap_data.pivot_table(index='Type', columns='Rarity', values='Kills')
    heatmap_data_pivot.fillna(0, inplace=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.imshow(heatmap_data_pivot, cmap='coolwarm', aspect='auto')
    ax.set_title('Avg. Kills by Rarity & Type ({})'.format(Name))
    ax.set_xlabel('Weapon Type')
    ax.set_ylabel('Rarity')
    ax.set_xticks(np.arange(len(heatmap_data_pivot.columns)))
    ax.set_yticks(np.arange(len(heatmap_data_pivot.index)))
    ax.set_xticklabels(heatmap_data_pivot.columns)
    ax.set_yticklabels(heatmap_data_pivot.index)
    for i in range(len(heatmap_data_pivot.index)):
        for j in range(len(heatmap_data_pivot.columns)):
            text = ax.text(j, i, round(heatmap_data_pivot.iloc[i, j], 2), ha="center", va="center", color="w")
    cbar = fig.colorbar(cax)
    cbar.set_label('Avg. Kills')
    plt.savefig(Name + '_Avg_Kills_by_Rarity_Type')
    plt.close()
def genVisGrid(data,Name):
    # Create a figure with subplots

    formattedName = str.format("({0})",Name)

    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    fig.subplots_adjust(hspace=1,wspace=1)
    Average = data.groupby('Type')[['Usage', 'Kills', 'Headshots']].mean()
    # Plot the first bar chart in the first subplot
    Average.plot(kind='bar', ax=axs[0][0])
    axs[0][0].set_title('Avg. % by Type '+ formattedName)
    axs[0][0].set_xlabel('Weapon Type')
    axs[0][0].set_ylabel('Percentage')
    axs[0][0].set_xticklabels(Average.index, rotation=tickTitleRoationDegrees)
    axs[0][0].legend(['Usage', 'Kills', 'Headshots'])

    # Create a scatter plot of Kills vs Usage in the third subplot
    axs[0][1].scatter(data['Kills'], data['Usage'])
    axs[0][1].set_title('Usage vs. Kills '+formattedName)
    axs[0][1].set_ylabel('Usage')
    axs[0][1].set_xlabel('Kills')

    # Create the boxplot
    axs[1][0].boxplot([data[data['Rarity']== c]['Kills'] for c in data['Rarity'].unique()])
    axs[1][0].set_xticklabels(data['Rarity'].unique())
    axs[1][0].set_title('Rarity vs. Kills '+formattedName)
    axs[1][0].set_xlabel('Rarity')
    axs[1][0].set_ylabel('Kills')

    # Calculate the Avg. kills and headshots for each combination of rarity and type
    heatmap_data = data.groupby(['Rarity', 'Type'])[['Kills', 'Headshots']].mean().reset_index()
    # Pivot the data to create a matrix suitable for a heatmap
    heatmap_data_pivot = heatmap_data.pivot_table(index='Type', columns='Rarity', values='Kills')
    # Fill missing values with zeros
    heatmap_data_pivot.fillna(0, inplace=True)
    # Create the heatmap in the third subplot
    cax = axs[1][1].imshow(heatmap_data_pivot, cmap='coolwarm', aspect='auto')
    # Set the title and labels for the heatmap
    axs[1][1].set_title('Avg. Kills by Rarity & Type '+formattedName)
    axs[1][1].set_xlabel('Weapon Type')
    axs[1][1].set_ylabel('Rarity')

    # Set x-axis and y-axis labels for the heatmap
    axs[1][1].set_xticks(np.arange(len(heatmap_data_pivot.columns)))
    axs[1][1].set_yticks(np.arange(len(heatmap_data_pivot.index)))
    axs[1][1].set_xticklabels(heatmap_data_pivot.columns)
    axs[1][1].set_yticklabels(heatmap_data_pivot.index)

    # Loop over the data to add the text annotations to the heatmap
    for i in range(len(heatmap_data_pivot.index)):
        for j in range(len(heatmap_data_pivot.columns)):
            text = axs[1][0].text(j, i, round(heatmap_data_pivot.iloc[i, j], 2), ha="center", va="center", color="w")

    # Create a colorbar for the heatmap
    cbar = fig.colorbar(cax, ax=axs[1][1])
    cbar.set_label('Avg. Kills')

    plt.savefig(Name+'VisGrid.png')
    saveGridElements(data,Name)

tickTitleRoationDegrees = 80
# Read data from the file 'Competitive PvP.csv'
data = pd.read_csv('csv\\Competitive PvP.csv', header=None, names=['Name', 'Rarity', 'Type', 'Usage', 'Kills', 'Headshots', 'Image'])

genVisGrid(data,"Competative")


data = pd.read_csv('csv\\Quickplay PvP.csv', header=None, names=['Name', 'Rarity', 'Type', 'Usage', 'Kills', 'Headshots', 'Image'])

genVisGrid(data,"Quickplay")
