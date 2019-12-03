########## TELA INICIAL ##########

#Arquivos do programa
from LCR import revenda             #Leitura e cálculo de revenda
from Config import config
from Backup import backup
import platform

#Biblioteca
import os

#Tela inicial
def tela_inicial ():
    
    #Limpa a tela
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        print('Sistema operacional não aceito')
        return

    #Cabeçalho
    print('\t\tThe Reselling Machine\n')
    
    #Menu
    print('1 - Inserir novo XML')
    print('2 - Backup')
    print('3 - Configurações')
    print('4 - Sair')
    print()

    opcao = input('Escolha uma opção: ')

    #Seleciona a tela
    if (opcao == '1'):
        revenda()
        
    elif (opcao == '2'):
        backup()
    
    elif (opcao == '3'):
        config()
         
    elif (opcao == '4'):
        return

    else:
        input("\nOpção inválida. Pressione enter.")
    
    #Usuário fica na tela inicial até sair do programa
    tela_inicial()

#Função principal
def main ():
    tela_inicial()

#Chamada da main
if __name__ == '__main__':
    main()
