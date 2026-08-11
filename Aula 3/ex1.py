class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Notebook", 3500.00)
produto2 = Produto("Mouse", 80.00)

print("Produto:", produto1.nome)
print("Preço: R$", produto1.preco)

print("Produto:", produto2.nome)
print("Preço: R$", produto2.preco)