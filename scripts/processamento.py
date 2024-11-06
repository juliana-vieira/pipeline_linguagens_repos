import requests # Biblioteca utilizada pra consumir a API do Github
import pandas as pd # Biblioteca utilizada para a transformação dos dados
from dotenv import load_dotenv # Biblioteca utilizada para carregar variáveis de ambiente
import os # Biblioteca utilizada para carregar variáveis de ambiente

load_dotenv() # Método necessário para carregar variáveis de ambiente

# Classe necessária para acessar a API do Github
class ClienteAPI:

    def __init__(self):
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv("GITHUB_TOKEN")
        self.headers = {'Authorization' : 'Bearer ' + self.access_token, 
                            'X-Github-Api-Version': '2022-11-28'}

# Classe que executa a leitura, transformação e carregamento dos dados herdando a classe com os dados de acesso à API
class DadosRepositorios(ClienteAPI):

    def __init__(self, owner):
        super().__init__()
        self.owner = owner # Nome da empresa
        self.data = self.__read_repos() # Dados dos repositórios da empresa em json, obtidos pelo método de extração de dados read_repos()
        self.repos_names =  self.__get_repos_names() # Lista de nomes dos repositórios da empresa, obtida pelo método de extração dos nomes dos repositórios get_repos_names()
        self.repos_languages = self.__get_repo_languages() # Lista de linguagens dos repositórios da empresa, obtida pelo método de extração das linguagens dos repositórios get_repo_languages()
        self.dataframe = self.to_dataframe() # Dataframe com nome dos repositórios e linguagem dos respectivos repositórios, obtido pelo método de transformação to_dataframe()

    def __read_repos(self):

        # Método que percorre todas as páginas de repositórios da empresa especificada em "owner", armazena em uma lista e a retorna
        # O laço é interrompido quando o json recebido tem o tamanho 0, ou quando um erro é encontrado

        repos_list = []
        page = 1

        while True:
            try:
                url_page = f"{self.api_base_url}/users/{self.owner}/repos?page={page}"
                response = requests.get(url_page, headers = self.headers)
                repos = response.json()

                if len(repos) == 0:
                    break

                repos_list.append(repos)
                page += 1

            except Exception as e:
                print(e)
                break
        
        return repos_list
    
    def __get_repos_names(self):

        # Método que percorre todas as páginas de repositórios da lista de repositórios armazenada em self.data e cria uma lista de nomes dos repositórios, armazenando esses nomes nessa lista
        # Estrutura de self.data: Lista [Páginas Sublista [Repositórios Dict {Características dos repositórios}]]
        # O método retorna essa lista, que é armazenada no atributo da classe self.repos_names

        repos_names = []

        for page in self.data:
            for repo in page:
                try:
                    repos_names.append(repo['name'])
                except Exception as e:
                    print(e)

        return repos_names

    def __get_repo_languages(self):
        # Método que percorre todas as páginas de repositórios da lista de repositórios armazenada em self.data e cria uma lista de linguagens usadas nos repositórios, armazenando essas linguagens nessa lista
        # Estrutura de self.data: Lista [Páginas Sublista [Repositórios Dict {Características dos repositórios}]]
        # O método retorna essa lista, que é armazenada no atributo da classe self.repos_languages
        # Caso haja um erro, o erro será printado no console

        languages_list = []

        for page in self.data:
            for repo in page:
                try:
                    languages_list.append(repo['language'])
                except Exception as e:
                    print(e)

        return languages_list
    
    def to_dataframe(self):

        # Método que cria um DataFrame pandas e armazena os nomes dos repositórios e as linguagens desses repositórios nas colunas "repository_name" e "language"
        # O método retorna esse dataframe, que é armazenado no atributo da classe self.dataframe 
        # Caso haja um erro, o erro será printado no console

        try:
            df = pd.DataFrame()
            df['repository_name'] = self.repos_names
            df['language'] = self.repos_languages
             
            return df

        except Exception as e:
            print(e)

    def save_csv(self):

        # Método que salva o dataframe gerado em um arquivo csv na pasta "data"
        # Caso haja um erro, o erro será printado no console

        try:
            self.dataframe.to_csv(f'data/{self.owner}.csv')

        except Exception as e:
            print(e)
        




        

