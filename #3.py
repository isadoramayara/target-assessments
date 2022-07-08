#a
i = 0;
logicVar = 1;

while i < 4:
    logicVar = logicVar + 2
    i += 1

print("a) Último elemento é " + str(logicVar))

#b
i = 0
logicVar = 1

while i < 7:
    logicVar = logicVar * 2
    i += 1

print("b) Último elemento é " + str(logicVar))

#c
i = 0
logicVar = 0
oddSum = 1

while i < 7:
    logicVar = logicVar + oddSum
    oddSum = oddSum + 2
    i += 1

print("c) Último elemento é " + str(logicVar))

#d
i = 0
logicVar = 4
prog = 12

while i < 4:
    logicVar = logicVar + prog
    prog = prog + 8
    i += 1

print("d) Último elemento é " + str(logicVar))

#e
i = 0
logicVar = 0
fibbo = 1

while i < 7:
    soma = logicVar + fibbo
    logicVar = fibbo
    fibbo = soma
    i += 1

print("e) Último elemento é " + str(logicVar))

#f
i = 0
logicVar = 16

while i < 4:
    logicVar += 1
    i += 1
    
print("f) Último elemento é " + str(logicVar) + "0")
