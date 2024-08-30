#sequencia de fibonnaci
def sequencia_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

#número a ser verificado
numero = int(input("Informe um número: "))

#checagem do numero: 
if sequencia_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
