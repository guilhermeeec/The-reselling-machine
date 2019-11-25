
####### CONFIGURAÇÕES ########

from os import system

def margem_lucro (on_off = "Habilitar", margem = None):     
    ''' Recebe o estado atual das configurações (se atualmente está 
        habilitado ou desabilitado, e a margem atual).
        Na primeira vez ficará habilitado, e margem = None, porém, 
        talvez possa mudar essa forma como foi feita qnd descobrirmos
        como salvar em disco 
    '''
    
    system("clear")                                                    
    print("******************* CONFIGURAÇÕES ********************")     
    print("                   MARGEM DE LUCRO\n")                      
    print("*aperte 'v' para voltar*")                                  
    print("")
    print("1 -", on_off, "margem de lucro predefinida") 
    print("2 - Definir margem de lucro")
    
    opcao = input("Opção: ")
    
    
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
            print("Você tem que inserir uma margem de lucro primeiro")
            input()
            opcao = "2"              
        else:
            return (on_off, margem)
    else:
        if(opcao != "2"):                   
            print("Opção inválida")
            input()
            on_off_e_margem = margem_lucro(on_off,margem)
            return on_off_e_margem

    if (opcao == "2"):
        tem_simbolo = True
        while (tem_simbolo == True):
            if (margem == None):
                print("\nMargem de Lucro atual: " + "Não foi inserida")
            else:
                print("\nMargem de Lucro atual:", margem*100 + "%")
                
            anterior = margem
            margem = input("Margem de lucro desejada (em %): ")
        
            if (margem != "v"):
                if (margem[-1] == "%"):
                    margem = margem[:-1]
                tem_simbolo = False
                pontos = 0
                for caract in range(len(margem)):
                    if (ord(margem[caract]) >= ord("a")):
                        tem_simbolo = True
                    elif (ord(margem[caract]) < ord("0") and ord(margem[caract]) != ord(".")):
                        tem_simbolo = True
                    if (ord(margem[caract]) == ord(".")):
                        pontos += 1
                    if (pontos == 2):
                        tem_simbolo = True
                        

                if (tem_simbolo == False):
                    margem = float(margem)/100   ## Margem de lucro na forma de decimal pronto para ser usado
                    print("\n*Alterações aplicadas*")
                else:
                    print("\nInválido. Insira somente números e '.' para decimal")
                    margem = anterior
            else:
                return (on_off,anterior)
                
        return (on_off,margem)  #Retorna uma tupla 


    return (on_off_e_margem) #retorna a tupla do if opcao == 1


            
tupla = margem_lucro()
print("Tupla:", tupla)




        
        

    

