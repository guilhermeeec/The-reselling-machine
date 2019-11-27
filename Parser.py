import xml.etree.ElementTree as ET

def parser (XML_file_name, debug=False):
    
    #Retorna uma árvore XML
    arvore = ET.parse(XML_file_name)

    '''
    Pega a raiz da árvore que é uma lista em que cada elemento da lista é um filho da árvore. 
    Cada filho da árvore é uma lista com seus filhos e assim por diante
    '''
    raiz = arvore.getroot()

    #Pega informações da nota e monta uma dicionário
    fornecedor = raiz[0][0][1][1].text
    data_emissao = raiz[0][0][0][6].text
    chave_acesso = raiz[1][0][2].text
    icms_st = raiz[0][0][13][0][5].text
    ipi = raiz[0][0][13][0][13].text
    outras_despesas = raiz[0][0][13][0][12].text
    valor_total = raiz[0][0][13][0][18].text
    
    nota_info = {
                'Fornecedor':fornecedor,
                'Data de emissão':data_emissao,
                'Chave de acesso': chave_acesso,
                'ICMS ST':icms_st,
                'IPI':ipi,
                'Outras despesas':outras_despesas,
                'Valor total':valor_total
                }
    
    if debug == True:
        print('Informações da nota: ')
        print(nota_info)

    #Listas vazias com informações dos produtos
    codigo_p = []
    nome_p = []
    quantidade_p = []
    valor_total_p = []
    icms_st_p = []
    ipi_p = []
    unitario_p = []

    #Pega informações dos produtos e preenche as listas
    quantidade_de_produtos = 0
    tem_icmsst = False
    for item in raiz[0][0]:
        if item.tag[36:40] == 'det':
            codigo_p.append(item[0][0].text)

            #O nome pode estar dividido em duas partes ou não
            if len(item) >= 3:
                nome_p.append(item[0][2].text + ' ' + item[2].text)
            else:
                nome_p.append(item[0][2].text)

            quantidade_p.append(item[0][13].text)
            valor_total_p.append(item[0][10].text)

            #Alguns produtos tem ICMS ST outros não
            for tipo_de_icms in item[1][1][0]:
                if tipo_de_icms.tag[36:42] == 'vICMSST':
                    icms_st_p.append(tipo_de_icms.text)
                    tem_icmsst = True
            if tem_icmsst == False:
                icms_st_p.append(0)

            ipi_p.append(item[1][2][1][3].text)
            unitario_p.append(item[0][9].text)
            
            quantidade_de_produtos += 1

    #Monta uma lista de dicionarios dos produtos
    produtos = []
    for indice in range (quantidade_de_produtos):
        produtos.append({'Código':0, 'Nome':' ', 'Quantidade':0, 'Total':0, 'ICMS ST':0, 'IPI':0, 'Valor unitário':0})
        
        produtos[indice]['Código'] = codigo_p[indice]
        produtos[indice]['Nome'] = nome_p[indice]
        produtos[indice]['Quantidade'] = quantidade_p[indice]
        produtos[indice]['Total'] = valor_total_p[indice]
        produtos[indice]['ICMS ST'] = icms_st_p[indice]
        produtos[indice]['IPI'] = ipi_p[indice]
        produtos[indice]['Unitário'] = unitario_p[indice]

    if debug == True:
        print('Dicionários dos produtos')
        for dicionario in produtos:
            print(dicionario, '\n')
    
    #Monta uma lista com todas as informações. O último elemento da lista é o dicionário com as informações da nota
    produtos.append(nota_info)

    return produtos
