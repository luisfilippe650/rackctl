import json
import sys


def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


def print_response(response):
    """
    Displays the API response formatted:
    - Success: prints a combined JSON with the URL and the response body.
    - Error: displays where the error occurred and the response content and exits with non-zero status.
    """
    if response.status_code < 400:
        # Success: print a combined JSON with the URL and the response body
        try:
            response_content = response.json()
            output = {
                "url": response.url,
                "data": response_content
            }
            print(pretty_json(output))
        except (ValueError, AttributeError):
            # Fallback to printing just the URL in JSON format if no body
            print(pretty_json({"url": response.url}))
    else:
        # Error: displays where the error is and the response content, then exit
        error_output = {
            "error": f"{response.status_code}",
            "method": response.request.method,
            "url": response.url
        }
        try:
            response_content = response.json()
            if response_content:
                error_output["data"] = response_content
        except (ValueError, AttributeError):
            if hasattr(response, "text") and response.text:
                error_output["message"] = response.text
        
        print(pretty_json(error_output))
        sys.exit(1)
