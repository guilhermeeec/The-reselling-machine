########## LEITURA DO XML E CÁLCULO DE REVENDA ##########

#Bibliotecas
import os
from pathlib import Path
from datetime import date

#Arquivo do programa
from Parser import parser 

#Pega todos os xml do diretório predefinido
def varre_xml (end_dir_predef):
 
    #Cria uma lista vazia com os arquivos xml do diretório pré-definido
    lista_xml = []

    #Varre uma lista com os arquivos do diretório pré-definido 
    for arquivo in os.listdir (end_dir_predef):

        #Verifica quais arquivos são xml para listá-los
        if Path(arquivo).suffix == '.xml':
            lista_xml.append(arquivo)
        
    return lista_xml

#Tela 1.1B
def escolher_xml_endereco ():

    #Limpa a tela
    os.system('clear' or 'cls')

    #Cabeçalho
    print('************************** LEITURA DO XML E CÁLCULO DE REVENDA *************************\n')

    print('(digite \'v\' para voltar)\n')
    entrada = input('Digite o endereço do arquivo XML: ')

    #Voltar
    if entrada == 'v' or entrada == 'V':
        return

    else:
        endereco = entrada

    #Verifica se o caminho existe
    if os.path.exists (endereco) == False:
        input('\nEndereço não encontrado')
        retorno = escolher_xml_endereco()
        return retorno
        
    #Verifica se o arquivo tem extensão .xml
    elif Path(endereco).suffix != '.xml':
        input('\nArquivo não possui extensão .xml')
        retorno = escolher_xml_endereco()
        return retorno
        
    #Endereço existe e tem extensão .xml
    else:
        input('\nEndereço encontrado')
        return endereco
    
#Tela 1.1A
def escolher_xml_diretorio (end_dir_predef, quant_xml_exibidos=25):
    
    #Limpa a tela
    os.system('clear' or 'cls')

    #Cabeçalho
    print('************************** LEITURA DO XML E CÁLCULO DE REVENDA *************************\n')

    #Lista de arquivos xml no diretório predefinido
    lista_xml = varre_xml(end_dir_predef)

    #Listagem de xml para o usuário
    print('Lista de XML no diretório predefinido:\n')

    #Calcula a quantidade de arquivos xml a ser exibidos (n)
    n = min(len(lista_xml),quant_xml_exibidos)

    #Lista n arquivos xml
    for item in range(quant_xml_exibidos-25, n):
        print(item+1, end=' - ')
        print(lista_xml[item])
        
    #Pede pro usuário apertar m para exibir mais xml caso existam
    if n < len(lista_xml):
        print('\nPressione "m" para exibir mais')
            
    print('\n(digite "v" para voltar)\n')
    entrada = input('Selecione o XML (ou digite "T" para todos): ')

    #Voltar
    if entrada == 'v' or entrada == 'V':
        return 

    #Exibir mais 25 xml
    elif (entrada == 'm' or entrada == 'M') and n < len(lista_xml):
            
        #Chama a função recursivamente pedindo pra exibir mais 10 xml
        quant_xml_exibidos += 25
        retorno = escolher_xml_diretorio(end_dir_predef, quant_xml_exibidos)
    
    #Processa todos os xml
    elif entrada == 't' or entrada == 'T':
        return 't'
    
    #Digitou algo inválido
    else:
        erro = False

        #Verificar se não digitou um número
        for letra in entrada:
            if ord(letra) < ord('0') or ord(letra) > ord('9'):
                erro = True

        if erro == True:
            input('\nComando inválido')
            retorno = escolher_xml_diretorio(end_dir_predef, quant_xml_exibidos)
        
        #Verificar se o número corresponde a um xml
        elif int(entrada) <= len(lista_xml):
            retorno = end_dir_predef + lista_xml[int(entrada)-1]
            return retorno
    
        else:
            input('\nNão há um XML na lista com esse número')
            retorno = escolher_xml_diretorio(end_dir_predef)
            return retorno

