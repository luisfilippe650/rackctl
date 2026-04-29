from src.api.rackspace.rack_client import get

def list_racks(args):
    route = "/racks"

    response = get(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_list_racks(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all racks"
    )

    parser.set_defaults(func=list_racks)