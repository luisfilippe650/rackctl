from src.api.rackspace.locations_client import get
from src.utils.output import print_response

def list_locations(_):
    response = get("/locations")

    print_response(response)


def register_command_list_locations(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all locations"
    )

    parser.set_defaults(func=list_locations)