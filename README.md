# Projeto KNN - Classificação de Flores (Atividade Acadêmica - UFBA)

Este projeto é uma **atividade prática da disciplina CTIB07 INTELIGÊNCIA ARTIFICIAL** da **UNIVERSIDADE FEDERAL DA BAHIA (UFBA)**. Ele implementa o algoritmo K-Nearest Neighbors (KNN) do zero para classificação de flores, baseado em um pequeno dataset. O objetivo é classificar novas amostras de flores (comprimento e largura da pétala) e avaliar a acurácia do modelo utilizando validação cruzada Leave-One-Out.

---

## Tabela de Conteúdos

* [Visão Geral do Projeto](#visão-geral-do-projeto)
* [Contexto Acadêmico](#contexto-acadêmico)
* [Funcionalidades](#funcionalidades)
* [Dataset](#dataset)
* [Pré-requisitos](#pré-requisitos)
* [Como Executar](#como-executar)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Exemplo de Uso](#exemplo-de-uso)
* [Resultado Esperado](#resultado-esperado)
* [Licença](#licença)

---

## Visão Geral do Projeto

O projeto consiste na implementação manual do algoritmo KNN para um problema de classificação binária (Flor do tipo A ou Flor do tipo B). 
Ele permite que o usuário interaja fornecendo novos pontos de dados para classificação e oferece a opção de escolher entre duas métricas de distância: Euclidiana e Manhattan. 
Além disso, a acurácia do modelo é avaliada por meio de validação cruzada Leave-One-Out, e uma visualização gráfica é gerada para apresentar os dados e o ponto classificado.

---

## Contexto Acadêmico

Este projeto foi desenvolvido como **Exercício 4 - Prática** da disciplina **CTIB07 INTELIGÊNCIA ARTIFICIAL**, no **INSTITUTO DE CIÊNCIA, TECNOLOGIA E INOVAÇÃO (ICTI)** da **UNIVERSIDADE FEDERAL DA BAHIA (UFBA)**. A atividade tem como foco a implementação do algoritmo K-Nearest Neighbors para classificação, cobrindo tópicos como extração, transformação e armazenamento de dados, bem como avaliação de modelos.

---

## Funcionalidades

* Carregamento manual do dataset de flores.
* Implementação do algoritmo KNN do zero para classificação.
* Cálculo das **distâncias Euclidiana e Manhattan**, com opção de escolha pelo usuário.
* Criação de uma função `knn_predict(ponto, k, tipo_distancia)` que retorna a classe prevista.
* Interatividade com o usuário para entrada de novos pontos (comprimento e largura da pétala), valor de `K` e tipo de distância.
* Geração de visualização dos pontos do dataset (coloridos por classe) e da nova amostra classificada usando `matplotlib`.
* Avaliação da acurácia do modelo com **validação cruzada Leave-One-Out**.

---

## Dataset

O dataset é pequeno e fornecido diretamente no código, contendo as seguintes colunas: `comprimento_petala`, `largura_petala` e `classe` (0 para flor do tipo A, 1 para flor do tipo B).

```python
dados = [
    [1.4, 0.2, 0],
    [1.3, 0.2, 0],
    [1.5, 0.2, 0],
    [4.5, 1.5, 1],
    [4.1, 1.0, 1],
    [4.7, 1.4, 1],
    [1.7, 0.3, 0],
    [4.2, 1.3, 1],
    [1.5, 0.4, 0],
    [4.3, 1.4, 1]
]
```

---

## Pré-requisitos

Para executar este projeto, você precisará ter o **Python** instalado. As seguintes bibliotecas Python são necessárias:

* **matplotlib** (para visualização gráfica)
* **collections** (especificamente `Counter`, para votação de classes)

Você pode instalá-las usando pip:

```bash
pip install matplotlib
```

---

## Como Executar

1.  **Clone este repositório** (ou baixe o arquivo `.py` diretamente):

    ```bash
    git clone <https://github.com/slimarc/knn-algorithm.git>
    cd <knn-algorithm>
    ```

2.  **Execute o script Python**:

    ```bash
    python main.py
    ```

O programa solicitará que você insira o comprimento e a largura da pétala de uma nova amostra, o valor de K e o tipo de distância a ser utilizado.

---

## Tecnologias Utilizadas

* **Python 3.x**
* **matplotlib.pyplot**: Para a geração de gráficos e visualizações.
* **collections.Counter**: Para auxiliar na contagem de classes dos vizinhos mais próximos.

---

## Exemplo de Uso

Ao executar o script, você verá um prompt similar a este no terminal:

Digite o comprimento da pétala: 1.6

Digite a largura da pétala: 0.3

Digite o valor de K: 3

Escolha a distância (euclidiana/manhattan): euclidiana

---

## Resultado Esperado

Após a entrada do usuário, o programa exibirá a classe prevista e a acurácia do modelo, além de gerar uma janela com a visualização gráfica.

Classe prevista: 0 (Flor do tipo A)

Acurácia com validação Leave-One-Out: 90%

---

## Licença

Este projeto é disponibilizado exclusivamente para **fins educacionais e acadêmicos**, conforme exigência da disciplina **CTIB07 INTELIGÊNCIA ARTIFICIAL** da **UNIVERSIDADE FEDERAL DA BAHIA (UFBA)**. O código e os conceitos aqui apresentados são para estudo e aprendizado.

---
