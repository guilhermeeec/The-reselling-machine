
####### CONFIGURAÇÕES ########

import os

#   1 - Margem de lucro


def margem_lucro (on_off = "Habilitar", margem = None, erro_margem = False):     
    ''' Recebe o estado atual das configurações (se atualmente está 
        habilitado ou desabilitado, e a margem atual).
        Na primeira vez ficará habilitado, e margem = None, porém, 
        talvez possa mudar essa forma como foi feita qnd descobrirmos
        como salvar em disco 
    '''
    
    os.system("clear" or "cls")                                                    
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
            print("Você tem que inserir uma margem de lucro primeiro ou desabilitar a opção")
            input()
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
        
        if (margem != "v"):
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
                print("\n*Alterações aplicadas*")
                on_off_e_margem = (on_off, margem, erro_margem)
            else:
                print("\nInválido. Insira somente números e '.' para decimal")
                input()
                margem = anterior
                on_off_e_margem = margem_lucro(on_off,margem,erro_margem)
        else:
            if (anterior == None and on_off == "Desabilitar"):
                print("Você tem que inserir uma margem de lucro primeiro ou desabilitar a opção")
                input()
                on_off_e_margem = margem_lucro(on_off, anterior)                      
            return (on_off,anterior) 

    else:            
        print("Opção inválida")
        input()
        on_off_e_margem = margem_lucro(on_off,margem)


    return on_off_e_margem 





#   2 - Diretório 




def diretorio (on_off = "Habilitar", endereco = None, erro_dir = False ):
    
    os.system("clear" or "cls")                                                    
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
            print("Você tem que inserir o endereço do diretório primeiro ou desabilitar a opção")
            input()
            on_off_e_endereco = diretorio(on_off, endereco)
        else:
            return (on_off, endereco)

    elif (opcao == "2"):
        
        if (endereco == None):
            print("\nDiretório atual: " + "Não foi inserido")
        else:
            print("\nDiretório atual:", endereco)
                
        anterior = endereco
        print("Digite o endereço do diretório desejado. " + "Ex: C:\Apps\SupportAssist ou /home/joaquim\n") #Windows ou Linux
        endereco = input("Diretório: ")
        
        if (endereco != "v"):
            erro_dir = not(os.path.isdir(endereco))     #Verifica se a pasta existe
            
            if (erro_dir == False):
                print("\n*Alterações aplicadas*")
                input()
                return (on_off, endereco)
            
            else:
                print("\nDiretório inválido. Digite novamente")
                input()
                endereco = anterior
                on_off_e_endereco = diretorio(on_off,endereco,erro_dir)

        else:
            if (anterior == None and on_off == "Desabilitar"):     
                print("Você tem que inserir o endereço do diretório primeiro ou desabilitar a opcao")
                input()
                on_off_e_endereco = diretorio(on_off, anterior)
            else:
                return (on_off,anterior)
                
    else:                   
        print("Opção inválida")
        input()
        on_off_e_endereco = diretorio(on_off, endereco)
         
    return on_off_e_endereco     


def ler_arq (arq):
    lista = arq.readlines()
    input(lista)
    lista[0] = lista[0][:-1]
    
    
    return lista



def escrever_arq (arq, tupla):
    lista = list(tupla)
    input(lista)
    arq.write(lista[0] + "\n")
    arq.write(str(lista[1]))


    
    
def config ():
    os.system("clear" or "cls")
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
        config_margem = margem_lucro(config_margem[0], float(config_margem[1]))
        margem_txt.close()
        margem_txt = open("Margem.txt","w")
        escrever_arq(margem_txt, config_margem)
        margem_txt.close()
        config()
    
    elif (opcao == "2"):
        diretorio_txt = open ("Diretorio.txt", "r")
        config_diretorio = ler_arq(diretorio_txt)
        config_diretorio = diretorio(config_diretorio[0], config_diretorio[1])
        diretorio_txt.close()
        diretorio_txt = open("Diretorio.txt", "w")
        escrever_arq(diretorio_txt, config_diretorio)
        diretorio_txt.close()
        config()
    
    elif (opcao == "v"):
        return
    else: 
        print("Opção inválida")
        input()
        config()


config()



        
        

    

