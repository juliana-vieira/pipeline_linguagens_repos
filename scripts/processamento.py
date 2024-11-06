import requests 
import pandas as pd

class ClienteAPI:

    def __init__(self):
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'Authorization' : 'Bearer ' + self.access_token, 
                            'X-Github-Api-Version': '2022-11-28'}

class DadosRepositorios(ClienteAPI):

    def __init__(self, owner):
        super().__init__()
        self.owner = owner
        self.data = self.__read_repos()
        self.repo_names =  self.__get_repo_names()
        self.repos_languages = self.__get_repo_languages()
        self.dataframe = self.to_dataframe()

    def __read_repos(self):

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
    
    def __get_repo_names(self):
        
        repos_names = []

        for page in self.data:
            for repo in page:
                try:
                    repos_names.append(repo['name'])
                except:
                    pass

        return repos_names

    def __get_repo_languages(self):

        languages_list = []

        for page in self.data:
            for repo in page:
                try:
                    languages_list.append(repo['language'])
                except:
                    pass

        return languages_list
    
    def to_dataframe(self):

        try:
            df = pd.DataFrame()
            df['repository_name'] = self.repo_names
            df['language'] = self.repos_languages
             
            return df

        except Exception as e:
            print(e)

    def load(self):

        try:
            self.dataframe.to_csv(f'data/{self.owner}.csv')

        except Exception as e:
            print(e)
        




        

