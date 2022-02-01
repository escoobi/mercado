from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print("=" * 100)
    print("=" * 40 + " Bem-Vindo(a) " + "=" * 46)
    print("=" * 40 + " Python Shop's " + "=" * 45)
    print("=" * 100)
    print("Selecionar uma opção abaixo: ")
    print("1 - Cadastrar Produto")
    print("2 - Listas Produto")
    print("3 - Comprar Produto")
    print("4 - Visualizar carrinho")
    print("5 - Fechar Pedido")
    print("6 - Sair")

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Bye!")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida!")
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print("Cadastro de produto")
    print("+++++++++++++++++++")
    nome: str = str(input("Informe o nome do produto: "))
    preco: float = float(input("Informe o preço do produto: "))
    # Instanciando a class produto
    produto: Produto = Produto(nome, preco)
    # Adicionar o objeto Produto instanciado na Lista de Produtos
    produtos.append(produto)
    print(f"O Produto {produto.nome} foi cadastrado com sucesso!")
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print("Listagem de produtos")
        print("++++++++++++++++++++")
        for prod in produtos:
            print(prod)
            print("------------------")
            sleep(1)
            menu()
    else:
        print("Ainda não existe produtos cadastrado.")
        sleep(2)
        menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print("Informe o código do produto que deseja cadastrar: ")
        print("--------------------------------------------------")
        print("........... Produtos disponíveis .................")
        for prod in produtos:
            print(prod)
            print("----------------------------------------")
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f"O produto {prod.nome} agora possui {quant + 1} unidades no carriho.")
                        tem_carrinho = True
                        sleep(2)
                        menu()
                if not tem_carrinho:
                    pro = {produto: 1}
                    carrinho.append(pro)
                    print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                    sleep(2)
                    menu()
                else:
                    pass
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                sleep(2)
                menu()
        else:
            print(f"O produto com o código {codigo} não foi encontrado.")
            sleep(2)
            menu()

    else:
        print("Não existe produtos cadastrado.")
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print("Produtos no carrinho: ")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                print("-------------------------")
                sleep(1)

    else:
        print("Não tem produtos no carrinho.")
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print("Carrinho")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                valor_total += dados[0].preco * dados[1]
                print("------------------------------")
                sleep(2)
        print(f"A sua fatura é {formata_float_str_moeda(valor_total)}")
        print("Bye!")
        carrinho.clear()
        sleep(5)

    else:
        print("Carrinho vazio!")
        sleep(2)
        menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == "__main__":
    main()
