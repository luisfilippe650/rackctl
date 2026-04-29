from src.api.rackspace.locations_client import get


def list_locations(args):
    response = get("/locations")

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_list_locations(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all locations"
    )

    parser.set_defaults(func=list_locations)