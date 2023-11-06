# Requisito 03

Este arquivo contém os resultados da análise de 5 redes de grafos escolhidas. Abaixo estão os resultados e informações sobre cada uma das redes.

## Tabela de Resultados

A tabela a seguir apresenta os resultados da análise das cinco redes de grafos selecionadas. Cada linha representa uma 
rede de grafos diferente e fornece informações sobre o número de nós, o número de arestas, o coeficiente de assortatividade de grau, 
o número de componentes conectados, o maior componente conectado (GCC), e o coeficiente de agrupamento médio.

|                           | Nodes | Edges | Deg. Assortativity Coefficient. | Connected Components | GCC  | Avg. Clustering.     |
|---------------------------|-------|-------|---------------------------------|----------------------|------|----------------------|
| **Social Network**        | 4039  | 88234 | 0.06357722918564943             | 1                    | 4039 | 0.6055467186200876   |    
| **Collaboration Network** | 5242  | 14496 | 0.6591640320931624              | 355                  | 355  | 0.529635811052136    |
| **Ground Truth Network**  | 1005  | 16706 | -0.010990490627931076           | 20                   | 986  | 0.3993549664221539   |
| **Internet PP Networks**  | 6301  | 20777 | 0.03555037316941865             | 2                    | 6299 | 0.010867921935819964 |
| **Citation Network**      | 41108 | 38496 | -0.6959342757375792             | 2722                 | 782  | 0.0                  |

### Social Network
A rede "Social Network" apresenta uma quantidade significativa de nós (4,039) e arestas (88,234), indicando uma 
estrutura robusta e possivelmente densa. O coeficiente de assortatividade de grau levemente positivo (0.06357722918564943) 
implica que há uma leve tendência dos nós se conectarem com outros de graus semelhantes, embora essa tendência não seja 
fortemente marcada. A rede possui um único componente conectado, mostrando que é completamente interconectada (GCC = 4039). 
Com um coeficiente médio de clustering de 0.6055467186200876, há uma indicação de uma propensidade moderada a alta para 
a formação de grupos fechados de interações entre os nós.

### Collaboration Network

A "Collaboration Network" é composta por 5,242 nós e 14,496 arestas, com um coeficiente de assortatividade de grau 
bastante alto (0.6591640320931624), sugerindo que os indivíduos dentro desta rede tendem a colaborar com outros que 
têm um nível de colaboração semelhante. Com 355 componentes conectados, a rede parece ser fragmentada, mas o maior 
componente conectado também possui 355 nós, indicando que um desses componentes é dominante. O coeficiente de agrupamento 
médio de 0.529635811052136 sugere uma tendência considerável de formação de clusters colaborativos.

### Ground Truth Network

A "Ground Truth Network" possui 1,005 nós e 16,706 arestas. O coeficiente de assortatividade de grau é ligeiramente 
negativo (-0.010990490627931076), o que indica uma tendência quase neutra em relação à conectividade entre nós de 
diferentes graus. Existem 20 componentes conectados dentro da rede, mas o maior componente conectado (GCC) contém quase 
todos os nós (986), revelando uma rede principal altamente interconectada. O coeficiente médio de clustering de 
0.3993549664221539 demonstra uma capacidade moderada da rede de formar grupos.

### Internet PP Networks

A rede "Internet PP Networks" é formada por 6,301 nós e 20,777 arestas. Apresenta um coeficiente de assortatividade de 
grau baixo (0.03555037316941865), indicando uma leve preferência dos nós para se conectar indistintamente com outros nós, 
independentemente do grau. A rede é quase inteiramente interconectada com apenas 2 componentes conectados, e o GCC 
abrange a quase totalidade dos nós (6,299). Contudo, o coeficiente de agrupamento médio é muito baixo (0.010867921935819964), 
o que sugere que os nós não tendem a formar triângulos fechados ou grupos locais.

### Citation Network

Finalmente, a "Citation Network" é a mais extensa das redes examinadas, com 41,108 nós e 38,496 arestas. O coeficiente 
de assortatividade de grau fortemente negativo (-0.6959342757375792) indica uma pronunciada tendência dos nós de alto 
grau a se conectarem com nós de grau baixo, caracterizando-a como fortemente disassortativa em termos de grau. Existem 
2,722 componentes conectados, e o maior componente conectado inclui 782 nós, refletindo uma rede com muitos agrupamentos 
isolados. O coeficiente de agrupamento médio é 0.0, o que sugere uma ausência completa de tendência à formação de grupos 
triádicos fechados nesta rede.



