##MVC
#Model
### vai conter a lógica de cálculo # da calculadora.

#View
### vai exibir o resultado na tela.

#Controller
### vai receber as entradas do # usuário e interagir com o modelo.


def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Adição")
    print("2. Subtração")
    print("5. Sair")
    print("-----------------")

##Atividade Prática
# Implementar a multiplicação e divisão
# desafio para calcular a porcentagem e calcular a raiz quadrada.
# Use os menus 3, 4 e 8 para implementar as novas funcionalidades.

def obter_numeros():
    while True:
        try:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, " \
            "digite números válidos.")
    
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            num1, num2 = obter_numeros()
            resultado = num1 + num2
            print(f"Resultado da adição: {resultado}")
        elif opcao == "2":
            num1, num2 = obter_numeros()
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente as seguintes opções: 1, 2 ou 5.")

if __name__ == "__main__":
    main()
