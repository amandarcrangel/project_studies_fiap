from email.policy import default


def calcula_pizza(tamanho, quantidade_sabores):
    # Verifica se a quantidade de sabores é válida
    if quantidade_sabores < 1:
        return "A quantidade de sabores deve ser pelo menos 1."

    if tamanho.lower() == 'pequena':
        preco = 20
    elif tamanho.lower() == 'media':
        preco = 30
    elif tamanho.lower() == 'grande':
        preco = 40
    else:
        return "Tamanho de pizza inválido. Escolha entre 'pequena', 'media' ou 'grande'."

    preco += (quantidade_sabores - 1) * 5
    return preco


# Teste da função
print(calcula_pizza('pequena', 1))  # 20
print(calcula_pizza('media', 2))  # 35
print(calcula_pizza('grande', 3))  # 50
print(calcula_pizza('gigante', 2))  # Tamanho de pizza inválido
print(calcula_pizza('media', 0))  # A quantidade de sabores deve ser pelo menos 1.
