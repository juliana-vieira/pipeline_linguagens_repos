from processamento import DadosRepositorios

company_list = ['juliana-vieira']

for company in company_list:

    dados = DadosRepositorios(company) # Extract
    dados.to_dataframe() # Transform
    dados.save_csv() # Load



