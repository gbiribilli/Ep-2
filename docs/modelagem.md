# Modelagem do Problema --- Otimização de Cronograma de Equipamentos de Laboratório


# 1. Cromossomo

## O que representa

Cada **indivíduo** da população do AG representa um **cronograma
completo** contendo todas as etapas de todas as análises.

Cada **gene** possui a forma:

    (a, i, intervalo)

Onde:

-   **a** → ID da análise (1 a 18)
-   **i** → índice da etapa dentro da análise\
-   **intervalo** → horário escolhido para executar aquela etapa

## Exemplo de gene

    (7, 0, 12)

Significa:\
Etapa 0 da análise 7 será executada no **intervalo 12**.

## Tamanho do cromossomo

Cada análise possui entre 1 e 3 etapas.\
Somando todas as etapas no dicionário ANALISES → o cromossomo possui
**33 genes**.

------------------------------------------------------------------------

# 2. Função de Aptidão

A aptidão é calculada por:

    aptidão = 10000 − penalidades − (makespan × 5)

A ideia geral é:\
✔ bons cronogramas têm menos penalidades\
✔ cronogramas mais curtos são favorecidos

------------------------------------------------------------------------

## 2.1 Penalidades consideradas

### a) Conflito de equipamento

Ocorre quando dois genes usam o mesmo equipamento no mesmo intervalo.

→ Penalidade: **100 pontos por conflito**

------------------------------------------------------------------------

### b) Conflito interno dentro da análise

Duas etapas da mesma análise agendadas no mesmo horário.

→ Penalidade: **100 pontos por conflito**

------------------------------------------------------------------------

### c) Ordem das etapas

As etapas devem ocorrer em ordem crescente e com intervalo mínimo entre
elas.

-   Se a próxima etapa ocorrer antes ou no mesmo horário da anterior →
    **+80**
-   Se o intervalo for menor que 2 horas → **+50**

------------------------------------------------------------------------

### d) Limite diário de uso dos equipamentos

Cada equipamento tem um número máximo de usos por dia (tempoMaximo).

Se um dia ultrapassar esse limite:

→ Penalidade: **120 por uso excedente**

------------------------------------------------------------------------

### e) Análises críticas

Análises 4, 10 e 15 envolvendo o **Espectrômetro de Massa** devem
ocorrer antes do intervalo 30.

→ Se ocorrer depois: **+200**

------------------------------------------------------------------------

### f) Usos consecutivos e limpeza

Equipamentos com atributo `limpeza=True` não podem ser usados por mais
de `usosConsecutivos` intervalos seguidos.

→ Se ultrapassar: **+70**

Se necessário, o algoritmo insere um intervalo de limpeza ao exibir o
cronograma.

------------------------------------------------------------------------

# 3. Operadores Genéticos

## 3.1 Seleção --- Torneio

-   São selecionados **k = 3** indivíduos aleatórios.
-   O melhor entre eles vence e é utilizado como pai.

Vantagens: - simples\
- rápido\
- mantém pressão seletiva

------------------------------------------------------------------------

## 3.2 Crossover --- Corte único

Dado dois pais `p1` e `p2`:

    filho = p1[:corte] + p2[corte:]

-   O corte é aleatório
-   O tamanho do cromossomo é sempre preservado
-   As etapas continuam associadas às análises corretas

------------------------------------------------------------------------

## 3.3 Mutação

Cada gene tem probabilidade `taxa_mutacao` de ter o horário modificado.

A mutação troca o intervalo por um novo número aleatório entre 0 e
TOTAL_INTERVALOS - 1.

→ Isso permite que o algoritmo explore novas combinações.

------------------------------------------------------------------------

# 4. Inicialização

A população inicial é criada **inteiramente ao acaso**, mas seguindo
duas regras:

1.  A primeira etapa de cada análise recebe um horário aleatório.\
2.  As demais etapas são deslocadas para frente com um intervalo de 2 a
    4 horas.

Isso ajuda a evitar cronogramas absurdos como etapas invertidas, mas não
impõe nenhuma restrição rígida --- todas as penalidades ainda podem
ocorrer e o AG deve resolvê-las.

------------------------------------------------------------------------

# 5. Critério de Parada

O algoritmo para quando atinge:

    número fixo de gerações

O valor padrão é:

-   **100 gerações**

Durante a execução, o algoritmo registra: - melhor aptidão da geração -
média das aptidões - pior indivíduo - melhor solução global encontrada

------------------------------------------------------------------------

# 6. Resumo Geral

  Parte           Como funciona
  --------------- --------------------------------------------------
  Cromossomo      Lista de genes (a, i, intervalo)
  Aptidão         Quanto menos penalidades + menor duração, melhor
  Seleção         Torneio
  Crossover       Corte único
  Mutação         Troca aleatória do intervalo
  Inicialização   Aleatória com pequenos deslocamentos
  Parada          Número fixo de gerações