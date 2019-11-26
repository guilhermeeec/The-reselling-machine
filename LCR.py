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

def escolher_xml (config_dir_predef=False, lista_xml=[], quant_xml_exibidos=10):
    os.system('clear')

    #Caso não tenha diretório pré-definido (Tela 1.1B)
    if config_dir_predef == False:
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
            retorno = escolher_xml()
        
        #Verifica se o arquivo tem extensão .xml
        elif Path(endereco).suffix != '.xml':
            print('\nArquivo não possui extensão .xml')
            input()
            retorno = escolher_xml()
        
        #Endereço existe e tem extensão .xml
        else:
            print('\nEndereço encontrado')
            input()
            return endereco

        return retorno
    
    #Caso tenha diretório pré-definido (Tela 1.1A)
    else:

        #Listagem de xml para o usuário
        print('Lista de XML no diretório predefinido')

        #Calcula a quantidade de arquivos xml a ser exibidos (n)
        n = min(len(lista_xml),quant_xml_exibidos)
        
        #Lista de números
        numeros = []

        #Lista n arquivos xml
        numero = 0
        for item in range(n):
            numero += 1
            numeros.append(numero)
            print('\t')
            print(numero, end=' - ')
            print(lista_xml[item])
        
        #Pede pro usuário apertar seta pra baixo ou m patra exibir mais xml caso existam
        if n < len(lista_xml):
            print('\nPressione seta para baixo (ou \'m\') para exibir mais')
            
        print('\n(digite \'v\' para voltar)\n')
        print('Selecione o XML (ou digite \'T\' para todos: ')
        
        entrada = input()

        if entrada == 'v' or entrada == 'V':

            #Código de voltar
            return -1

        #'^[[B' = seta para baixo
        elif entrada == 'm' or entrada == 'M' or entrada == '^[[B':
            
            #Chama a função recursivamente pedindo pra exibir mais 10 xml
            quant_xml_exibidos += 10
            retorno = escolher_xml(True, lista_xml, quant_xml_exibidos)

        elif entrada == 't' or entrada == 'T':

            #Código para todos
            return 't'

        return retorno

  
print(escolher_xml())
