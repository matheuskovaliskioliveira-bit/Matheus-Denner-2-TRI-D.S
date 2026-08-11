class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print("Aluno")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Matrícula:", self.matricula)
        print()


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print("Professor")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Salário:", self.salario)
        print()


pessoas = [
    Aluno("Matheus", 16, "2026001"),
    Professor("João", 40, 6500),
    Aluno("Ana", 17, "2026002"),
    Professor("Maria", 35, 7200)
]

for pessoa in pessoas:
    pessoa.apresentar()