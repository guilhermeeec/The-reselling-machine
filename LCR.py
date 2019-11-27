########## LEITURA DO XML E CÁLCULO DE REVENDA ##########

import os
from Parser import parser 
from pathlib import Path

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
    print('************************** LEITURA DO XML E CÁLCULO DE REVENDA *************************')

    print('(digite \'v\' para voltar)\n')
    entrada = input('Digite o endereço do arquivo XML: ')

    if entrada == 'v' or entrada == 'V':
            
        #Código de voltar
        return

    else:
        endereco = entrada

    #Verifica se o caminho existe
    if os.path.exists (endereco) == False:
        input('\nEndereço não encontrado')
        retorno = escolher_xml_endereco()
        
    #Verifica se o arquivo tem extensão .xml
    elif Path(endereco).suffix != '.xml':
        input('\nArquivo não possui extensão .xml')
        retorno = escolher_xml_endereco()
        
    #Endereço existe e tem extensão .xml
    else:
        input('\nEndereço encontrado')
        return endereco

    return retorno
    
#Tela 1.1A
def escolher_xml_diretorio (end_dir_predef, quant_xml_exibidos=10):
    
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
    for item in range(quant_xml_exibidos-10, n):
        print(item+1, end=' - ')
        print(lista_xml[item])
        
    #Pede pro usuário apertar seta pra baixo ou m para exibir mais xml caso existam
    if n < len(lista_xml):
        print('\nPressione seta para baixo (ou \'m\') para exibir mais')
            
    print('\n(digite \'v\' para voltar)\n')
    entrada = input('Selecione o XML (ou digite \'T\' para todos): ')

    #Tratamento de erro
    if entrada == 'v' or entrada == 'V':

        #Código de voltar
        return 

    #'^[[B' = seta para baixo
    elif entrada == 'm' or entrada == 'M' or entrada == '^[[B':
            
        #Chama a função recursivamente pedindo pra exibir mais 10 xml
        quant_xml_exibidos += 10
        retorno = escolher_xml_diretorio(lista_xml, quant_xml_exibidos)

    elif entrada == 't' or entrada == 'T':

        #Código para todos
        return 't'

    else:
        erro = False

        #Verificar se não digitar um número
        for letra in entrada:
            if ord(letra) < ord('0') or ord(letra) > ord('9'):
                erro = True

        if erro == True:
            input('\nComando inválido')
            retorno = escolher_xml_diretorio(end_dir_predef, quant_xml_exibidos)
        
        #Verificar se o número corresponde a um xml
        elif int(entrada) <= len(lista_xml):
            retorno = end_dir_predef + lista_xml[int(entrada)-1]
    
        else:
            input('\nNão há um XML na lista com esse número')
            retorno = escolher_xml_diretorio(end_dir_predef)

    return retorno


def exibir_produtos_BACKUP(info_xml, margem):
    info_xml = info_xml[:-1]
    
    for produto in info_xml:
        print(produto['Nome'])
        print('\tCódigo: ', produto['Código'])
        print('\tQuantidade: ', produto['Quantidade'])
        print('\tValor total: ', produto['Total'])
        print('\tValor ICMS ST: ', produto['ICMS ST'])
        print('\tValor IPI: ', produto['IPI'])
        print('\tPreço unitário: ', produto['Valor unitário'])
        print('\tPreço de revenda: ', (margem + 1) * produto['Valor unitário'])
        print()

def exibir_produtos(info_xml, margem, maximo=6):
    
    #Tira o dicionário da nota
    info_xml = info_xml[:-1]
    
    n = min(len(info_xml),maximo)

    #Mostra os produtos na tela
    for produto in range(maximo-6, n):

        #Falta formatação

        print(produto['Nome'])
        print('\tQuantidade: ', produto['Quantidade'])
        print('\tPreço unitário: ', produto['Valor unitário'])
        print('\tPreço de revenda: ', (margem + 1) * produto['Valor unitário'])
        print()
    
    #Verifica se ja exibiu todos os produtos
    if n < len(info_xml):
        print('\nPressione seta para baixo (ou \'m\') para exibir mais\n')

    print('Deseja salvar os dados no sistema?')
    print('Y/N:')

    entrada = input()

    #Tratamento de erro
    if entrada == 'm' or entrada == 'M' or entrada == '^[[B':
        maximo += 6
        exibir_info(endereco, maximo, margem)

    elif entrada == 'y' or entrada == 'Y':
        
        #FALTANDO

    elif entrada == 'n' or entrada == 'N':
        return

    else:
        input('Opção inválida')
        exibir_info(endereco, maximo, margem)

#Tela 1.2A e 1.2B
def exibir_info (endereco, maximo=6, margem=0):
    
    #Limpa a tela
    os.system('clear' or 'cls')
    
    #Lê as configurações da margem de lucro armazenadas em disco
    arq_margem = open('Margem.txt', 'r')
    margem_on_off = arq_margem.readlines()[0]
    
    #Cabeçalho
    print('************************** LEITURA DO XML E CÁLCULO DE REVENDA *************************')
    
    #Verifica se o usuário decidiu processar um xml
    if endereco != 't':
        info_xml = parser(endereco)
        info_nota = info_xml[-1]
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
            margem = arq_margem.readlines()[1]
        
        #Se estiver habilitada e for a primeira vez rodando o programa
        elif margem_on_off == 'Habilitar\n' and maximo == 6:
            print('\nDigite a margem de lucro desejada: ')
            
            #FALTANDO
        
        #Vai exibir a margem de lucro que o usuário digitou anteriormente
        else:
            print('Digite a margem de lucro desejada:', margem)

        exibir_produtos(info_xml, margem, maximo)

    else:
        if margem_on_off == 'Desabilitar\n':
            print('*Configurações padrões aplicadas*')
            margem = arq_margem.readlines()[1]
        elif margem_on_off == 'Habilitar\n' and maximo == 6:
            print('Digite a margem de lucro desejada: ')
            #FALTANDO
        else:
            print('Digite a margem de lucro desejada:', margem)
        
        arq_dir_predef = open('Diretório.txt', 'r')
        end_dir_predef = arq_dir_predef.readlines()[1]
        
        lista_xml = varre_xml(end_dir_predef)
        
        #Cada linha dessa matriz é um XML (todos os produtos de um xml)
        #Cada coluna são os produtos (dicionários) que estão no xml
        matriz_xml = []
    
        for arquivo in lista_xml:
            matriz_xml.append(parser(end_dir_predef + arquivo))
        
        listona = []

        for xml in matriz_xml:
            exibir_produtos(xml, margem, maximo)

#Função principal (chamada feita pela main)
def revenda():

    #Verifica as configurações de diretório predefinido armazenadas em disco
    arq_dir_predef = open('Diretório.txt', 'r')
    config_dir_predef = arq_dir_predef.readlines()[0]

    #Verificar se o diretório predefinido está desabilitado
    if config_dir_predef == 'Habilitar':
        end_dir_predef = arq_dir_predef.readlines()[1]
        arq_dir_predef.close()
        endereco = escolher_xml_endereco()
    else:
        endereco = escolher_xml_diretorio(end_dir_predef)

    exibir_info(endereco)

revenda()
