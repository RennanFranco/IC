from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
#apenas os melhores paineis de cada empresa (com maior eficiencia)
data_paineis = { 

    'Empresa': ['Canadian Solar', 'First Solar', 'GCL-Si LONGi Solar', 'Ja Solar', 'Jinko Solar', 'Renesola', 'Risen Energy', 'Trina Solar' ],
    'Painel': ['BiHiKu7', 'Series 6 Plus', 'GCL-M8/60H', 'DeepBlue 3.0 Series', 'Tiger Neo', 'RS6-NBG-E3', 'TITAN 40', 'Vertex N'],
    'Potencia': ['635~655W', '455~480W', '365~400W', '600W', '635W', '560~580W', '395~420W', '565~585W'],
    'Eficiencia': ['21.6%', '19.0%', '22%', '23.7%', '23.23%', '22.45%', '21.8%', '22.0%' ],
    'Half/FullCell': ['Half', 'Half', 'SI', 'Half', 'Half', 'Half', 'Half', 'Half' ],
    'Mono/Bifacial': ['Bifacial', 'SI', 'Mono', 'SI', 'Bifacial', 'Bifacial', 'Mono', 'Bi'],
    'Mono/Policristalino': ['Mono', 'SI', 'Mono', 'SI', 'SI', 'Mono', 'Mono', 'SI'],
    'Fita circular': ['Não', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Não' ],
    'Area': ['3m²', '2.52m²', '1.8m²', 'SI', 'SI', '2.58m²', '1.92m²', 'SI'],
    'PERC': ['Sim', 'Não', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Não' ],
    'Filme fino': ['Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim' ],
    'Celulas duplas': ['Sim', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não' ] 

}

df = pd.DataFrame(data_paineis)
print(tabulate(data_paineis, headers ="keys", tablefmt = "fancy_grid"))

df_sorted = df.sort_values(by='Eficiencia', ascending=True)  

x = df_sorted['Empresa']
y = df_sorted['Eficiencia']

plt.figure(figsize=(8, 6))  
plt.bar (x, y, width= 0.3)
#plt.ylim([0, 25])
plt.ylabel('Eficiência')
plt.title('Eficiência dos melhores painéis solares por empresa')
plt.xticks(rotation=45)  
plt.show()
