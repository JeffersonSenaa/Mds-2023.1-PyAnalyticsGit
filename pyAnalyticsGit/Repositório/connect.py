import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_user = os.getenv("user_name")
api_name = os.getenv("repo_name")

class Connect:
    def __init__(self):
        pass
    

    def connect_issue(self):
        self.username = api_user
        self.reponame = api_name

        page = 1
        per_page = 30
        self.all_issues = []

        while True:           
            response = requests.get(f'https://api.github.com/repos/{self.username}/{self.reponame}/issues?state=all&page={page}&per_page={per_page}')

            if response.status_code == 200:
                self.issues = response.json()
                self.all_issues.extend(self.issues)
                #print("conexão estabelecida\n")

                if len(self.issues) < per_page:
                    break
                else:
                    page += 1
               

            else:
                print(f'Falha ao obter os detalhes do repositório {self.reponame}.')
                print(f'StatusCode: {response.status_code}')
                break

        return self.all_issues       

# connect = Connect()

# all_issues  = connect.connect_issue("fga-eps-mds","2023.1-PyAnalyticsGit")
# print(all_issues)