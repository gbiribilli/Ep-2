# Otimização de Cronograma de Equipamentos de Laboratório

## 📌 Descrição do Problema

Este projeto utiliza um **Algoritmo Genético (AG)** para otimizar a
agenda semanal de uso dos equipamentos de um laboratório de química.\
O objetivo é alocar horários para análises químicas respeitando:

-   disponibilidade dos equipamentos\
-   limite diário de uso\
-   tempo máximo de usos consecutivos\
-   ordem obrigatória das etapas\
-   análises críticas com horários restritos\
-   não haver conflitos entre análises

O modelo gera: - uma **visão por análise**\
- uma **visão por equipamento**\
- horários detalhados e ordenados

------------------------------------------------------------------------

## ▶ Como Executar

### 1. Instale as dependências

``` bash
pip install pandas
```

### 2. Execute o programa principal

``` bash
python laboratorio_quimica.py
```

### 3. Parâmetros disponíveis

``` bash
python laboratorio_quimica.py.py --pop 80 --gen 200 --mut 0.1 --cross 0.8
```

  Parâmetro   Significado
  ----------- ----------------------
  `--pop`     Tamanho da população
  `--gen`     Número de gerações
  `--mut`     Taxa de mutação
  `--cross`   Taxa de crossover

------------------------------------------------------------------------

