# Pipeline de extração de linguagens de programação de repositórios Github

Esse projeto implementa um pipeline de dados em Python, usando Programação Orientada a Objetos (POO), para extrair dados das principais linguagens de programação utilizadas por grandes empresas. Entre as empresas analisadas, estão Amazon, Spotify, Netflix, Discord, entre outras. O pipeline foi desenvolvido para extrair dados diretamente dos perfis dessas empresas no GitHub, mas é um pipeline flexível que pode ser utilizado para extrair dados de qualquer perfil.

Projeto desenvolvido durante a formação de Engenharia de Dados da Alura, com pequenas modificações para otimizar a automação do processo de ETL.

## Tabela de Conteúdos
- [Características](#características)
- [Requisitos](#requisitos)
- [Configuração e Uso](#configuração-e-uso)
- [Exemplo de Uso](#exemplo-de-uso)

## Características

- Extrai dados sobre as linguagens de programação mais usadas em cada repositório público de perfis do GitHub.
- Flexível e extensível: basta informar o nome de usuário do GitHub para extrair dados de qualquer perfil.
- Estrutura modular baseada em POO, permitindo fácil expansão e manutenção.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `pandas`
  - `python-dotenv` e `os` (opcional, para gerenciamento seguro de tokens de acesso)

## Configuração e Uso

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/juliana-vieira/pipeline_linguagens_repos.git
   cd pipeline_linguagens_repos

2. **Configuração do Token de Acesso**:
   Para evitar limitações de taxa ao acessar a API do GitHub, é recomendável configurar um token de acesso pessoal.

   - Crie um token de acesso no GitHub.
   - Armazene o token em uma variável de ambiente chamada `GITHUB_TOKEN` ou em um arquivo `.env`:
     ```plaintext
     GITHUB_TOKEN=seu_token_aqui
     ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt

## Exemplo de Uso

Para extrair dados das linguagens de programação utilizadas por empresas, defina a lista `company_list` com os nomes de usuário desejados:

```python
from processamento import DadosRepositorios

# Lista de empresas (ou qualquer usuário GitHub) a serem analisadas
company_list = ["amzn", "netflix", "spotify", "discord"]

for company in company_list:

    dados = DadosRepositorios(company) # Cria um objeto da classe DadosRepositorios, que possui os métodos de extração de dados consumindo a API do Github
    dados.to_dataframe() # Transforma os dados para um DataFrame pandas
    dados.save_csv() # Salva o arquivo em CSV na pasta "data"
```

O código acima irá criar um arquivo CSV para cada perfil listado em `company_list`, contendo os dados das principais linguagens de programação utilizadas por cada empresa, e salvar esses arquivos na pasta "data".

A clase DadosRepositorios possui todos os métodos necessários para extrair os dados, transformá-los e salvá-los dentro do contexto do negócio.

🎉 **Obrigada por conferir este projeto!** 😊
