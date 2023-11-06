import networkx as nx
import seaborn as sns
from matplotlib import pyplot as plt


def plot_degree_assortativity(G, network_data, title):
    # Imprime as métricas da rede
    print(f"Network Data for {title}:")
    print(f"Number of Nodes: {network_data['nodes']}")
    print(f"Number of Edges: {network_data['edges']}")
    print(f"Degree Assortativity Coefficient: {network_data['degree_assortativity_coefficient']}")
    print(f"Number of Connected Components: {network_data['number_connected_components']}")
    print(f"Largest Component Size: {network_data['largest_component_size']}")
    print(f"Average Clustering Coefficient: {network_data['average_clustering']}\n")

    # Obtém a conectividade média dos vizinhos para cada grau de nó
    degree, avg_neigh_degree = zip(*nx.average_degree_connectivity(G).items())

    # Converte os valores para listas
    degree = list(degree)
    avg_neigh_degree = list(avg_neigh_degree)

    # Configura o estilo do gráfico
    plt.style.use("fivethirtyeight")
    fig, ax = plt.subplots(figsize=(12, 8))

    # Cria o gráfico de dispersão com a linha de regressão
    sns.regplot(x=degree, y=avg_neigh_degree, ax=ax)

    # Configura os rótulos dos eixos e o limite do eixo x
    ax.set_xlabel("Node Degree")
    ax.set_ylabel("Average Neighbor Degree")
    ax.set_xlim(0, None)

    # Adiciona o título
    plt.title(title)

    # Exibe o gráfico
    plt.show()


def read_network_data(file_path):
    # Lê a rede de um arquivo de lista de arestas
    G = nx.read_edgelist(file_path)
    data = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "degree_assortativity_coefficient": nx.degree_assortativity_coefficient(G),
        "number_connected_components": nx.number_connected_components(G),
        "largest_component_size": len(max(nx.connected_components(G), key=len)),
        "average_clustering": nx.average_clustering(G)
    }
    return G, data