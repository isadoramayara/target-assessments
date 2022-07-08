inverte = input("Digite a frase que você deseja inverter: ")
i = 1;
length = len(inverte);
inverso = ""

while i < length + 1:
    inverso += inverte[length - i]
    i += 1

print ("Sua frase invertida é: " + inverso);

