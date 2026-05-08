import json


def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


def print_response(response):

    ok = response.status_code < 400
    symbol = "[+]" if ok else "[-]"

    method = response.request.method
    url = response.url

    try:
        response_content = response.json()

    except ValueError:
        response_content = response.text

    output = {
        "url": url,
        "status_code": response.status_code,
        "method": method,
        "symbol": symbol,
        "response": response_content
    }

    print(pretty_json(output))
    print()