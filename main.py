def carregar_tarefas():
    try:
        with open("tasks.txt","r") as f:
            return [linha.strip() for linha in f.readline()]
    except FileNotFoundError:
        return[]
    
def salvar_tarefas(tarefas):
    with open("task.txt", "w") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa.")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}.{tarefa}")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa:")
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        index =  int(input("Digite o numero da tarefa a remover: "))-1
        if 0<= index < len(tarefas):
            tarefas.pop(index)
            salvar_tarefas(tarefas)
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def main():
    tarefas = carregar_tarefas()
    while True:
        print("\n1. Listar tarefas\n2. Adicionar tarefa\n3. Remover tarefa\n4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            listar_tarefas(tarefas)
        elif escolha == "2":
            adicionar_tarefa(tarefas)
        elif escolha == "3":
            remover_tarefa(tarefas)
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
