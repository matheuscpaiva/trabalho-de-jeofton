import sys

# Dados iniciais
def __init__(self, titulo, horarios, preco):
    self.titulo = titulo
    self.horarios = horarios
    self.preco = preco

filmes = {
    1: Filme("Mulher-Maravilha", ["14:00", "17:30", "20:45"], 25,0),
    2: Filme("Vingadores: Ultimato", ["13:15", "16:40", "19:55"], 28,0),
    3: Filme("O incrível Hulk", ["12:00", "15:20", "18:50"], 22.0)
}

formas_pagamento = {
    1: ("Dinheiro", 0.00),          # sem acréscimo
    2: ("Cartão de Crédito", 0.10), # +10%
    3: ("Pix", -0.05)               # -5%
}

dublagens = {
    1: ("Dublado", 2.00),    # acréscimo de R$2 por ingresso
    2: ("Legendado", 0.00)   # sem acréscimo
}
