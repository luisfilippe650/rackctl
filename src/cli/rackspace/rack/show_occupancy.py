from src.api.rackspace.rack_client import get_single_occupancy
from src.utils.output import print_response

def show_rack_occupancy(args):
    route = f"/racks/{args.rack_id}/occupancy"

    response = get_single_occupancy(route)

    print_response(response)


def register_command_show_rack_occupancy(subparser):
    parser = subparser.add_parser(
        "show-occupancy",
        help="Show occupancy of a single rack"
    )

    parser.add_argument(
        "rack_id",
        type=int,
        help="Rack ID"
    )

    parser.set_defaults(func=show_rack_occupancy)