import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
data = pd.read_csv('clean_data.csv')

# Extract the relevant columns (from the 5th column onwards, excluding the last column)
topics_data = data.iloc[:, 4:-1]

# Convert all relevant columns to numeric, forcing errors to NaN
topics_data = topics_data.apply(pd.to_numeric, errors='coerce')

# Group by university and sum the occurrences of each topic
uni_topic_counts = topics_data.groupby(data['Uni']).sum()

# Calculate the percentage of each topic for each university
uni_topic_percentage = uni_topic_counts.div(uni_topic_counts.sum(axis=1), axis=0) * 100

# Define hatch patterns and shades of grey for visualization
hatch_patterns = ["/", "\\", "|", "-", "+", "x", "o", "O", "*", ".", "//", "\\\\", "XX", "--", ".."]
grey_shades = ["#f7f7f7", "#e0e0e0", "#d9d9d9", "#c2c2c2", "#bdbdbd", "#a8a8a8", "#969696"]

# Set up the figure and axis
plt.rcParams.update({'font.family': 'Georgia', 'font.size': 14})
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the 100% stacked bar chart with hatching and grey shades
bottom_values = np.zeros(len(uni_topic_percentage))
for idx, column in enumerate(uni_topic_percentage.columns):
    ax.bar(
        uni_topic_percentage.index, 
        uni_topic_percentage[column], 
        bottom=bottom_values, 
        edgecolor="black", 
        hatch=hatch_patterns[idx % len(hatch_patterns)],
        color=grey_shades[idx % len(grey_shades)]
    )
    bottom_values += uni_topic_percentage[column].values

# Set plot labels and title
ax.set_xlabel('University')
ax.set_ylabel('Recurrence of topics at universities')
ax.set_title('')

# Remove the border, including the y-axis but leaving the x-axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Add horizontal gridlines where the ticks are and move them to the background
ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.7)
ax.xaxis.grid(False)
ax.set_axisbelow(True)

# Move the legend to the top of the plot and distribute it horizontally
ax.legend(uni_topic_percentage.columns, bbox_to_anchor=(0.5, 1.15), loc='upper center', ncol=4)

plt.xticks(rotation=0)

# Save the figure with the specified dimensions in PDF format
fig.set_size_inches(1727/100, 949/100)  # Convert pixels to inches (DPI = 100)
fig.savefig('uni_topic_recurrence_bw.pdf', format='pdf', bbox_inches='tight')

# Show the plot
plt.tight_layout()
plt.show()
