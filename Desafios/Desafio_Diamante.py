"""
1. Análise de dados de preços de diamantes

Os diamantes são divididos em cinco tipos de impurezas com base na estrutura de seus átomos de carbono. 
O conjunto de dados de diamantes da Kaggle fornece ainda mais informações - corte, clareza, cor e preço. 
Desenvolva suas habilidades de visualização de dados com algumas análises exploratórias de dados.

Preço médio por tipo de corte

Pergunta: diamantes com corte "Ideal" realmente são mais caros do que os com corte "Fair"?

Influência da cor no preço

Pergunta: qual a diferença média de preço entre diamantes de cor D (melhor) e J (pior)?

Clareza vs. Preço

Pergunta: diamantes mais claros (IF, VVS1) têm um preço significativamente maior que os menos claros (I1, SI2)?

Distribuição do preço total

Pergunta: a maioria dos diamantes custa abaixo de quanto? (histograma).

Correlação entre carat (peso) e preço

Pergunta: quanto mais pesado o diamante, maior o preço? É linear ou exponencial?

Boxplot de preços por corte

Pergunta: existe muita variação de preço dentro da mesma categoria de corte?

Análise conjunta

Pergunta: se compararmos corte, cor e clareza juntos, qual combinação aparece como a mais cara?

Tendência de mercado

Pergunta: se um comprador tiver um orçamento limitado (ex.: $3000), qual a melhor relação custo-benefício (melhor corte, cor e clareza possíveis dentro desse limite)?

"""

import pandas as pd
import tkinter as tk
from tksheet import Sheet

def searchHead():
    df = pd.read_csv('diamonds.csv')
    list_parameters = []
    for row in df.head():
        list_parameters.append(row)
    list_parameters.remove('Unnamed: 0')
    print(list_parameters)
    ####

df = pd.read_csv('diamonds.csv')

def searchCommons(X=True):
    while X:
        I = 0
        list_cuts = []
        
        for index, row in df.iterrows():
            list_cuts.append(row['cut']) if row['cut'] not in list_cuts else None
        X = False
    return list_cuts

def calculateMedia():
    lista_cortes = searchCommons()
    list_values = []
    list_medias = []
    b = 0
    w = 0
    count_0=0
    count_1=0
    count_2=0
    count_3=0
    count_4=0
    media_corte0 = 0
    media_corte1 = 0
    media_corte2 = 0
    media_corte3 = 0
    media_corte4 = 0
    for index, row in df.iterrows():
        list_values.append([row['cut'],row['price']]) if row['price'] not in list_values else None
        match list_values:
            case _ if row['cut'] == lista_cortes[0]:
                count_0 +=1 
                media_corte0 += row['price']
            case _ if row['cut'] == lista_cortes[1]:
                count_1 +=1 
                media_corte1 += row['price']
            case _ if row['cut'] == lista_cortes[2]:
                count_2 +=1 
                media_corte2 += row['price']
            case _ if row['cut'] == lista_cortes[3]:
                count_3 +=1 
                media_corte3 += row['price']
            case _ if row['cut'] == lista_cortes[4]:
                count_4 +=1 
                media_corte4 += row['price']
            case _:
                ...
                
    data = [[lista_cortes[0],round(media_corte0/count_0)],
            [lista_cortes[1],round(media_corte1/count_1)],
            [lista_cortes[2],round(media_corte2/count_2)],
            [lista_cortes[3],round(media_corte3/count_3)],
            [lista_cortes[4],round(media_corte4/count_4)],
            ]
    return data


def plotData(): 
    root = tk.Tk()
    root.title("Diamantes")
    root.geometry("500x300")
    sheet = Sheet(
        root,
        data=calculateMedia(),
        headers=['Corte','Media de Preço'],
        width=480,
        height=280,
        column_width=240,
            )
    sheet.pack(expand=True,fill='both')
    root.mainloop()
    
plotData()