from graphviz import Digraph
import string
import time

from avl import AVL
from bst import BST

corpus = """
Naquela bela manhã, o sol brilhava no céu azul, e a cidade acordava com seus habitantes cheios de ânimo. A vida naquela localidade era repleta de peculiaridades que a tornavam única. As pessoas ali tinham uma ligação especial com a natureza e valorizavam os pequenos detalhes do cotidiano.

A cidade se destacava por suas ruas arborizadas e suas praças bem cuidadas. As árvores frondosas proporcionavam sombra agradável nos dias quentes de verão, convidando os moradores a fazerem picnics e a relaxarem sob suas copas generosas. As crianças, por sua vez, adoravam brincar nos parquinhos cheios de brinquedos coloridos.

Os meios de transporte também eram diferentes. Os moradores utilizavam bicicletas como principal forma de locomoção. Ciclovias cruzavam a cidade, tornando-a amigável para os ciclistas. Pedalar pelas ruas sinuosas era um prazer diário, e os ciclistas se cumprimentavam com sorrisos enquanto cruzavam seus caminhos.

A gastronomia local era um verdadeiro deleite. Os restaurantes ofereciam pratos deliciosos, com ingredientes frescos e saborosos. Os habitantes se deliciavam com refeições que variavam de saladas fresquinhas a pratos quentes e reconfortantes. Os doces também eram uma tentação, com bolos e sobremesas que deixavam qualquer um com água na boca.

As casas naquela cidade tinham um charme especial. Muitas delas eram construídas com tijolos aparentes, criando um ambiente acolhedor e rústico. Os jardins eram bem cuidados, repletos de flores coloridas que enchiam o ar com aromas agradáveis. A arquitetura única das residências dava à cidade um toque de nostalgia.

À noite, a cidade ganhava uma nova vida. As ruas se iluminavam com luzes cintilantes, e os bares e cafés se enchiam de pessoas em busca de entretenimento. A música ao vivo ecoava pelos estabelecimentos, convidando todos a dançar e se divertir. Era uma noite cheia de energia e animação.

A educação era valorizada naquela cidade, e as escolas proporcionavam um ambiente de aprendizado estimulante. As crianças recebiam uma educação de qualidade, com professores dedicados e recursos modernos. O senso de comunidade estava presente também nas instituições de ensino, onde pais e educadores trabalhavam juntos para o crescimento das novas gerações.

Em resumo, aquela cidade era um lugar verdadeiramente especial, onde a natureza, a cultura e a comunidade se uniam para criar um ambiente único. Os moradores se orgulhavam de suas tradições e valores, e a vida ali era marcada por momentos felizes e memoráveis. Era um lugar onde as palavras como beleza, simplicidade e amizade ganhavam um novo significado, tornando-o um local verdadeiramente encantador.
"""


def visualize_avl_tree(node, dot=None):
    if dot is None:
        dot = Digraph(comment="AVL Tree")

    if node is not None:
        dot.node(str(node.value))
        if node.left_child:
            dot.edge(str(node.value), str(node.left_child.value))
            visualize_avl_tree(node.left_child, dot)
        if node.right_child:
            dot.edge(str(node.value), str(node.right_child.value))
            visualize_avl_tree(node.right_child, dot)

    return dot


def build_avl(corpus):
    # Converte o texto para minúsculas e remove pontuação
    corpus = corpus.lower()
    corpus = corpus.translate(str.maketrans('', '', string.punctuation))

    # Divide o texto em palavras
    words = corpus.split()

    # Remove duplicatas mantendo a ordem de ocorrência
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Crie uma instância da árvore AVL
    avl_tree = AVL()

    # Insira cada palavra na árvore AVL
    for word in unique_words:
        avl_tree.add(word)

    return avl_tree


def build_bst(corpus):
    # Converte o texto para minúsculas e remove pontuação
    corpus = corpus.lower()
    corpus = corpus.translate(str.maketrans('', '', string.punctuation))

    # Divide o texto em palavras
    words = corpus.split()

    # Remove duplicatas mantendo a ordem de ocorrência
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Crie uma instância da árvore AVL
    bst_tree = BST()

    # Insira cada palavra na árvore AVL
    for word in unique_words:
        bst_tree.add(word)

    return bst_tree


def find_avl_node(tree, characters):
    # Verifique se a entrada tem pelo menos dois caracteres
    if len(characters) < 2:
        return []

    # Função recursiva para realizar a pesquisa na árvore e adicionar nós correspondentes a 'matches'
    def search_recursive(node, matches):
        if node is None:
            return

        # Adicione a letra do nó atual à sequência atual
        current_chars = node.value

        # Verifique se a sequência de caracteres fornecida está em qualquer lugar da palavra do nó atual
        if current_chars.startswith(characters):
            matches.append(current_chars)

        # Recurso para o nó esquerdo
        search_recursive(node.left_child, matches)

        # Recurso para o nó direito
        search_recursive(node.right_child, matches)

    # Inicialize a lista de correspondências
    matches = []

    # Chame a função de pesquisa recursiva a partir da raiz da árvore
    search_recursive(tree.root, matches)

    return matches


def find_bst_node(tree, characters):
    # Verifique se a entrada tem pelo menos dois caracteres
    if len(characters) < 2:
        return []

    # Função recursiva para realizar a pesquisa na árvore e adicionar nós correspondentes a 'matches'
    def search_recursive(node, matches):
        if node is None:
            return

        # Adicione a letra do nó atual à sequência atual
        current_chars = node.value

        # Verifique se a sequência de caracteres fornecida está em qualquer lugar da palavra do nó atual
        if current_chars.startswith(characters):
            matches.append(current_chars)

        # Recurso para o nó esquerdo
        search_recursive(node.left_child, matches)

        # Recurso para o nó direito
        search_recursive(node.right_child, matches)

    # Inicialize a lista de correspondências
    matches = []

    # Chame a função de pesquisa recursiva a partir da raiz da árvore
    search_recursive(tree.root, matches)

    matches = sorted(matches)

    return matches


def find_on_avl(avl_tree):
    while True:
        input_text = input("Buscar: ")
        if (input_text == "exit"):
            break

        start_time = time.time()
        # print("Tempo de start: ", start_time)
        matches = find_avl_node(avl_tree, input_text)

        end_time = time.time()
        # print("Tempo ao finalizar: ", end_time)
        during_time = end_time - start_time

        for match in matches:
            print(match)

        print(f"Tempo de busca: {during_time:.10f} segundos")


def find_on_bst(bst_tree):
    while True:
        input_text_bst = input("Buscar: ")
        if (input_text_bst == "exit"):
            break

        start_time_bst = time.time()
        matches_bst = find_bst_node(bst_tree, input_text_bst)

        end_time_bst = time.time()
        during_time_bst = end_time_bst - start_time_bst

        for match in matches_bst:
            print(match)

        print(f"Tempo de busca: {during_time_bst:.6f} segundos")


if __name__ == '__main__':
    # Build trees
    avl = build_avl(corpus)
    # bst = build_bst(corpus)

    # Search
    find_on_avl(avl)
    # find_on_bst(bst)
