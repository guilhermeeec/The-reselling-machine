########## TELA INICIAL ##########

#Arquivos do programa
import LCR              #Leitura e cálculo de revenda
import Config
import Backup

#Biblioteca
import os

#Tela inicial
def tela_inicial ():
    
    #Limpa a tela
    system("clear" or "cls")

    #Cabeçalho
    print('\t\tThe Reselling Machine\n')
    
    #Menu
    print('1 - Inserir novo XML')
    print('2 - Backup')
    print('3 - Confihurações')
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
        input("Opção inválida")
    
    #Usuário fica na tela inicial até sair do programa
    tela_inicial()

#Função principal
def main ():
    tela_inicial()

#Chamada da main
if __name__ == '__main__':
    main()
