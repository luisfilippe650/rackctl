from src.api.rackspace.rows_client import get


def list_rows(args):
    route = "/rows"

    response = get(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_list_rows(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all rows"
    )

    parser.set_defaults(func=list_rows)