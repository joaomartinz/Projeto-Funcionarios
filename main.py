from models import Funcionario, Departamento, Empresa

empresa = Empresa()

lista_funcionarios = {
    "001": Funcionario("001", "2023-01-01", 5000, "D001", "Alice", 30, "Engenheira"),
    "002": Funcionario("002", "2023-02-01", 6000, "D002", "Bob", 35, "Gerente"),
    "003": Funcionario("003", "2023-03-01", 5500, "D001", "Charlie", 28, "Analista"),
    "004": Funcionario("004", "2023-04-01", 7000, "D003", "Diana", 40, "Diretora"),
    "005": Funcionario("005", "2023-05-01", 4800, "D002", "Eve", 25, "Assistente"),
    "006": Funcionario("006", "2023-06-01", 6200, "D001", "Frank", 32, "Desenvolvedor"),
    "007": Funcionario("007", "2023-07-01", 5300, "D003", "Grace", 29, "Consultora"),
    "008": Funcionario("008", "2023-08-01", 5800, "D002", "Hank", 38, "Supervisor"),
    "009": Funcionario("009", "2023-09-01", 4900, "D001", "Ivy", 27, "Coordenadora"),
    "010": Funcionario("010", "2023-10-01", 7500, "D003", "Jack", 45, "Presidente"),
    "011": Funcionario("011", "2023-11-01", 5200, "D002", "Kathy", 31, "Especialista"),
    "012": Funcionario("012", "2023-12-01", 6100, "D001", "Leo", 33, "Arquiteto"),
    "013": Funcionario("013", "2024-01-01", 5400, "D003", "Mona", 26, "Técnica"),
    "014": Funcionario("014", "2024-02-01", 6800, "D002", "Nate", 39, "Líder"),
    "015": Funcionario("015", "2024-03-01", 4700, "D001", "Olivia", 24, "Estagiária"),
    "016": Funcionario("016", "2024-04-01", 6300, "D003", "Paul", 34, "Administrador"),
    "017": Funcionario("017", "2024-05-01", 5600, "D002", "Quinn", 29, "Analista de Dados"),
    "018": Funcionario("018", "2024-06-01", 5900, "D001", "Rita", 36, "Engenheira de Software"),
    "019": Funcionario("019", "2024-07-01", 5100, "D003", "Sam", 28, "Consultor de TI"),
    "020": Funcionario("020", "2024-08-01", 7200, "D002", "Tina", 41, "Gerente de Projetos")
}

lista_departamentos = {
    "D001": Departamento("D001", "Desenvolvimento"),
    "D002": Departamento("D002", "Recursos Humanos"),
    "D003": Departamento("D003", "Financeiro")
}

for dept in lista_departamentos.values():
    empresa.cadastrar_departamento(dept)

for func in lista_funcionarios.values():
    empresa.cadastrar_funcionario(func)

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Funcionário")
        print("2. Cadastrar Departamento")
        print("3. Buscar Funcionário por ID")
        print("4. Listar Funcionários")
        print("5. Listar Departamentos")
        print("6. Remover Funcionário")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id = input("ID: ")
            data_registro = input("Data de Registro (YYYY-MM-DD): ")
            salario = float(input("Salário: "))
            departamento_id = input("ID do Departamento: ")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cargo = input("Cargo: ")
            novo_funcionario = Funcionario(id, data_registro, salario, departamento_id, nome, idade, cargo)
            empresa.cadastrar_funcionario(novo_funcionario)
            print("Funcionário cadastrado com sucesso!")

        elif escolha == "2":
            id = input("ID do Departamento: ")
            nome = input("Nome do Departamento: ")
            novo_departamento = Departamento(id, nome)
            empresa.cadastrar_departamento(novo_departamento)
            print("Departamento cadastrado com sucesso!")

        elif escolha == "3":
            id = input("ID do Funcionário: ")
            funcionario = empresa.buscar_funcionario_por_id(id)
            if funcionario:
                print(funcionario)
            else:
                print("Funcionário não encontrado.")

        elif escolha == "4":
            funcionarios = empresa.listar_funcionarios()
            for func in funcionarios:
                print(func)

        elif escolha == "5":
            departamentos = empresa.listar_departamentos()
            for dept in departamentos:
                print(f"Departamento(id={dept.id}, nome={dept.nome})")

        elif escolha == "6":
            id = input("ID do Funcionário a ser removido: ")
            funcionario = empresa.buscar_funcionario_por_id(id)
            if funcionario:
                empresa.remover_funcionario(funcionario)
                print("Funcionário removido com sucesso!")
            else:
                print("Funcionário não encontrado.")

        elif escolha == "7":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()