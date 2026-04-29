from src.api.rackspace.rack_client import post

def create_rack(args):
    route = "/racks"

    data = {
        "name": args.name,
        "rack_height": args.height,
        "row_id": args.row
    }

    response = post(route, data)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_create_rack(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a rack"
    )

    parser.add_argument(
        "name",
        type=str,
        help="Rack name"
    )

    parser.add_argument(
        "--height",
        type=int,
        required=True,
        help="Rack height"
    )

    parser.add_argument(
        "--row",
        type=int,
        required=True,
        help="Row ID"
    )

    parser.set_defaults(func=create_rack)