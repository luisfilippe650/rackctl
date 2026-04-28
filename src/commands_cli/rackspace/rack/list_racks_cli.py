from src.api.rackspace.rack_client import get

def get_rack(args):
    route = "/racks"

    response = get(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_get_racks(subparser):
    get_racks_parser = subparser.add_parser(
        "list",
        help="List all racks"
    )

    get_racks_parser.set_defaults(func=get_rack)
