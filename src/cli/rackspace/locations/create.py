from src.api.rackspace.locations_client import post

def create_location(args):
    data = {
        "name": args.name
    }

    response = post("/locations", data)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_create_location(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new location"
    )

    parser.add_argument(
        "name",
        type=str,
        help="Location name"
    )

    parser.set_defaults(func=create_location)