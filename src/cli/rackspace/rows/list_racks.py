from src.api.rackspace.rows_client import get
from src.utils.output import print_response

def get_rows_racks(_):
    route = "/rows/racks"

    response = get(route)

    print_response(response)


def register_command_list_rows_racks(subparser):
    parser = subparser.add_parser(
        "list-racks",
        help="List all rows with racks"
    )

    parser.set_defaults(func=get_rows_racks)