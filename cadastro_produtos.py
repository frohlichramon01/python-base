"""Cadastro de produto"""
__version__ = "0.1.0"

import pprint

produto = {
    "nome": "Caneta",
    "cores": ["Azul", "Branco"],
    "preco": 3.10,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 12345,
    "codebar": None,
}

cliente = {
    "nome": "Bruno",
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

pprint.pprint(compra)
