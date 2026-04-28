from src.api.rackspace.rows_client import get


def list_rows(args):
    route = "/rows"

    response = get(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_list_rows(subparser):
    list_parser = subparser.add_parser(
        "list",
        help="List all rows"
    )

    list_parser.set_defaults(func=list_rows)