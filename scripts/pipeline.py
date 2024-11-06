from processamento import DadosRepositorios

# Extract
company_list = ['amzn', 'Netflix', 'spotify', 'apple']

for company in company_list:

    dados = DadosRepositorios(company)
    dados.to_dataframe()
    dados.load()



