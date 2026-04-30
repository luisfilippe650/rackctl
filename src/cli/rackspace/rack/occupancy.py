from src.api.rackspace.rack_client import get_occupancy
from src.utils.output import print_response


def list_rack_occupancy(_):
    route = "/racks/occupancy"

    response = get_occupancy(route)

    print_response(response)


def register_command_racks_occupancy(subparser):
    parser = subparser.add_parser(
        "occupancy",
        help="List racks with occupancy"
    )

    parser.set_defaults(func=list_rack_occupancy)