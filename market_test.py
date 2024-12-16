import unittest
import logging
from decimal import Decimal
from market import Produto, Catalogo, Pedido

# Configuração do logger nos testes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Testes Unitários com integração de logging
class TestSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial para a classe de teste."""
        logging.info("Iniciando os testes do sistema...")

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        logging.info("Configurando os objetos para o teste...")
        self.catalogo = Catalogo()
        self.produto1 = Produto(1, "Notebook", 2000.0)
        self.produto2 = Produto(2, "Mouse", 50.0)
        self.produto3 = Produto(3, "Teclado", 100.0)

        # Adicionar produtos ao catálogo
        self.catalogo.adicionar_produto(self.produto1)
        self.catalogo.adicionar_produto(self.produto2)
        self.catalogo.adicionar_produto(self.produto3)

    def test_adicionar_produto_catalogo(self):
        """Teste para verificar se os produtos são adicionados corretamente ao catálogo."""
        logging.info("Testando adição de produtos ao catálogo...")
        self.assertEqual(len(self.catalogo.listar_produtos()), 3)
        self.assertIn(self.produto1, self.catalogo.listar_produtos())

    def test_buscar_produto_por_id(self):
        """Teste para verificar a busca de produtos por ID."""
        logging.info("Testando busca de produto por ID...")
        produto = self.catalogo.buscar_produto_por_id(1)
        self.assertEqual(produto.nome, "Notebook")

        produto_inexistente = self.catalogo.buscar_produto_por_id(99)
        self.assertIsNone(produto_inexistente)

    def test_calculo_pedido_sem_desconto(self):
        """Teste para verificar o cálculo de um pedido sem desconto."""
        logging.info("Testando cálculo do pedido sem desconto...")
        pedido = Pedido("Maria")
        pedido.adicionar_produto(self.produto2)  # Mouse - R$50.0
        pedido.adicionar_produto(self.produto3)  # Teclado - R$100.0
        total = pedido.calcular_total(False)
        self.assertEqual(total, Decimal('150.0'))

    def test_calculo_pedido_com_desconto(self):
        """Teste para verificar o cálculo de um pedido com desconto."""
        logging.info("Testando cálculo do pedido com desconto...")
        pedido = Pedido("João")
        pedido.adicionar_produto(self.produto1)  # Notebook - R$2000.0
        total = pedido.calcular_total()
        self.assertEqual(total, Decimal('1800.0'))  # 10% de desconto aplicado

    def test_adicionar_produto_pedido(self):
        """Teste para verificar a adição de produtos ao pedido."""
        logging.info("Testando adição de produtos ao pedido...")
        pedido = Pedido("Carlos")
        pedido.adicionar_produto(self.produto2)
        self.assertIn(self.produto2, pedido.produtos)

    @classmethod
    def tearDownClass(cls):
        """Finalização dos testes."""
        logging.info("Todos os testes foram concluídos.")


if __name__ == "__main__":
    unittest.main()
