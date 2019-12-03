
####### CONFIGURAÇÕES ########

import os
import platform

#   1 - Margem de lucro


def margem_lucro (on_off = "Habilitar", margem = None, erro_margem = False):     
    ''' Recebe o estado atual das configurações (se atualmente está 
        habilitado ou desabilitado, e a margem atual).
        Na primeira vez ficará habilitado, e margem = None, porém, 
        talvez possa mudar essa forma como foi feita qnd descobrirmos
        como salvar em disco 
    '''
                                                    
    #Limpa a tela
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        print('Sistema operacional não aceito')
        return

    print("******************* CONFIGURAÇÕES ********************")     
    print("                   MARGEM DE LUCRO\n")                      
    print("*aperte 'v' para voltar*")                                  
    print("\n"*2)
    print("1 -", on_off, "margem de lucro predefinida") 
    print("2 - Definir margem de lucro")
    
    if (erro_margem == False):
        opcao = input("Opção: ")
    else:
        opcao = "2"
    
    if (opcao == "1"):
        if (on_off == "Habilitar"):
            on_off = "Desabilitar"
        else:
            on_off = "Habilitar" 
        
        on_off_e_margem = margem_lucro(on_off,margem) # Vai receber uma tupla  
        ''' Vai chamar a mesma função de novo, botando como parâmetro o estado atual. Deve-se guardar o valor de retorno, 
            visto que se for mudado algum outro parâmetro na próxima funçao, essa primeira função deve saber o que mudou, 
            para retornar ao programa principal. Se for apertado o '1' várias vezes vai ser criado várias funções recursivamente.
        '''
    
    elif (opcao == "v"):
        if (margem == None and on_off == "Desabilitar"):     #Na primeira vez, habilitou e apertou 'v', sem definir uma margem
            input("\nMargem habilitada mas nada inserido. Insira uma margem ou desabilite a opção")
            on_off_e_margem = margem_lucro(on_off, margem)              

        else:
            return (on_off, margem)

    elif (opcao == "2"):
        erro_margem = True
        
        if (margem == None):
            print("\nMargem de Lucro atual: " + "Não foi inserida")
        else:
            print("\nMargem de Lucro atual: ", margem*100 , "%" ,sep = "")
                
        anterior = margem
        margem = input("Margem de lucro desejada (em %): ")
    
        if (margem != "v" and margem != "V" and margem != ""):
            if (margem[-1] == "%"):
                margem = margem[:-1]
            
            #----Tratamento de erro para o que for digitado: 
            erro_margem = False
            pontos = 0
            for caract in range(len(margem)):
                if (ord(margem[caract]) >= ord("a")):
                    erro_margem = True
                elif (ord(margem[caract]) < ord("0") and ord(margem[caract]) != ord(".")):
                    erro_margem = True
                
                if (ord(margem[caract]) == ord(".")):
                    pontos += 1
                    if (pontos == len(margem)):  #Se a pessoa digitar apenas um ponto
                        erro_margem = True
                if (pontos == 2):
                    erro_margem = True
            #----
            
            if (erro_margem == False):
                margem = float(margem)/100   ## Margem de lucro na forma de decimal pronto para ser usado
                input("\n*Alterações aplicadas*")
                on_off_e_margem = (on_off, margem, erro_margem)
            else:
                input("\nInválido. Insira somente números e '.' para decimal")
                
                margem = anterior
                on_off_e_margem = margem_lucro(on_off,margem,erro_margem)
        elif ((anterior == None and on_off == "Desabilitar")):
            input("\nMargem habilitada mas nada inserido. Insira uma margem ou desabilite a opção")
            on_off_e_margem = margem_lucro(on_off, anterior)                      
        elif (margem == ""):
            input("\nInválido. Insira somente números e '.' para decimal")
            on_off_e_margem = margem_lucro(on_off, anterior)                      
            
        else:    
            return (on_off,anterior) 

    else:            
        input("\nOpção inválida")
        
        on_off_e_margem = margem_lucro(on_off,margem)


    return on_off_e_margem 





#   2 - Diretório 




