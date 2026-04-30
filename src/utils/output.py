import json

def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)

def print_response(response):
    ok = response.status_code < 400
    symbol = "[+]" if ok else "[-]"
    method = response.request.method
    url = response.url

    print(f"\n{symbol} {response.status_code} | {method} {url}")

    try:
        print(pretty_json(response.json()))
    except ValueError:
        print(response.text)
    print()