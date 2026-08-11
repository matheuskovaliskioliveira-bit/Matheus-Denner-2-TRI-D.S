class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    # Getter e Setter do nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    # Getter e Setter do preço
    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço inválido!")

produto = Produto("Notebook", 3500)

print(produto.get_nome())
print(produto.get_preco())

produto.set_preco(3000)
print(produto.get_preco())

produto.set_preco(-100)