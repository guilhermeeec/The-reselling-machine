########## LEITURA DO XML E CÁLCULO DE REVENDA ##########

import os
#from Parser import parser 
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
    os.system('clear' or 'cls')
    print('(digite \'v\' para voltar)\n')
    print('Digite o endereço do arquivo XML: ')
    entrada = input()

    if entrada == 'v' or entrada == 'V':
            
        #Código de voltar
        return -1

    else:
        endereco = entrada

    #Verifica se o caminho existe
    if os.path.exists (endereco) == False:
        print('\nEndereço não encontrado')
        input()
        retorno = escolher_xml_endereco()
        
    #Verifica se o arquivo tem extensão .xml
    elif Path(endereco).suffix != '.xml':
        print('\nArquivo não possui extensão .xml')
        input()
        retorno = escolher_xml_endereco()
        
    #Endereço existe e tem extensão .xml
    else:
        print('\nEndereço encontrado')
        input()
        return endereco

    return retorno
    
#Tela 1.1A
def escolher_xml_diretorio (end_dir_predef, quant_xml_exibidos=10):
    
    os.system('clear' or 'cls')

    lista_xml = varre_xml(end_dir_predef)

    #Listagem de xml para o usuário
    print('Lista de XML no diretório predefinido')

    #Calcula a quantidade de arquivos xml a ser exibidos (n)
    n = min(len(lista_xml),quant_xml_exibidos)

    #Lista n arquivos xml
    numero = 0
    for item in range(n):
        numero += 1
        print(numero, end=' - ')
        print(lista_xml[item])
        
    #Pede pro usuário apertar seta pra baixo ou m patra exibir mais xml caso existam
    if n < len(lista_xml):
        print('\nPressione seta para baixo (ou \'m\') para exibir mais')
            
    print('\n(digite \'v\' para voltar)\n')
    print('Selecione o XML (ou digite \'T\' para todos): ')
        
    entrada = input()

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
        for letra in entrada:
            if ord(letra) < ord('0') or ord(letra) > ord('9'):
                erro = True

        if erro == True:
            print('\nComando inválido')
            input()
            retorno = escolher_xml_diretorio(end_dir_predef)

        elif int(entrada) <= numero:
            retorno = end_dir_predef + lista_xml[int(entrada)-1]

        else:
            print('\nNão há um XML na lista com esse número')
            input()
            retorno = escolher_xml_diretorio(end_dir_predef)

    return retorno

def revenda():

    end_dir_predef = '/home/guiat/comp1/The-reselling-machine/'
    config_dir_predef = 'Desabilitar'
    
    #Verificar se o diretório predefinido está desabilitado
    if config_dir_predef == 'Habilitar':
        endereco = escolher_xml_endereco()
    else:
        endereco = escolher_xml_diretorio(end_dir_predef)
    print(endereco)

revenda()

