from src.api.rackspace.rack_client import get_occupancy

def get_rack_occupancy(args):
    route = "/racks/occupancy"

    response = get_occupancy(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_get_racks_occupancy(subparser):
    get_racks_occupancy_parser = subparser.add_parser(
        "occupancy",
        help="List all racks with occupancy"
    )

    get_racks_occupancy_parser.set_defaults(func=get_rack_occupancy)

