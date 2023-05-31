from database import Database
from TeacherCRUD import TeacherCRUD

def main():
    # Criar uma instância da classe Database
    db = Database("bolt://52.55.147.3:7687", "neo4j", "straw-downgrade-analogs")

    # Criar uma instância da classe TeacherCRUD
    teacher_crud = TeacherCRUD(db)

    while True:
        print("Escolha uma opção:")
        print("1. Adicionar Teacher")
        print("2. Pesquisar Teacher")
        print("3. Atualizar CPF do Teacher")
        print("4. Deletar Teacher")
        print("5. Sair")

        opcao = input("Opção selecionada: ")

        if opcao == "1":
            name = input("Digite o nome do Teacher: ")
            ano_nasc = input("Digite o ano de nascimento do Teacher: ")
            cpf = input("Digite o CPF do Teacher: ")

            teacher_crud.create(name, ano_nasc, cpf)
            print("Teacher adicionado com sucesso.")

        elif opcao == "2":
            name = input("Digite o nome do Teacher: ")

            teacher = teacher_crud.read(name)
            if teacher:
                print("Teacher encontrado:")
                print(teacher)
            else:
                print("Teacher não encontrado.")

        elif opcao == "3":
            name = input("Digite o nome do Teacher: ")
            new_cpf = input("Digite o novo CPF do Teacher: ")

            teacher_crud.update(name, new_cpf)
            print("CPF do Teacher atualizado com sucesso.")

        elif opcao == "4":
            name = input("Digite o nome do Teacher: ")

            teacher_crud.delete(name)
            print("Teacher deletado com sucesso.")

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

    # Fechar a conexão com o banco de dados
    db.close()


if __name__ == "__main__":
    main()
