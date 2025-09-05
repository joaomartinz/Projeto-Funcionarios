class Funcionario:
    def __init__(self, id, data_admissao, salario, departamento_id, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.id = id
        self.data_admissao = data_admissao
        self.salario = salario
        self.departamento_id = departamento_id

    def __str__(self):
        return f"Funcionario(id={self.id}, nome={self.nome}, idade={self.idade}, cargo={self.cargo}, salario={self.salario}, departamento_id={self.departamento_id})"


class Departamento:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)

    def listar_funcionarios(self):
        return self.funcionarios
    


class Empresa:
    def __init__(self):
        self.departamentos = []
        self.funcionarios = []
   
    def cadastrar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def cadastrar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        for dept in self.departamentos:
            if dept.id == funcionario.departamento_id:
                dept.adicionar_funcionario(funcionario)
                break

    def buscar_funcionario_por_id(self, id):
        for funcionario in self.funcionarios:
            if funcionario.id == id:
                return funcionario
        return None
    
    def listar_funcionarios(self):
        return self.funcionarios
    
    def listar_departamentos(self):
        return self.departamentos

    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)
        for dept in self.departamentos:
            if dept.id == funcionario.departamento_id:
                dept.remover_funcionario(funcionario)
                break