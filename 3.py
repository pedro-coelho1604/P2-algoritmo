def fibo(n):
    if n <= 0:
        return "A posição deve ser um número inteiro positivo."

    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

while True:
    numero = input("Informe a posição na sequência de Fibonacci (ou 'stop' para encerrar): ")

    if numero.lower() == 'stop':
        print("Programa encerrado.")
        break

    try:
        posicao = int(numero)
        resultado = fibo(posicao)
        print(f"O valor na posição {posicao} da Sequência de Fibonacci é {resultado}.")
    except ValueError:
        print("Por favor, informe um número inteiro válido para a posição.")