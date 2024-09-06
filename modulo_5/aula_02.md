
# Aula 2 - *Pandas* - *DataFrame*

**Objetivo:** apresentar o conceito de *DataFrames* da biblioteca ***Pandas***.

## ***DataFrame***

Em ***Pandas***, o ***DataFrame*** é uma estrutura de dados bidimensional, que permite manipular, processar e analisar dados.

As principais características do ***DataFrame Pandas*** são:

- Estrutura **bidimensional**: organizada em **linhas** e **colunas**
- Estrutura **heterogênea**: as colunas podem armazenar diferentes tipos de dados: *int*, *float*, *str*, etc.
- **Etiquetas** (*labels*): cada linha e coluna possuem rótulos (*labels*) associados, que facilitam o acesso e a manipulação de dados. As **linhas** são indexadas (0 - n), sendo que o índice pode ser personalizado.
- **Alinhamento automático**: operações entre diferentes *dataframes* são automaticamente alinhadas pelos *labels* das linhas e colunas.
- **Processamento Eficiente**: oferece funções e métodos eficientes para a manipulação,  filtragem, agregação, ordenação e tratamento de dados.
- **Interoperabilidade**: oferece compatibilidade com diversos formatos de arquivo, como CSV, Excel, JSON, SQL, etc.

## Funções Principais

Para o uso da biblioteca *Pandas* é necessário importar a biblioteca `pandas` e para abrir um arquivo é possível usar a função `read_csv`, como exemplo no código a seguir:

```python
import pandas as pd

from pandas.core.frame import DataFrame

file_path: str = "kc_house_data.csv"
data_set: DataFrame = pd.read_csv(file_path, sep=",", header=0)

print(type(data_set))
print(data_set)
```

Como resultado é apresentado os dados do arquivo CSV, com 21.613 linhas e 21 colunas.

Para imprimir as primeiras linhas de um *DataFrame* é possível usar o método `head(lines[optional, default=5])`. Enquanto que para imprimir as últimas linhas de um *DataFrame* existe o método `tail(lines[optional, default=5])`. Para buscar uma amostra aleatória existe o método `sample`:

```python
import pandas as pd

from pandas.core.frame import DataFrame

file_path: str = "kc_house_data.csv"
data_set: DataFrame = pd.read_csv(file_path, sep=",", header=0)

print(data_set.head())
print(data_set.tail())

print(data_set.head(150))
print(data_set.tail(10))
print(data_set.sample(10))
```

As colunas são organizadas de acordo com um *label*, e para indexar os dados por uma coluna é possível usar o parâmetro `index_col` da função `read_csv`. No exemplo, o *DataFrame* é indexado pela coluna `date`:

```python
import pandas as pd

from pandas.core.frame import DataFrame

file_path: str = "kc_house_data.csv"
data_set: DataFrame = pd.read_csv(file_path, sep=",", index_col="date")

print(data_set)
```

Para selecionar um subconjunto de *labels* do arquivo é possível usar o parâmetro `usecols` da função `read_csv`, como apresentado a seguir:

```python
import pandas as pd

from pandas.core.frame import DataFrame

file_path: str = "kc_house_data.csv"
labels: list[str] = ["date", "price", "zipcode"]
data_set: DataFrame = pd.read_csv(file_path, sep=",", usecols=labels)

print(data_set)
print(date_set.head())
```

O *pandas* possui implementações que facilitam extrair informações sobre o *DataFrame*:

- Atributo `shape` é responsável por retornar uma tupla com as dimensões do *DataFrame*.
- Atributo `columns` é responsável por retornar o nome dos *labels* do *DataFrame*.
- Método `count` é responsável por retornar o número de linhas do *DataFrame*.
- Método `describe` apresenta informações estatísticas (mínimo, máximo, média e desvio padrão) do *DataFrame*.
- Método `info` apresenta informações sobre as colunas e uso de memória do *DataFrame*.

```python
import pandas as pd

from pandas.core.frame import DataFrame

file_path: str = "kc_house_data.csv"
data_set: DataFrame = pd.read_csv(file_path, sep=",")

print(data_set.columns)
print(data_set.count())
print(data_set.describe())
print(data_set.info())
```
