from cotacao import cotacao_dolar
from datetime import datetime, timedelta


def main():
    data_cotacao_inicial = input('Data da cotação inicial[mm-dd-aaaa]:')
    data_cotacao_final = input('Data da cotação final[mm-dd-aaaa]:')


    data_inicial  = datetime.strptime(data_cotacao_inicial, '%m-%d-%Y').date()
    data_final = datetime.strptime(data_cotacao_final, '%m-%d-%Y').date()


    delta = data_final - data_inicial


    numdays = delta.days +1
    date_list = [data_final - timedelta(days=x) for x in range(numdays)]


    date_list_conversao_data = []
    for d in date_list:
        date_time = d.strftime("%m-%d-%Y")
        date_list_conversao_data.append(date_time)


    todas_cotacoes={}


    for d in date_list_conversao_data:
        venda,compra = cotacao_dolar(d) 
        todas_cotacoes[d] = {'venda': venda, 'compra': compra}
        

    def print_cotacao(todas_cotacoes):
        for k, v in todas_cotacoes.items():
            if v["venda"] == 0 or v["compra"] == 0:
                print(f'{k} - Cotação do Dólar: Dia não útil')
            else:
                print(f'{k} - Cotação do Dólar: Venda R$ {v["venda"]:.4f} | Compra R$  {v["compra"]:.4f}')
            
       
    print_cotacao(todas_cotacoes)


if __name__ == '__main__':
    main()
