import requests
import pandas as pd
from bs4 import BeautifulSoup


class Consulta:
    
    def requisicao(self,url):
        req = requests.get(f'{url}')
        return req
        
    def verificar_status(self,req):
        return req.status_code == 200

    def pegar_conteudo(self,status,req):
        if status:
            content = req.content
            soup = BeautifulSoup(content, 'html.parser')
            tabela = soup.find(name='table')
            table_str = str(tabela)
            return table_str
    
    def exibindo_conteudo(self,table):
        df = pd.read_html(table)
        print(df)
        
if __name__=='__main__':
    
    consulta = Consulta()
    req = consulta.requisicao('https://www.todamateria.com.br/estados-do-brasil/')
    status = consulta.verificar_status(req)
    conteudo= consulta.pegar_conteudo(status,req)
    consulta.exibindo_conteudo(conteudo)