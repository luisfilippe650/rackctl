import json


def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


def print_response(response):
    """
    Exibe a resposta da API de forma legível.
    Mantém a URL e o método visíveis para facilitar o debug.
    """
    ok = response.status_code < 400
    symbol = "[+]" if ok else "[-]"

    # Linha de status: [Símbolo] Código Método URL
    print(f"{symbol} {response.status_code} {response.request.method}: {response.url}")

    try:
        response_content = response.json()
        if response_content:
            print(pretty_json(response_content))
    except (ValueError, AttributeError):
        if hasattr(response, "text") and response.text:
            print(response.text)

    print("-" * 50)  # Separador visual
    print()