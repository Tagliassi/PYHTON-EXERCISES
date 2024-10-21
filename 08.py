Numbers = []

print("Digite três números inteiros: ", Numbers.append(int(input())), Numbers.append(int(input())), Numbers.append(int(input())))

print(Numbers)

print("O maior número é: ", max(Numbers), "e o menor número é: ", min(Numbers))

#Numbers.sort(reverse=True)

# Ordenar os números colocando os múltiplos de 2 primeiro
Numbers.sort(key=lambda x: (x % 2 != 0, x))

print("Os números em ordem decrescente são: ", Numbers)