
####### CONFIGURAÇÕES ########

from os import system

def margem_lucro (on_off = "Habilitar", margem = None):
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
    
    elif (opcao == "v"):
        if (margem == None and on_off == "Desabilitar"):     #Provavelmente tá errado
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
        if (margem == None):
            print("Margem de Lucro atual: " + "Não foi inserida")
        else:
            print("Margem de Lucro atual:", margem*100 + "%")
        
        margem = input("Margem de lucro desejada (em %): ")
        if (margem != "v"):
            if (margem[-1] == "%"):
                margem = margem[:-1]
            margem = float(margem)/100   ## Margem de lucro na forma de decimal pronto para ser usado
            print("*Alterações aplicadas*")
            return (on_off,margem)  #Retorna uma tupla 
        else:
            return (on_off,margem)


    return (on_off_e_margem)


            
tupla = margem_lucro()
print("Tupla:", tupla)




        
        

    

