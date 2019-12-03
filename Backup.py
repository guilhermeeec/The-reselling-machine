import os

def backup(quant_prod_exibidos=3):

    os.system('clear' or 'cls')

    print('************************* BACKUPS ************************\n')

    print('Lista de produtos com a data da última modificação')
    
    backups = open('Backup.txt', 'r')
    backups.seek(0)

    matriz=[]
    
    if backups.read() == None:
        input('Não há produtos no backup')
        return
    
    backups.seek(0)
    for produto in backups.readlines():
        matriz.append(produto.split('~')[:-1])
    
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
    print('Pressione "D" para deletar um produto de Bakcup')
    print('Digite "v" para voltar')
    
    entrada = input()

    if entrada == 'v' or entrada == 'V':
        return

def main():
    backup()

if __name__ == '__main__':
    main()
