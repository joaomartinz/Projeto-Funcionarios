# Sistema de Cadastro de Funcionários em Python

## Visão Geral

O projeto **Sistema de Cadastro de Funcionários** é uma aplicação em **Python**, construída utilizando **Programação Orientada a Objetos (POO)**, que permite gerenciar informações de funcionários e departamentos de forma organizada e persistente.

O sistema armazena os dados em um arquivo **JSON**, garantindo que todas as informações sejam mantidas mesmo após o fechamento do programa. Ele é ideal para empresas que desejam um controle básico de funcionários, departamentos e suas relações.

![Exemplo Menu](https://via.placeholder.com/600x150?text=Menu+do+Sistema)

---

## Funcionalidades

O sistema possui um **menu interativo** com as seguintes funcionalidades:

| Opção | Função                    | Descrição                                                               |
| ----- | ------------------------- | ----------------------------------------------------------------------- |
| 1     | Cadastrar Funcionário     | Adiciona um novo funcionário, vinculando-o a um departamento existente. |
| 2     | Cadastrar Departamento    | Cria um novo departamento para a empresa.                               |
| 3     | Buscar Funcionário por ID | Localiza um funcionário pelo seu ID único.                              |
| 4     | Listar Funcionários       | Mostra todos os funcionários cadastrados com seus dados.                |
| 5     | Listar Departamentos      | Exibe todos os departamentos e seus IDs.                                |
| 6     | Remover Funcionário       | Remove um funcionário da empresa e do seu departamento.                 |
| 7     | Sair                      | Encerra a aplicação.                                                    |

---

## Estrutura do Projeto

### 1. **Funcionario**

* Representa um funcionário individual.
* Atributos:

  * `id`: ID único do funcionário.
  * `nome`: Nome completo.
  * `idade`: Idade.
  * `cargo`: Cargo ocupado.
  * `salario`: Salário mensal.
  * `data_admissao`: Data de admissão.
  * `departamento_id`: ID do departamento ao qual pertence.
* Método `__str__`: Exibe o funcionário de forma legível.

### 2. **Departamento**

* Representa um departamento da empresa.
* Atributos:

  * `id`: ID do departamento.
  * `nome`: Nome do departamento.
  * `funcionarios`: Lista de funcionários pertencentes.
* Métodos:

  * `adicionar_funcionario(funcionario)`
  * `remover_funcionario(funcionario)`
  * `listar_funcionarios()`

### 3. **Empresa**

* Gerencia os funcionários e departamentos.
* Atributos:

  * `funcionarios`: Lista completa de funcionários.
  * `departamentos`: Lista completa de departamentos.
* Métodos:

  * `cadastrar_funcionario(funcionario)`
  * `cadastrar_departamento(departamento)`
  * `buscar_funcionario_por_id(id)`
  * `listar_funcionarios()`
  * `listar_departamentos()`
  * `remover_funcionario(funcionario)`

---

## Exemplos de Uso

### Cadastrando Funcionário

```
Escolha uma opção: 1
ID: 021
Data de Admissão (YYYY-MM-DD): 2025-09-05
Salário: 5000
ID do Departamento: D004
Nome: Joao Martins
Idade: 23
Cargo: Chefe
Funcionário cadastrado com sucesso!
```

### Listando Funcionários

```
Funcionario(id=001, nome=Alice, idade=30, cargo=Engenheira, salario=5000, departamento_id=D001)
Funcionario(id=002, nome=Bob, idade=35, cargo=Gerente, salario=6000, departamento_id=D002)
Funcionario(id=021, nome=Joao Martins, idade=23, cargo=Chefe, salario=5000, departamento_id=D004)
```

### Removendo Funcionário

```
Escolha uma opção: 6
ID do Funcionário a ser removido: 021
Funcionário removido com sucesso!
```

---

## Persistência de Dados

* Todos os dados são salvos no arquivo `dados.json`.
* Estrutura JSON para um funcionário:

```json
{
    "id": "001",
    "data_admissao": "2023-01-01",
    "salario": 5000,
    "departamento_id": "D001",
    "nome": "Alice",
    "idade": 30,
    "cargo": "Engenheira"
}
```

* Estrutura JSON para um departamento:

```json
{
    "id": "D001",
    "nome": "Desenvolvimento"
}
```

---

## Tecnologias Utilizadas

* **Python 3** – Linguagem de programação principal.
* **POO** – Organização das informações em classes e objetos.
* **JSON** – Armazenamento persistente de dados.
* **Terminal/Console** – Interface de interação com o usuário.

---

## Benefícios

* Sistema simples e intuitivo para gestão de funcionários.
* Persistência de dados com JSON.
* Estrutura modular e escalável para novos recursos, como relatórios e gráficos.
* Exemplo prático de POO aplicada à gestão de informações corporativas.

![Exemplo Funcionários](https://via.placeholder.com/600x200?text=Lista+de+Funcionários)

---

## Como Usar

1. Clone o repositório ou baixe os arquivos do projeto.
2. Certifique-se de ter Python 3 instalado no seu computador.
3. Execute o arquivo principal `main.py`.
4. Navegue pelo menu interativo para cadastrar, listar, buscar ou remover funcionários e departamentos.
5. Todos os dados serão salvos automaticamente no arquivo `dados.json`.

---

Este projeto demonstra como conceitos de **POO e manipulação de arquivos** podem ser aplicados de forma prática para criar sistemas de gestão de funcionários simples, mas eficazes, em Python.
