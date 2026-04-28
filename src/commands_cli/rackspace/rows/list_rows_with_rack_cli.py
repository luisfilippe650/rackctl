from src.api.rackspace.rows_client import get

def get_rows_racks(args):
    route = "/rows/racks"

    response = get(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_get_rows_racks(subparser):
    get_rows_racks_parser = subparser.add_parser(
        "list racks",
        help="List all rows with racks"
    )

    get_rows_racks_parser.set_defaults(func=get_rows_racks)