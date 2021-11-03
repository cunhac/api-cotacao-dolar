from datetime import date, datetime
from time import sleep
import requests

def cotacao_dolar(data_cotacao):

    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_cotacao}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"
    cotacao = requests.get(url)
    dados = cotacao.json()
    data_atual = datetime.now().date()
    date_base = data_cotacao
    date = datetime.strptime(date_base, '%m-%d-%Y').date()
    if date > data_atual:
        return 0.00, 0.00
    elif dados["value"] == []:
        return 0.00, 0.00
    else:
        pass

    data = dados["value"][0]["dataHoraCotacao"]
    venda = dados["value"][0]["cotacaoVenda"]
    compra = dados["value"][0]["cotacaoCompra"]

    return venda, compra


