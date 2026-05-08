import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.colors as mcolors
import matplotlib.cm as cm

# Load the Excel file
file_path = 'courselist-MASTER.xlsx'
df = pd.read_excel(file_path)

# Replace 'X' with 1 and NaN with 0 for co-occurrence calculation
df = df.replace('X', 1).fillna(0)

# Remove '*' from the column names
df.columns = df.columns.str.replace('*', '', regex=True)

# Calculate the Spearman correlation matrix
spearman_corr_matrix = df.corr(method='spearman')

# Save the Spearman correlation matrix as a CSV file
spearman_corr_matrix.to_csv('spearman_correlation_matrix.csv')

# Create a weighted graph from the Spearman correlation matrix
G = nx.Graph()

# Add edges to the graph with weights (excluding diagonal)
threshold = 0.1  # Adjust threshold as needed
for i in range(spearman_corr_matrix.shape[0]):
    for j in range(spearman_corr_matrix.shape[1]):
        if i != j and spearman_corr_matrix.iloc[i, j] > threshold:
            G.add_edge(spearman_corr_matrix.index[i], spearman_corr_matrix.columns[j], weight=spearman_corr_matrix.iloc[i, j])

# Add three nodes that are not connected to any other node
G.add_node('1')
G.add_node('2')
G.add_node('3')

# Normalize the edge weights for color mapping
weights = [d['weight'] for (u, v, d) in G.edges(data=True)]
min_weight = min(weights)
max_weight = max(weights)
norm = mcolors.Normalize(vmin=min_weight, vmax=max_weight)

# Define a custom colormap that starts from a visible light gray
cmap = mcolors.LinearSegmentedColormap.from_list('custom_greys', ['#d3d3d3', 'black'])

# Make edges slightly transparent by setting alpha value
edge_colors = [mcolors.to_rgba(cmap(norm(d['weight'])), alpha=0.8) for (u, v, d) in G.edges(data=True)]

# Define the label mapping
label_mapping = {
    'SW Security': 'Security',
    'Verification': 'Verific.',
    'SE process': 'Process',
    'SE economics': 'Economics',
    'Maintenance': 'Mainten.',
    'Configuration mgmt': 'Config.',
    'SE management': 'Manag.',
    'Operations': 'Oper.',
    'Architecture': 'Arch.',
    'SE models': 'Models',
    'Economics': 'Econom.',
    'Requirements': 'Req.'
}

# Apply the label mapping to the graph
G = nx.relabel_nodes(G, label_mapping)

# Draw the graph with thicker lines, course names inside bubbles, and grey bubbles with black borders
pos = nx.spring_layout(G, k=1.0, scale=2, iterations=100)  # Increase k and iterations to spread nodes further apart and avoid overlap
fig, ax = plt.subplots(figsize=(16, 9))  # Set the figure size to 16:9 aspect ratio
nx.draw(G, pos, with_labels=True, node_size=5000, node_color='grey', font_size=12, font_weight='bold', edge_color=edge_colors, width=[d['weight']*20 for (u, v, d) in G.edges(data=True)], font_family='serif', edgecolors='black', ax=ax)

# Add padding to ensure nodes stay within the margins
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# Add a colorbar as a legend on the right
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Spearman Correlation', fontsize=16, fontfamily='serif')

# Save the plot as a PDF file with 16:9 aspect ratio without title
plt.savefig('graph_courses.pdf', format='pdf', bbox_inches='tight')

plt.show()