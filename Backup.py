import os
import platform

def backup(quant_prod_exibidos=3):
    
    #Limpa a tela
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        print('Sistema operacional não aceito')
        return

    print('************************* BACKUPS ************************\n')
    
    print('Lista de produtos com a data da última modificação\n')
                    
    backups = open('Backup.txt', 'r')
    backups.seek(0)

    matriz=[]

    if backups.read() == 'none\n':
        input('Não há produtos no backup. Pressione enter.')
        return

    backups.seek(0)
    for produto in backups.readlines():
        matriz.append(produto.split('~')[:-1])
    
    matriz.pop(0)

    backups.close()
    
    n = min(len(matriz), quant_prod_exibidos)

    for produto in range(quant_prod_exibidos-3, n):
        print(matriz[produto][-1])
        print(produto+1,'-',matriz[produto][0])
        print('\tCódigo:',matriz[produto][1])
        print('\tQuantidade:',matriz[produto][2])
        print('\tValor total:',matriz[produto][3])
        print('\tValor ICMS ST:',matriz[produto][4])
        print('\tValor IPI:',matriz[produto][5])
        print('\tPreço unitário:',matriz[produto][6])
        print('\tPreço de revenda:',matriz[produto][7])
        print()

    if n < len(matriz):
        print('Pressione "m" para exibir mais')

    print('Pressione "D" para deletar um produto de Backup')
    print('Digite "v" para voltar')

    entrada = input()

    if entrada == 'v' or entrada == 'V':
        return

    elif (entrada == 'm' or entrada == 'M') and n < len(matriz):
        backup(quant_prod_exibidos+3)
        return

    elif entrada == 'd' or entrada == 'D':
        linha = input('Digite o número do produto a ser deletado: ')

        erro_caracter = False
        if linha != "" and linha != 'v' and  linha != 'V':
            for caracter in linha:
                if ord(caracter)<ord('0') or ord(caracter)>ord('9'):
                    erro_caracter = True

        elif linha == 'v' or linha == 'V':
            backup(quant_prod_exibidos)
            return
        
        else:
            erro_caracter = True

        if erro_caracter == True:
            input('Opção inválida. Pressione enter.')
            backup(quant_prod_exibidos)
            return

        else:
            linha = int(linha)
            if linha > len(matriz):
                input('Esse número não corresponde a nenhum produto. Pressione enter.')
                backup(quant_prod_exibidos)
                return
            else:
                backups = open('Backup.txt', 'r')
                backups.seek(0)
                produtos = backups.readlines()
                produtos.pop(linha)
                backups.close()
                backups = open('Backup.txt', 'w')
                backups.seek(0)
                backups.writelines(produtos)
                backups.close()
                backup(quant_prod_exibidos)
                return
    
    else:
        input('Opção inválida. Pressione enter.')
        backup(quant_prod_exibidos)
        return

def main():
    backup()

if __name__ == '__main__':
    main()
