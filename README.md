
**Cotação_dólar - API (Python)**


Este projeto tem como objetivo realizar a cotação do dólar referente a uma data ou um período.

As informações serão coletadas através do site oficial do Banco Central: https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes

A consulta da cotação é realizada através da solicitação dos inputs da data inicial (mm-dd-aaaa) e data final  (mm-dd-aaaa).

Essas informações são a base para alimentar a API que retornará com os valores das cotações do dólar correspondentes a venda e a compra.

As informações serão fornecidas apenas para dias úteis. Aos finais de semana e feriados retornará a informação: `dia não útil`. Esses casos foram testados e estão no arquivo `tests/cotacao_test.py`.

<br><br>


**INSTALAÇÃO**

    Instalar o ambiente virtual:
        $ python -m venv venv
    
    Ativar o venv(Windows):
        $ venv\Scripts\activate

    Na sequência instalar o requirementes:
        $ pip install -r requirements.txt
        
<br>

**ESTRUTURA DO REPOSITÓRIO**
```
api_cotacao_dolar/
├── docs/
|   └── imagem_cotacao.JPG
├── src/
│   └── cotacao.py
├── tests/
│   └── cotacao_test.py
├── main.py
├── readme.md
└── requirements.txt
```
#
**DEMONSTRAÇÃO DA APLICAÇÃO**

![MENU](docs/imagem_cotacao.JPG)

#
**EXPLICAÇÃO DOS ARQUIVOS**

* `docs/`: <p>- armazenamento da imagem `.jpg` com a demonstração da aplicação.</p>
<br/>

* `src/` : 
     <p>- cotacao.py: consta a função cotacao_dolar com a url para a realização da API.</p>
<br>

* `tests/`:
<br>

   <p>- cotacao_test.py: foram desenvolvidos testes para data futura, data no final de semana, feriado e dias úteis.</p>
<br>


* `main.py`:
<br>

    - consta os inputs das datas para a realização da cotação, como também, a conversão dessas datas para o padrão solicitado pelo site responsável pela API. 
    O retorno da API será estruturado em um dicionário.
    A função print_cotacao realiza a configuração da visualização das informações disponíveis no dicionário. 
    O arquivo main.py é responsável por rodar o código.

<br>

* `requirements.txt`: 
<br>

    requests==2.26.0
    pytest==6.2.5
<br>
