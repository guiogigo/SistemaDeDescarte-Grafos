# Siste de Coleta de lixo - Grafos

## Integrantes
- Arthur Lobo Feitosa de Oliveira 
- Arthur Ricardo Macedo Pereira
- Guido Xenofonte de Almeida Gonçalves
- Guilherme Viana Batista 

## Descrição
O projeto envolve a criação de um sistema de gerenciamento para a coleta de lixo e controle de animais de rua, visando melhorar a qualidade de vida dos moradores e minimizar os impactos negativos causados pela coleta precária e pela presença de animais soltos.

O sistema automatiza a alocação de caminhões de lixo e funcionários, otimizando as coletas de resíduos com compactação eficiente para maximizar a capacidade dos veículos. Além disso, integra alertas em tempo real sobre a presença de animais de rua nos pontos de coleta, ativando ações coordenadas com o centro de zoonoses para capturá-los e garantir um ambiente mais limpo e seguro.

O projeto também considera desafios como deslocamento entre os pontos de coleta e comportamentos dinâmicos dos animais, como interações entre ratos, gatos e cachorros. Com base em algoritmos de otimização, o programa calcula os recursos mínimos necessários para completar a operação dentro de um limite de 8 horas, tornando-o essencial para uma gestão pública eficiente.

## Inicialização
Para inicializar o projeto basta:
1. Clonar o repositório do GitHub
2. Configurar o arquivo grafo.json
3. Rodar o arquivo main.py

## Arquivo JSON
Você pode personalizá-lo conforme suas necessidades.

    "pontos" : {Quantidade de pontos de coleta},
    "direcionado" : {true ou false},
    "arestas" : [[{Vértice 1},{Vértice 2},{peso}], [v1,v2,n]],
    "aterro" : {Número do vértice que será o aterro},
    "centroZoo" : {Número do vértice que será o centro de Zoonose}

## Principais Funções
| Participante       | Função Principal                          |
|--------------------|-------------------------------------------|
| Arthur Lobo Feitosa de Oliveira  | Implementação do Grafo e construção da main             |
| Arthur Ricardo Macedo Pereira | Implementação dos animais |
| Guido Xenofonte de Almeida Gonçalves | Implementação da Carrocinha e Arquivo JSON |
| Guilherme Viana Batista  | Implementação do Caminhão e do algoritmo de Dijkstra           |
---

## Vídeo Explicativo
Veja os vídeos com a explicação completa no YouTube: [Playlist do projeto](https://www.youtube.com/playlist?list=PLPQ1WkSoGf5ywTjfCDsIK4ThJ_6Z82ilT)
---
#### UFCA - ALGORITMOS EM GRAFOS - 2024.1
