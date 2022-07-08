fibo = 1;
nacci = 0;
soma = 0;
i = 0;
numberIs = 0;

number = int(input("Confira se o número faz parte da sequência de Fibonacci ou não: "))

while i < number:
    soma = fibo + nacci
    nacci = fibo
    fibo = soma
    if soma == number:
        numberIs = 1;
        break;
    else:
        numberIs = 0;
    i += 1

if numberIs == 1:
    print("O número " + str(number) + " faz parte da sequência de Fibonacci")
else:
    print("O número " + str(number) + " NÃO faz parte da sequência de Fibonacci")

