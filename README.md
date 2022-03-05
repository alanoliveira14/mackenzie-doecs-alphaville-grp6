# MACKENZIE: GIT - GROUP 6 #
![Build Status](https://github.com/gabumoreira/mackenzie-doecs-alphaville-grp6/actions/workflows/build.yml/badge.svg)

## Abstract ##

A aplicação tem como função principal executar analises aritimeticas e gerar relatórios sobre a venda de Carros da VemCar. 

## I. Environment ##

Para padronizar os ambientes e garantir que o ambiente local reflita o maximo possivel os ambientes produtivos, é recomendado utilizar o PYENV para criar um ambiente virtual com as dependências do projeto isoladas.

```bash
$ pyenv activate env/<ENVIROMENT_NAME>
```

Os ambiente mapeados são:
| Ambiente      | Porta | Usuário | Descrição |
| --            | --    | --      | --        |
| local         | 5001  | local   | Para testes locais e desenvolvimento | 
| development   | 5001  | dev     | Ambiente para validações e testes integrados em ambiente compartilhado |
| homolgation   | 5001  | homolog | Ambiente estavel para homologação e documentação de evidências | 
| production    | 5001  | prod890 | Ambiente produtivo e aberto para usuarios |

## II. Development Requirements ##

### A. Versions ###
O projeto utiliza a versão 3.8.2 do Python, demais dependencias são listadas no arquivo requirements.txt

### B. Running Server ###
```bash
$ pip install -r requirements.txt
$ python .
```

### C. Running Tests ###
```bash
$ pip install -r requirements.txt
$ pytest
```

### D. Command to build project in docker ###
```bash
sudo docker build -t mackenzie-group-x .
sudo docker run -p 5001:5001 -d mackenzie-group-x
```
_______________________________________________________
