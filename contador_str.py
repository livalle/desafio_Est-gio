#recebimento da string pelo usuario
texto = input("Digite uma string: ")

contador = 0
#laço for para verificação
for letra in texto:
    if letra == 'a' or letra == 'A':
        contador += 1

if contador > 0:
    print(f"A letra 'a' aparece {contador} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
