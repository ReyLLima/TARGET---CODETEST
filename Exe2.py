def pertence_fibonacci(numero):
    fib1, fib2 = 0, 1
    
    if numero == fib1 or numero == fib2:
        return f"O número {numero} pertence à sequência de Fibonacci."
    
    while fib2 < numero:
        fib1, fib2 = fib2, fib1 + fib2
    
    if fib2 == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)
