def exibir_menu():
    print("\n========================================")
    print("         SISTEMA TASKTRACKER            ")
    print("========================================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("========================================")

def cadastrar_tarefa(lista_tarefas):
    print("\n--- Cadastro de Nova Tarefa ---")
    
    # Validação rigorosa do Título (Não pode ser vazio ou apenas espaços)
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo == "":
            print("[ERRO] O título é obrigatório e não pode ficar vazio. Tente novamente.")
        else:
            break
            
    descricao = input("Digite a descrição detalhada (opcional): ").strip()
    
    # Validação estrita da Prioridade (Alta, Média, Baixa)
    while True:
        prioridade = input("Digite a prioridade [Alta / Média / Baixa]: ").strip().capitalize()
        if prioridade == "Media":
            prioridade = "Média"
            
        if prioridade in ["Alta", "Média", "Baixa"]:
            break
        else:
            print("[ERRO] Prioridade inválida! Escolha estritamente entre: Alta, Média ou Baixa.")
            
    data_limite = input("Digite a data limite (formato DD/MM/AAAA): ").strip()
    
    # Geração de ID incremental exclusivo e status padrão "Pendente"
    novo_id = len(lista_tarefas) + 1
    tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não informada",
        "status": "Pendente"
    }
    
    lista_tarefas.append(tarefa)
    print(f"\n[SUCESSO] Tarefa '{titulo}' cadastrada com sucesso sob o ID #{novo_id}!")

def visualizar_tarefas(lista_tarefas):
    print("\n--- Lista de Tarefas Cadastradas ---")
    if len(lista_tarefas) == 0:
        print("Nenhuma tarefa cadastrada até o momento no sistema.")
        return
        
    for t in lista_tarefas:
        print("----------------------------------------")
        print(f"ID: {t['id']}")
        print(f"Título: {t['titulo']}")
        print(f"Descrição: {t['descricao']}")
        print(f"Prioridade: {t['prioridade']}")
        print(f"Data Limite: {t['data_limite']}")
        print(f"Status: {t['status']}")
    print("----------------------------------------")

def main():
    tarefas = []
    print("Bem-vindo ao TaskTracker - Versão Python (Fase 2)")
    print("Desenvolvido por: Paulo Eduardo Fernandes Dias (RA: 22303387)")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até a próxima!")
            break
        else:
            print("\n[ERRO] Opção inválida! Escolha uma opção entre 1 e 3.")

if __name__ == "__main__":
    main()
