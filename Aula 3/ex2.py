class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        novo_preco = self.preco - (self.preco * percentual / 100)
        return novo_preco

produto = Produto("Notebook", 100.0)

print("Preço original: R$", produto.preco)
print("Preço com desconto: R$", produto.desconto(10))