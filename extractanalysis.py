import pandas as pd
import matplotlib.pyplot as plt


#Abrindo arquivo csv e corrigindo

conta_fatura = pd.read_csv(r'', sep = ',')
conta_fatura = conta_fatura.drop('', axis=1)


#Selecionando a célula e valor esperados

def get():
    
    x = len(conta_fatura.index)
    z = 0
    valor = 0
    valor_total = []
    
    while (z < x):
        
        conta1 = conta_fatura.at[z,''].split()[1]
        
        if (conta1 == ''):
            valor = conta_fatura.at[z,'']
            valor_total.append(valor)
            z = z + 1
        else:
            z = z + 1
    
    total = sum(valor_total)
    
    return total



#Plot do fluxo de entrada e saída

conta_fatura.plot()