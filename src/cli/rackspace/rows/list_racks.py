from src.api.rackspace.rows_client import get


def get_rows_racks(args):
    route = "/rows/racks"

    response = get(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_list_rows_racks(subparser):
    parser = subparser.add_parser(
        "list-racks",
        help="List all rows with racks"
    )

    parser.set_defaults(func=get_rows_racks)