from models import Funcionario, Departamento, Empresa
import json

def carregar_dados():
    try:
        with open("dados.json", "r") as file:
            dados = json.load(file)
            funcionarios = dados.get("funcionarios", [])
            departamentos = dados.get("departamentos", [])
            return funcionarios, departamentos
    except FileNotFoundError:
        return [], []
    
def salvar_dados(funcionarios, departamentos):
    with open("dados.json", "w") as file:
        dados = {
            "funcionarios": funcionarios,
            "departamentos": departamentos
        }
        json.dump(dados, file, indent=4)

empresa = Empresa()

def main():

    funcionarios, departamentos = carregar_dados()

    for dept_data in departamentos:
        dept = Departamento(dept_data['id'], dept_data['nome'])
        empresa.cadastrar_departamento(dept)
        
    for func_data in funcionarios:
        func = Funcionario(func_data['id'], func_data['data_registro'], func_data['salario'], func_data['departamento_id'], func_data['nome'], func_data['idade'], func_data['cargo'])
        empresa.cadastrar_funcionario(func)
    
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