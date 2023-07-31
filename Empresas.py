from tabulate import tabulate
import pandas as pd

data_empresas = {

    'Empresa': ['Canadian Solar', 'First Solar', 'GCL-Si LONGi Solar', 'Ja Solar', 'Jinko Solar', 'Renesola', 'Risen Energy', 'Trina Solar'],
    'Ano': ['2001', '1999', '1996','2005', '2006', '2005', '1986', '1997'],
    'Localização' : ['São Paulo', 'São Paulo', 'Fora do Brasil', 'São Paulo', 'São Paulo', 'São Paulo', 'São Paulo','São Paulo'],
    'Parcerias' : ['SI', '3', 'SI', 'SI', 'SI','SI', 'SI', 'SI'],
    'Premios' : ['Fabricante n° 1 (BNEF 2020) +3 premios', 'Tier 1', 'SI', 'SI', 'n°1 2016-2019 (global modulo shipment)', 'Tier 1 (bloomberg)', '5 Prêmios 2017-2020','SI'],
    'Energia por ano' : ['150 GWh', '30GW', 'SI', '103 GW', '130 GW', '25GW', '30GW','80GW'],
    'Casas alimentadas' : ['172.000', 'SI', 'SI', '33.000', 'SI', 'SI','10.000','SI'],
    'CO2 evitado' : ['900.000 ton', 'SI', 'SI', 'SI', 'SI','SI', 'SI','SI'],
    'N° módulos' : ['3', '9', '12','11', '4', '10', '11','13'],
    'Usina/Parque' : ['Sim', 'Sim', 'Sim','Sim', 'Não', 'Sim', 'Não','Não']
}

df = pd.DataFrame(data_empresas)


print(tabulate(data_empresas, headers="keys", tablefmt= "fancy_grid"))