#Salva os produtos em disco
def salvamento_disco(info_xml, margem):
    
    backup = open('Backup.txt', 'a')
    
    #Data de modificação
    data = date.today()
    data_texto = '{}/{}/{}'.format(data.day, data.month, data.year)

    #Escreve os profutos em disco
    for produto in info_xml:
        backup.write(produto['Nome']+'~')
        backup.write(produto['Código']+'~')
        backup.write(produto['Quantidade']+'~')
        backup.write(produto['Total']+'~')
        backup.write(str(produto['ICMS ST'])+'~')
        backup.write(produto['IPI']+'~')
        backup.write(produto['Valor unitário']+'~')
        erro_unitario = False
        for caracter in produto['Valor unitário']:
            if(ord(caracter)<ord('0') and caracter!= '.') or ord(caracter)>ord('9'):
                erro_unitario = True
        if erro_unitario == False:
            backup.write(str(((float(margem))/100 + 1) * float(produto['Valor unitário']))+'~')
        else:
            backup.write('Error'+'~')
        backup.write(data_texto+'~')
        backup.write('\n')

    backup.close()

#Tela 1.2A e 1.2B
def exibir_produtos(info_xml, margem, endereco, maximo=4):
    
    #Verifica quantos xml precisam ser exibidos
    n = min(len(info_xml),maximo)

    #Mostra os produtos na tela
    for produto in range(maximo-4, n):
        
        print(info_xml[produto]['Nome'])
        print('\tQuantidade: ', info_xml[produto]['Quantidade'])
        print('\tPreço unitário: ', info_xml[produto]['Valor unitário'])
        
        #Alguns produtos não consegui acessar o valor unitário
        erro_unitario = False
        for caracter in info_xml[produto]['Valor unitário']:
            if (ord(caracter)<ord('0') and caracter != '.') or ord(caracter)>ord('9'):
                erro_unitario = True
        if erro_unitario == False:
            print('\tPreço de revenda: ', ((float(margem)/100) + 1) * float(info_xml[produto]['Valor unitário']))
        else:
            print('\tPreço de revenda: NÃO PODE SER CALCULADO')
        print()
    
    #Verifica se ja exibiu todos os produtos
    if n < len(info_xml):
        print('\nPressione "m" para exibir mais\n')

    print('Deseja salvar os dados no sistema?')
    print('Y/N:')

    entrada = input()

    #Exibir mais
    if (entrada == 'm' or entrada == 'M') and (n < len(info_xml)):
        maximo += 4
        exibir_info(endereco, maximo, margem)
        return

    #Salvar em disco
    elif entrada == 'y' or entrada == 'Y':
        salvamento_disco(info_xml, margem)
        return
    
    #Não salvar
    elif entrada == 'n' or entrada == 'N':
        return

    else:
        input('Opção inválida')
        exibir_info(endereco, maximo, margem)
        return