def diretorio (on_off = "Habilitar", endereco = None, erro_dir = False ):
                                                    
    #Limpa a tela
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        print('Sistema operacional não aceito')
        return
    
    print("******************* CONFIGURAÇÕES **********************")     
    print("                      DIRETÓRIO\n")                      
    print("*aperte 'v' para voltar*")                                  
    print("\n"*2)
    print("1 -", on_off, "diretório predefinido") 
    print("2 - Definir diretório")
    print("\n"*2)
    
    if (erro_dir == False):
        opcao = input("Opção: ")
    
    else:
        opcao = "2"
    
    if (opcao == "1"):
        if (on_off == "Habilitar"):
            on_off = "Desabilitar"
        else:
            on_off = "Habilitar" 
        
        on_off_e_endereco = diretorio(on_off, endereco)   
    
    elif (opcao == "v"):
        if (endereco == None and on_off == "Desabilitar"):     
            input("\nDiretório habilitado mas nada inserido. Insira um endereço ou desabilite a opção")
            on_off_e_endereco = diretorio(on_off, endereco)
        else:
            return (on_off, endereco)

    elif (opcao == "2"):
        
        if (endereco == None):
            print("\nDiretório selecionado: " + "Não foi inserido")
        else:
            print("\nDiretório selecionado:", endereco)
                
        anterior = endereco
        print("Digite o endereço do diretório desejado. " + "Ex: C:\Apps\SupportAssist ou /home/joaquim\n") #Windows ou Linux
        endereco = input("Diretório: ")
        
        if (endereco != "v" and endereco != "V"):
            erro_dir = not(os.path.isdir(endereco))     #Verifica se a pasta existe
            
            if (erro_dir == False):
                input("\n*Alterações aplicadas*")
                
                return (on_off, endereco)
            
            else:
                input("\nDiretório inválido. Digite novamente")
                endereco = anterior
                on_off_e_endereco = diretorio(on_off,endereco,erro_dir)

        elif (anterior == None and on_off == "Desabilitar"):     
                input("\nDiretório habilitado mas nada inserido. Insira um endereço ou desabilite a opção")
                on_off_e_endereco = diretorio(on_off, anterior)
        else:    
            return (on_off,anterior)
                
    else:                   
        input("\nOpção inválida")
        on_off_e_endereco = diretorio(on_off, endereco)
         
    return on_off_e_endereco     


def ler_arq (arq):
    lista = arq.readlines()
    lista[0] = lista[0][:-1]
    return lista



def escrever_arq (arq, tupla):
    if (tupla != "\n"):
        lista = list(tupla)
        arq.write(lista[0] + "\n")
        arq.write(str(lista[1]))
    else:
        arq.write(lista[0] + "\n")


    
    
def config ():
    
    #Limpa a tela
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        print('Sistema operacional não aceito')
        return
    
    print("******************* CONFIGURAÇÕES *********************")                           
    print("")
    print("*aperte 'v' para voltar*")                                  
    print("\n"*2)
    print("1 - Margem de Lucro") 
    print("2 - Diretório")
    print("\n"*2)
    
    opcao = input("Opção: ")
    if (opcao == "1"):
        margem_txt = open("Margem.txt", "r")
        config_margem = ler_arq(margem_txt)
        margem_txt.close()
        if (config_margem[1] == "None" or config_margem[1] == "None\n"):
            config_margem = margem_lucro(config_margem[0])
        else:
            config_margem = margem_lucro(config_margem[0], float(config_margem[1]))
        
        margem_txt = open("Margem.txt","w")
        escrever_arq(margem_txt, config_margem)
        margem_txt.close()
        config()
    
    elif (opcao == "2"):
        diretorio_txt = open ("Diretorio.txt", "r")
        config_diretorio = ler_arq(diretorio_txt)
        diretorio_txt.close()
        if (config_diretorio[1] == "None" or config_diretorio[1] == "None\n"):
            config_diretorio = diretorio(config_diretorio[0])
        else:
            config_diretorio = diretorio(config_diretorio[0], config_diretorio[1])
        diretorio_txt = open("Diretorio.txt", "w")
        escrever_arq(diretorio_txt, config_diretorio)
        diretorio_txt.close()
        config()
    
    elif (opcao == "v"):
        return
    else: 
        input("\nOpção inválida")
        config()
    return

def main():
    config()

if __name__ == '__main__':
    main()
