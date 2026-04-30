from src.api.rackspace.rows_client import get
from src.utils.output import print_response

def list_rows(_):
    route = "/rows"

    response = get(route)

    print_response(response)


def register_command_list_rows(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all rows"
    )

    parser.set_defaults(func=list_rows)