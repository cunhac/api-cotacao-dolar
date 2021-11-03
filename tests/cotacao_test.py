from ..src.cotacao import cotacao_dolar

def test_cotacao_cotacao_dolar():
    venda,compra = cotacao_dolar("10-05-2021")
    
    assert round(venda, 4) == round(5.4611, 4)
    assert round(compra, 4) == round(5.4605, 4)


def test_cotacao_cotacao_dolar_dia_futuro():
    venda,compra = cotacao_dolar("11-05-2030")
    
    assert round(venda, 4) == round(0.00, 4)
    assert round(compra, 4) == round(0.00, 4)


def test_cotacao_cotacao_dolar_fim_de_semana():
    venda,compra = cotacao_dolar("10-09-2021")
    
    assert round(venda, 4) == round(0.00, 4)
    assert round(compra, 4) == round(0.00, 4)


def test_cotacao_cotacao_dolar_feriado():
    venda,compra = cotacao_dolar("10-12-2021")

    assert round(venda, 4) == round(0.00, 4)
    assert round(compra, 4) == round(0.00, 4)
