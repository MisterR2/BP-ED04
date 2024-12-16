import logging
from decimal import Decimal

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = Decimal(preco)

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}"


class Catalogo:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        logging.info(f"Produto adicionado ao catálogo: {produto.nome}")

    def listar_produtos(self):
        return self.produtos

    def buscar_produto_por_id(self, id):
        for produto in self.produtos:
            if produto.id == id:
                logging.info(f"Produto encontrado: {produto.nome}")
                return produto
        logging.error(f"Produto com ID {id} não encontrado.")
        return None

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        logging.info(f"Produto {produto.nome} adicionado ao pedido de {self.cliente}")

    def calcular_total(self, discount=True):
        total = sum(produto.preco for produto in self.produtos)
        if total > Decimal('100') and discount:
            logging.info(f"Desconto de 10% aplicado ao pedido de {self.cliente}")
            total *= Decimal('0.9')
        
        return total
    