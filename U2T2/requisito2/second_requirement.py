from utils import read_network_data, plot_degree_assortativity

root = "./data/"

# Arquivos de rede
network_files = {
    "Social Network": root + "social_network.txt",                 # REDE 1 - Social Network - Facebook
    "Collaboration Network": root + "collaboration_network.txt",   # REDE 2 - Collaboration Network - GRQC
    "Ground Truth Network": root + "ground-truth_network.txt",     # REDE 3 - Networks with ground-truth communities - email-Eu-core network
    "Internet PP Networks": root + "internetpp_network.txt",       # REDE 4 - Internet peer-to-peer networks - Gnutella peer-to-peer network, August 8
    "Citation Network": root + "citation_network.txt"              # REDE 5 - Citation networks - High-energy physics theory citation network
}

# Ler e analisar cada rede
for title, file_path in network_files.items():
    G, network_data = read_network_data(file_path)

    plot_degree_assortativity(G, network_data, title)
