from src.api.rackspace.rack_client import get_occupancy


def list_rack_occupancy(args):
    route = "/racks/occupancy"

    response = get_occupancy(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_racks_occupancy(subparser):
    parser = subparser.add_parser(
        "occupancy",
        help="List racks with occupancy"
    )

    parser.set_defaults(func=list_rack_occupancy)