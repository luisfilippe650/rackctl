from api.base_client import get
from utils.output import print_response

def list_racks(_):
    route = "/racks"

    response = get(route)

    print_response(response)

def register_command_list_racks(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all racks"
    )

    parser.set_defaults(func=list_racks)