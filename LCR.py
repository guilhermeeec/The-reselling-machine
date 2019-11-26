########## LEITURA DO XML E CÁLCULO DE REVENDA ##########

import os
from Parser import parser 
from pathlib import Path

def escolher_xml (config_dir_predef=False, end_dir_predef=None):
    os.system('clear')

    #Caso não tenha diretório pré-definido
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
    
    #Caso tenha diretório pré-definido
    else:
        
        #Cria uma lista vazia com os arquivos xml do diretório pré-definido
        lista_xml = []

        #Lista os arquivos do diretório pré-definido e os varre
        quant_de_xml = 0
        for arquivo in os.listdir (end_dir_predef):

            #Verifica quais arquivos são xml para listá-los
            if Path(arquivo).suffix == '.xml':
                lista_xml.append(arquivo)
                quant_de_xml += 1

        #Só libera a próxima tela se não houver nenhum erro
        erro = False
        limite = 20

        #Listagem de xml para o usuário
        print('Lista de XML no diretório predefinido\n')

        #10 arquivos ou menos
        numero = 0
        if quant_de_xml <= 10:
            for item in lista_xml:
                numero += 1
                print(numero, end=' - ')
                print(item)
        
        #Mais de 10 arquivos
        else:
            for indice in range(10):
                numero += 1
                print(numero, end=' - ')
                print(lista_xml[indice])
            print('\nPressione \'m\' para exibir mais')
            
        print('\n(digite \'v\' para voltar)\n')
        print('Selecione o XML (ou digite \'T\' para todos: ')
        opcao = input()

print(escolher_xml())
