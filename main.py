from random import randint
from time import sleep

print('='*30)
print("     JOGO DA MEGA SENA       ")
print('='*30)

jogos = []  #* Lista que vai guardar todos os jogos
quantidade = int(input("Quantos jogos voce quer que eu sorteie? "))

print(f"\nSORTEANDO {quantidade} JOGOS...")
sleep(1)

for i in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1,60)
        if numero not in jogo:  #* Evita numeros repetidos
            jogo.append(numero)
    jogo.sort()  #* Deixa os numeros em ordem crescente
    jogos.append(jogo)  

#* Exibir os resultados
for i, lista in enumerate(jogos):  
    print(f"Jogo {i+1}: {lista}")
    sleep(0.5)  #* Da um efeito de sorteio

print("-="*30)
print("BOA SORTE!!!")