#Tela 1.2A e 1.2B
def exibir_info (endereco, maximo=4, margem=0):
    
    #Limpa a tela
    os.system('clear' or 'cls')
    
    #Lê as configurações da margem de lucro armazenadas em disco
    arq_margem = open('Margem.txt', 'r')
    arq_margem.seek(0)
    margem_on_off = arq_margem.readlines()[0]
    
    #Cabeçalho
    print('************************** LEITURA DO XML E CÁLCULO DE REVENDA *************************\n')
    
    #Verifica se o usuário decidiu processar 1 xml
    if endereco != 't':

        #Lista com os dicionários dos produtos e com o dicionário da nota
        info_xml = parser(endereco)

        #Tira o dicionário da nota
        info_nota = info_xml[-1]

        #Exibe as informações da nota
        print('\nInformações do XML')
        print('\t1 - Fornecedor:', info_nota['Fornecedor'])
        print('\t2 - Data de emissão da nota:', info_nota['Data de emissão'])
        print('\t3 - Chave de acesso da nota:', info_nota['Chave de acesso'])
        print('\t4 - Valor ICMS subst.:', info_nota['ICMS ST'])
        print('\t5 - Valor do IPI:', info_nota['IPI'])
        print('\t6 - Outras despesas:', info_nota['Outras despesas'])
        print('\t7 - Valor total da nota:', info_nota['Valor total'])
        
        #Verifica se a margem de lucro padrão está habilitada
        if margem_on_off == 'Desabilitar\n':
            print('\n*Configurações padrões aplicadas*\n')
            arq_margem.seek(0)
            margem = arq_margem.readlines()[1]
            arq_margem.close()
        
        #Se estiver habilitada e for a primeira vez rodando o programa
        elif margem_on_off == 'Habilitar\n' and maximo == 4:
            margem = input('\nDigite a margem de lucro desejada: ')
            erro = False
            contador_pontos=0

            #Verifica se o usuário digitou algo que não é um número
            for caracter in margem:
                if (ord(caracter)<ord('0') or ord(caracter)>ord('9')) and caracter != '.':
                    erro = True
                if caracter == '.':
                    contador_pontos += 1
            if erro == True or contador_pontos >= 2:
                input('Margem de lucro inválida. Digite um número em porcentagem usando o "." para decimal caso necessário')
                exibir_info(endereco, maximo)
                return
        
        #Vai exibir a margem de lucro que o usuário digitou anteriormente se não for a primeira vez aberto
        else:
            print('Digite a margem de lucro desejada:', margem)
            print()
        
        #Tira o dicionário da nota sobrando apenas os dicionários dos produtos
        info_xml = info_xml[:-1]

        #Processa os xml dos produtos para listá-los na tela
        exibir_produtos(info_xml, margem, endereco, maximo)

    #Todos os xml
    else:

        #Verifica se a margem de lucro padrão está habilitada
        if margem_on_off == 'Desabilitar\n':
            print('*Configurações padrões aplicadas*')
            arq_margem.seek(0)
            margem = arq_margem.readlines()[1]
            arq_margem.close()
        
        #Se estiver habilitada e for a primeira vez rodando o programa
        elif margem_on_off == 'Habilitar\n' and maximo == 6:
            margem = input('\nDigite a margem de lucro desejada: ')
            
            #Verifica se não foi digitado um número 
            erro = False
            contador_pontos=0
            for caracter in margem:
                if (ord(caracter)<ord('0') or ord(caracter)>ord('9')) and caracter != '.':
                    erro = True
                if caracter == '.':
                    contador_pontos += 1
            if erro == True or contador_pontos == len(margem):
                input('Margem de lucro inválida. Digite um número em porcentagem usando o "." para decimal caso necessário')
                exibir_info(endereco, maximo)
                return

        #Vai exibir a margem de lucro que o usuário digitou anteriormente se não for a primeira vez aberto
        else:
            print('Digite a margem de lucro desejada:', margem)
        
        #Verifica o diretório predefinido
        arq_dir_predef = open('Diretorio.txt', 'r')
        end_dir_predef = arq_dir_predef.readlines()[1]
        if end_dir_predef[-1] == '\n':
            end_dir_predef = end_dir_predef[:-1]
        
        #Pega uma lista de arquivos xml
        lista_xml = varre_xml(end_dir_predef)
        
        #Cria uma lista juntando todos os produtos de todos os xml
        listona = []
        for arquivo in lista_xml:
            for produtos in parser(end_dir_predef + arquivo)[:-1]:
                listona.append(produtos)

        #Processa os xml dos produtos para listá-los na tela
        exibir_produtos(listona, margem, endereco, maximo)

#Chama as outras funções
def revenda():

    #Verifica as configurações de diretório predefinido armazenadas em disco
    arq_dir_predef = open('Diretorio.txt', 'r')
    arq_dir_predef.seek(0)
    config_dir_predef = arq_dir_predef.readlines()[0]

    #Verificar se o diretório predefinido está desabilitado
    if config_dir_predef == 'Habilitar\n':
        endereco = escolher_xml_endereco()
    else:
        arq_dir_predef.seek(0)
        end_dir_predef = arq_dir_predef.readlines()[1]
        if end_dir_predef[-1] == '\n':
            end_dir_predef = end_dir_predef[:-1]
        endereco = escolher_xml_diretorio(end_dir_predef)
    arq_dir_predef.close()

    #Pode ser None no caso de a pessoa apertar v para voltar
    if endereco is not None:
        exibir_info(endereco)

#Função principal
def main():
    revenda()

#Chamada da main
if __name__ == '__main__':
    main()
