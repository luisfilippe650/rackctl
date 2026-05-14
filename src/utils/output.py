import json


def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


def print_response(response):
    """
    Displays the API response formatted:
    - Success: only the URL inside braces.
    - Error: displays where the error occurred and the response content.
    """
    if response.status_code < 400:
        # Success: only the URL inside braces
        print(f"{{{response.url}}}")
    else:
        # Error: displays where the error is and the response content
        print(f"Error {response.status_code} at {response.request.method} {response.url}")
        try:
            response_content = response.json()
            if response_content:
                print(pretty_json(response_content))
        except (ValueError, AttributeError):
            if hasattr(response, "text") and response.text:
                print(response.text)