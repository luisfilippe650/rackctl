import json
import sys


def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


def print_response(response):
    """
    Displays the API response formatted:
    - Success: prints the URL (lowercase prefix 'url:') and JSON response body when possible.
    - Error: displays where the error occurred and the response content and exits with non-zero status.
    """
    if response.status_code < 400:
        # Success: print the URL (lowercase prefix) and try to pretty-print JSON body
        print(f"url:{response.url}")
        try:
            response_content = response.json()
            print(pretty_json(response_content))
        except (ValueError, AttributeError):
            # Fallback to printing the URL if no JSON body
            print(f"url:{response.url}")
    else:
        # Error: displays where the error is and the response content, then exit
        print(f"Error {response.status_code} at {response.request.method} {response.url}")
        try:
            response_content = response.json()
            if response_content:
                print(pretty_json(response_content))
        except (ValueError, AttributeError):
            if hasattr(response, "text") and response.text:
                print(response.text)
        sys.exit(1)
