numero = int(input("Digite um número inteiro entre 1 e 999: "))

# Função para decompor o número em centenas, dezenas e unidades
def decompor(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    return centenas, dezenas, unidades

# Função para converter cada parte em romano
def converter_para_romano(centenas, dezenas, unidades):
    romanos = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    def get_romano(valor, unidade_base):
        resultado = ''
        for base, simbolo in sorted(romanos.items(), reverse=True):
            while valor >= base:
                resultado += simbolo
                valor -= base
        return resultado

    # Converter as partes do número
    romano_centenas = get_romano(centenas * 100, 100)
    romano_dezenas = get_romano(dezenas * 10, 10)
    romano_unidades = get_romano(unidades, 1)

    return romano_centenas + romano_dezenas + romano_unidades

# Verificar se o número está dentro do intervalo permitido
if 1 <= numero <= 999:
    centenas, dezenas, unidades = decompor(numero)
    resultado_romano = converter_para_romano(centenas, dezenas, unidades)
    print(f"O número {numero} em romano é: {resultado_romano}")
else:
    print("Valor fornecido fora dos limites operacionais")