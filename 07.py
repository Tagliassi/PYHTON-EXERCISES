numero = int(input("Digite um número inteiro entre 1 e 999: "))

Unidades = ['I', 'V']
Dezenas = ['X', 'L']
Centenas = ['C', 'D']
Milhares = ['M']

Decomposto = []
romano = []

def decompor(numero):
    
    numero_str = str(numero)
    
    if(numero < 10):
        return Decomposto.append(int(numero_str[0]))
    elif(numero > 10 and numero < 100):
        Decomposto.append(int(numero_str[0])*10) 
        Decomposto.append(int(numero_str[1]))
        return Decomposto
    elif(numero > 100 and numero < 1000):
        Decomposto.append(int(numero_str[0])*100)
        Decomposto.append(int(numero_str[1])*10)
        Decomposto.append(int(numero_str[2]))
        return Decomposto
    elif(numero > 1000 and numero < 10000):
        Decomposto.append(int(numero_str[0])*1000)
        Decomposto.append(int(numero_str[1])*100)
        Decomposto.append(int(numero_str[2])*10)
        Decomposto.append(int(numero_str[3]))
        return Decomposto

decompor(numero)
print(Decomposto)

def converter_para_romano(decomposto):
    
    for _ in range(len(decomposto)):
        for i, valor in enumerate(decomposto):
            if i == 0 and len(decomposto) == 1:  # Unidade
                if valor == 1:
                    romano.append('I')
                elif valor == 5:
                    romano.append('V')
                elif valor < 4:
                    romano.append('I' * valor)
                elif valor == 4:
                    romano.append('IV')
                elif valor == 9:
                    romano.append('IX')
                elif valor > 5:
                    romano.append('V' + 'I' * (valor - 5))
            elif i == 0 and len(decomposto) == 2:  # Dezena
                if valor == 10:
                    romano.append('X')
                elif valor == 50:
                    romano.append('L')
                elif valor < 40:
                    romano.append('X' * (valor // 10))
                elif valor == 40:
                    romano.append('XL')
                elif valor == 90:
                    romano.append('XC')
                elif valor > 50:
                    romano.append('L' + 'X' * ((valor - 50) // 10))
            elif i == 0 and len(decomposto) == 3:  # Centena
                if valor == 100:
                    romano.append('C')
                elif valor == 500:
                    romano.append('D')
                elif valor < 400:
                    romano.append('C' * (valor // 100))
                elif valor == 400:
                    romano.append('CD')
                elif valor == 900:
                    romano.append('CM')
                elif valor > 500:
                    romano.append('D' + 'C' * ((valor - 500) // 100))
            elif i == 0 and len(decomposto) == 4:  # Milhar
                romano.append('M' * (valor // 1000))             
        decomposto.pop(0)
    print(''.join(romano))

if(numero < 1 or numero > 999):
    print("Valor fornecido fora dos limites operacionais")
else:
    converter_para_romano(Decomposto)