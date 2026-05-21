# Projeto ETL Parquet

Pipeline de **ETL** (Extract, Transform, Load) em Python que consolida arquivos JSON de vendas, calcula um KPI de faturamento e exporta o resultado em formato **CSV** e/ou **Parquet**.

## Visão geral

O projeto lê múltiplos arquivos de coleta diária (`data/coleta_dia*.json`), unifica os dados em um único `DataFrame`, calcula o total de vendas por registro e grava a saída no formato desejado.

```
data/*.json  ──►  Extract  ──►  Transform (KPI)  ──►  Load (CSV / Parquet)
```

## Estrutura do projeto

```
projeto_etl_parquet/
├── data/                  # Arquivos JSON de entrada (coleta diária)
│   ├── coleta_dia01.json
│   ├── coleta_dia02.json
│   └── coleta_dia03.json
├── etl.py                 # Funções de extração, transformação e carga
├── pipeline.py            # Script de orquestração do pipeline
├── dados.csv              # Saída gerada (CSV)
├── pyproject.toml         # Dependências e metadados (Poetry)
└── README.MD
```

## Etapas do ETL

As funções estão definidas em [etl.py](etl.py):

| Etapa | Função | Descrição |
|-------|--------|-----------|
| **Extract** | `extrair_dados(pasta)` | Lê todos os `.json` da pasta e consolida em um único `DataFrame`. |
| **Transform** | `calcular_kpi_total_de_vendas(df)` | Cria a coluna `Total` = `Quantidade` × `Venda`. |
| **Load** | `carregar_dados(df, format_saida)` | Exporta o `DataFrame` para `csv` e/ou `parquet`. |

### Formato dos dados de entrada

Cada arquivo JSON contém uma lista de registros de venda:

```json
{
    "Produto": "Notebook Gamer",
    "Categoria": "Eletrônicos",
    "Quantidade": 3,
    "Venda": 1500,
    "Data": "2023-01-15"
}
```

## Requisitos

- Python `>= 3.11`
- [Poetry](https://python-poetry.org/) (gerenciador de dependências)

Dependências principais:

- `pandas`
- `pyarrow` (suporte ao formato Parquet)
- `pandera` (validação de dados)

## Instalação

```bash
# Instalar as dependências
poetry install
```

## Como executar

Executando o módulo ETL completo (gera `dados.csv` e `dados.parquet`):

```bash
poetry run python etl.py
```

Ou rodando o pipeline orquestrado (gera apenas `dados.csv`):

```bash
poetry run python pipeline.py
```

## Saída

Após a execução, é gerado um arquivo com os dados consolidados e a coluna `Total` calculada:

| Produto | Categoria | Quantidade | Venda | Data | Total |
|---------|-----------|------------|-------|------|-------|
| Notebook Gamer | Eletrônicos | 3 | 1500 | 2023-01-15 | 4500 |

## Autor

**Guilherme Moreno**
