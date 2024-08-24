import osmnx as ox
import matplotlib.pyplot as plt

# Generate the road network graph in WGS84 (default, latitude/longitude)
G = ox.graph_from_place('University of Lagos, Lagos Mainland, Lagos State, Nigeria', 
                        network_type='drive_service')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(40, 40))

# Plot the graph with nodes and edges
ox.plot_graph(G, ax=ax, node_color='blue', node_size=30, edge_color='gray', show=False, close=False)

# Loop over each node in the graph to add labels
for node, data in G.nodes(data=True):
    x, y = data['x'], data['y']
    ax.text(x, y, str(node), fontsize=10, ha='left', va='bottom', color='blue')



# Display the plot
plt.show()

eval "$(/opt/homebrew/bin/brew shellenv)"
export PATH=/opt/homebrew/bin:/opt/homebrew/sbin:$PATH
export PATH="/opt/homebrew/bin:$PATH"