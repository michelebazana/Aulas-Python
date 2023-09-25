while True:
    try:
        num = int(input("Entre com um número inteiro: "))
        if num == 0:
            break
    except Exception:
        print("Número inválido! Entre com um número válido.")
