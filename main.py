from decimal import Decimal
from market import Produto, Catalogo, Pedido

def exibir_menu():
    print("\n=== MENU ===")
    print("1. Adicionar Produto ao Catálogo")
    print("2. Listar Produtos do Catálogo")
    print("3. Buscar Produto por ID")
    print("4. Criar Pedido")
    print("5. Adicionar Produto ao Pedido")
    print("6. Exibir Pedido e Total")
    print("7. Sair")

def main():
    catalogo = Catalogo()
    pedido_atual = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Adicionar produto ao catálogo
            try:
                while True:
                    try:
                        id = int(input("ID do Produto: "))
                        break
                    except ValueError:
                        print("ID inválido. Por favor, insira um número inteiro.")
                nome = input("Nome do Produto: ")
                while True:
                    try:
                        # Tratamento para aceitar tanto ',' quanto '.' como separador decimal
                        preco_input = input("Preço do Produto: ").replace(',', '.')
                        preco = Decimal(preco_input)
                        break
                    except:
                        print("ID inválido. Por favor, insira um número inteiro.")
                
                produto = Produto(id, nome, preco)
                catalogo.adicionar_produto(produto)
            except Exception as e:
                print(f"Erro ao adicionar produto: {e}")

        elif opcao == "2":
            # Listar produtos do catálogo
            produtos = catalogo.listar_produtos()
            if produtos:
                print("\n=== Produtos no Catálogo ===")
                for produto in produtos:
                    print(f"{produto}")
            else:
                print("O catálogo está vazio.")

        elif opcao == "3":
            # Buscar produto por ID
            produtos = catalogo.listar_produtos()
            
            if not produtos:
                print("O catálogo está vazio.")
                continue
            
            id_produto = int(input("ID do Produto desejado: "))
            produto = catalogo.buscar_produto_por_id(id_produto)
            if produto:
                print(f"\n=== Produto Encontrado ===")
                print(f"{produto}")
            else:
                print("Produto não encontrado no catálogo.")
        
        elif opcao == "4":
            # Criar um pedido
            nome_cliente = input("Nome do Cliente: ")
            pedido_atual = Pedido(nome_cliente)
            print(f"Pedido criado para o cliente '{nome_cliente}'.")

        elif opcao == "5":
            # Adicionar produto ao pedido
            if pedido_atual is None:
                print("Nenhum pedido ativo. Crie um pedido primeiro.")
            else:
                try:
                    id_produto = int(input("ID do Produto a adicionar: "))
                    produto = catalogo.buscar_produto_por_id(id_produto)
                    if produto:
                        pedido_atual.adicionar_produto(produto)
                    else:
                        print("Produto não encontrado no catálogo.")
                except Exception as e:
                    print(f"Erro ao adicionar produto ao pedido: {e}")

        elif opcao == "6":
            # Exibir pedido e total
            if pedido_atual is None:
                print("Nenhum pedido ativo.")
            else:
                print(f"\n=== Pedido de {pedido_atual.cliente} ===")
                if pedido_atual.produtos:
                    for produto in pedido_atual.produtos:
                        print(f"{produto}")
                    total = pedido_atual.calcular_total()
                    print(f"Total do Pedido: R${total:.2f}")
                else:
                    print("Nenhum produto no pedido.")

        elif opcao == "7":
            # Sair do programa
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
