########## TELA INICIAL ##########

import LCR
import Configuracoes
import Backup
import os

def tela_inicial ():
    system("clear" or "cls")
    print('\t\tThe Reselling Machine\n')
    print('1 - Inserir novo XML')
    print('2 - Backup')
    print('3 - Confihurações')
    print('4 - Sair')
    print()

    opcao = input('Escolha uma opção: ')

    if (opcao == '1'):
        revenda()
        
    elif (opcao == '2'):
        backup()
    
    elif (opcao == '3'):
        config()
         
    elif (opcao == '4'):
        return

    else:
        input("Opção inválida")
        tela_inicial()
        return

    tela_inicial()


def main ():
    tela_inicial()

main()
