import sys

# Dados iniciais
class Filme:
 def __init__(self, titulo, horarios, preco):
    self.titulo = titulo
    self.horarios = horarios
    self.preco = preco

filmes = {
    1: Filme("Mulher-Maravilha", ["14:00", "17:30", "20:45"], 25.0),
    2: Filme("Vingadores: Ultimato", ["13:15", "16:40", "19:55"], 28.20),
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

def escolher_filme():
    print("Filmes disponíveis:")
    for idx, filme in filmes.items():
        print(f"{idx}. {filme.titulo} (R${filme.preco:.2f})")
    escolha = int(input("Escolha o número do filme: "))
    return escolha

def escolher_horario(filme_id):
    horarios = filmes[filme_id].horarios
    print("\nHorários disponíveis:")
    for i, h in enumerate(horarios, 1):
        print(f"{i}. {h}")
    escolha = int(input("Escolha o horário: "))
    return horarios[escolha - 1]

def escolher_dublagem():
    print("\nOpções de dublagem:")
    for idx, (nome, acrescimo) in dublagens.items():
        sinal = "+" if acrescimo > 0 else ""
        print(f"{idx}. {nome} ({sinal}R${acrescimo:.2f} por ingresso)")
    escolha = int(input("Escolha a dublagem: "))
    return dublagens[escolha]

def escolher_pagamento():
    print("\nFormas de pagamento:")
    for idx, (nome, taxa) in formas_pagamento.items():
        desc = f"+{taxa*100:.0f}%" if taxa > 0 else f"{taxa*100:.0f}%"
        print(f"{idx}. {nome} ({desc})")
    escolha = int(input("Escolha a forma de pagamento: "))
    return formas_pagamento[escolha]

def main():
    print("🎬 Bem-vindo ao Cinema Python\n")

    # Escolhas iniciais
    id_filme = escolher_filme()
    filme = filmes[id_filme]
    horario = escolher_horario(id_filme)
    nome_dub, acrescimo_dub = escolher_dublagem()
    nome_pgto, taxa_pgto = escolher_pagamento()

    # Quantidade de ingressos
    total = int(input("\nQuantidade total de ingressos: "))
    meia = int(input("Quantos são meia-entrada? "))
    inteira = total - meia

    # Cálculo do valor bruto
    preco_base = filme.preco
    valor_inteira = inteira * preco_base
    valor_meia = meia * (preco_base / 2)
    soma = valor_inteira + valor_meia

    # Acréscimo de dublagem
    soma += total * acrescimo_dub
    # Aplicar taxa de pagamento
    valor_final = soma * (1 + taxa_pgto)

    # Resumo
    print("\n--- Resumo da Compra ---")
    print(f"Filme: {filme.titulo}")
    print(f"Horário: {horario}")
    print(f"Dublagem: {nome_dub} (acréscimo R${acrescimo_dub:.2f}/ingresso)")
    print(f"Forma de Pagamento: {nome_pgto} (taxa {taxa_pgto*100:.0f}%)")
    print(f"Ingressos Inteira: {inteira} x R${preco_base:.2f} = R${valor_inteira:.2f}")
    print(f"Ingressos Meia: {meia} x R${preco_base/2:.2f} = R${valor_meia:.2f}")
    print(f"Valor Bruto: R${soma:.2f}")
    print(f"Valor Final: R${valor_final:.2f}")
    print("------------------------\n")
    print("Obrigado e bom filme! 🎥")

if __name__ == "__main__":
    main()

