from src.api.rackspace.rack_client import get_details


def get_rack_details(args):
    route = f"/racks/{args.rack_id}"

    response = get_details(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_show_rack(subparser):
    parser = subparser.add_parser(
        "show",
        help="Show details of a rack"
    )

    parser.add_argument(
        "rack_id",
        type=int,
        help="Rack ID"
    )

    parser.set_defaults(func=get_rack_details)