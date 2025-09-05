class Funcionario:
    def __init__(self, id, data_registro, salario, departamento_id, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.id = id
        self.data_registro = data_registro
        self.salario = salario
        self.departamento_id = departamento_id


class Departamento:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Empresa:
    def __init__(self):
        self.departamentos = []
        self.funcionarios = []
   
    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)