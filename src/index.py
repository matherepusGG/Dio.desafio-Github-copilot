import re

def identificar_bandeira(numero_cartao: str) -> str:
    numero_cartao = re.sub(r'[\s-]', '', numero_cartao)

    patterns = [
        # Visa: 13 or 16 digits, starts with 4
        (r'^4\d{12}(\d{3})?$', 'Visa'),
        # Visa 16 dígitos explicitamente
        (r'^4\d{15}$', 'Visa (16 dígitos)'),
        # MasterCard
        (r'^(5[1-5]\d{14}|222[1-9]\d{12}|22[3-9]\d{13}|2[3-6]\d{14}|27[01]\d{13}|2720\d{12})$', 'MasterCard'),
        # Elo
        (r'^(4011|4312|4389)\d*$', 'Elo'),
        # American Express
        (r'^(34|37)\d{13}$', 'American Express'),
        # Discover
        (r'^(6011\d{12}|65\d{14}|64[4-9]\d{13})$', 'Discover'),
        # Hipercard
        (r'^6062\d*$', 'Hipercard'),
        # Diners Club: 14 digits, starts with 300-305, 36, 38, 39
        (r'^(30[0-5]\d{11}|36\d{12}|38\d{12}|39\d{12})$', 'Diners Club'),
        # EnRoute: 15 digits, starts with 2014 or 2149
        (r'^(2014|2149)\d{11}$', 'EnRoute'),
        # JCB: 16 digits, starts with 3528-3589
        (r'^(35(2[89]|[3-8][0-9])\d{12})$', 'JCB'),
        # Voyager: 15 digits, starts with 8699
        (r'^8699\d{11}$', 'Voyager'),
        # Aura: 16 digits, starts with 50
        (r'^50\d{14}$', 'Aura'),
    ]

    for pattern, bandeira in patterns:
        if re.match(pattern, numero_cartao):
            return bandeira
    return 'Bandeira desconhecida'

# Exemplo de uso:
if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    print("Bandeira:", identificar_bandeira(numero))