# TRP – Anonymization of Datasets with Privacy, Utility and Risk Analysis

Projeto da UC **Tecnologias de Reforço da Privacidade (TRP)**.

---

## 1. Objetivo do projeto

Este projeto tem como objetivo estudar o processo de anonimização de um dataset real, avaliando o equilíbrio entre:

- **privacidade**
- **utilidade**
- **risco de reidentificação**

O trabalho segue o enunciado da unidade curricular e inclui:

1. seleção, sanitização e caracterização do dataset;
2. definição de coding models e hierarquias de generalização;
3. aplicação de modelos de privacidade;
4. análise de utilidade, privacidade e risco;
5. elaboração de relatório final.

---

## 2. Dataset escolhido

Foi escolhido o dataset **Adult / Census Income**, extraído da base de dados do Census Bureau de 1994.

### Descrição resumida
O dataset contém informação demográfica, educacional e profissional de indivíduos, com o objetivo preditivo de determinar se uma pessoa aufere rendimento anual **superior a 50K USD**.

### Motivação para a escolha
Este dataset foi escolhido porque:

- possui número suficiente de registos e atributos;
- contém atributos categóricos e numéricos;
- inclui vários potenciais **quasi-identifiers**;
- permite experimentar diferentes estratégias de anonimização;
- facilita a avaliação de utilidade através de análises estatísticas comparativas.

---

## 3. Pré-processamento do dataset

Foi criada uma versão limpa do dataset original (`adult_clean.csv`), com as seguintes transformações:

- substituição de valores em falta (`?`) por `"Unknown"`;
- remoção do atributo redundante `education.num`;
- normalização do formato do ficheiro CSV.

---

## 4. Configuração de anonimização (ARX)

A anonimização foi realizada com recurso à ferramenta **ARX**.

### Projeto ARX
A configuração completa pode ser reproduzida através do ficheiro: **arx/projects/adult_project.deid**


Este ficheiro inclui:
- definição dos tipos de atributos;
- hierarquias de generalização;
- modelos de privacidade utilizados.

---

## 5. Modelos de privacidade

Foram aplicados os seguintes modelos:

- **k-anonymity (k = 5)**
- **l-diversity (l = 2)** sobre o atributo sensível `income`

Esta combinação permite garantir:
- proteção contra reidentificação direta;
- proteção contra inferência do atributo sensível.

---

## 6. Quasi-identifiers utilizados

Após experimentação, foram selecionados os seguintes atributos como quasi-identifiers:

- age  
- sex  
- education  
- native.country  

Outros atributos foram considerados inicialmente, mas removidos devido ao impacto negativo na possibilidade de satisfazer os modelos de privacidade.

---

## 7. Hierarquias de generalização

As hierarquias utilizadas encontram-se em: **arx/hierarchies/**

Incluem:
- generalização de idade por intervalos;
- agrupamento de países por regiões;
- agregação de níveis de educação.

---

## 8. Estrutura do repositório (IDEIA INICIAL)

```text
.
├── README.md
├── docs/
├── data/
│   ├── raw/
│   ├── processed/
│   └── anonymized/
├── arx/
│   ├── projects/
│   ├── hierarchies/
│   └── exports/
├── analysis/
│   ├── notebooks/
│   ├── scripts/
│   └── results/
└── presentation/

---
## 9. Reprodutibilidade

Para reproduzir os resultados:

1. Abrir o ARX;
2. Carregar o ficheiro: **arx/projects/adult_project.deid** 
3. Executar a anonimização.

---

## 10. Estado atual

- ✔ Dataset limpo e preparado  
- ✔ Classificação de atributos  
- ✔ Hierarquias definidas  
- ✔ Modelos de privacidade configurados  
- ✔ Primeira anonimização realizada  

---

## 11. Próximos passos

- análise de utilidade dos dados anonimizado;
- comparação entre diferentes valores de k;
- avaliação do risco de reidentificação;
- elaboração do relatório final.
