#Tarefa: Abaixo estão as etapas:
import random


#Construa um jogo de adivinhação de números, no qual o usuário seleciona um intervalo.
#Digamos que o usuário tenha selecionado um intervalo, ou seja, de A a B , onde A e B pertencem a inteiro.
#Algum inteiro aleatório será selecionado pelo sistema e o usuário deve adivinhar esse inteiro no número mínimo de adivinhações

def selecionarIntervalo():
    intervalA = input("""
Selecione o Intervalo (A, B):
          
Intervalo A: """)
    intervalB = input("""
Selecione o Intervalo (A, B):
          
Intervalo B: """)
    number = random.randint(int(intervalA), int(intervalB))

    return number

def adivinhar(number):
    number = number
    guessTry = False
    count = 0
    while guessTry == False:
        guess = int(input("""
ADIVINHE O NUMERO: """))
        if guess == number:
            count += 1
            print(f'Parabens você acertou com {count} tentativas!!')
            guessTry = True
        else:
            if guess > number:
                print('Valor muito alto tente novamente!')
                count+=1
            elif guess < number:
                print('Valor muito baixo tente novamente!')
                count+=1

adivinhar(selecionarIntervalo())