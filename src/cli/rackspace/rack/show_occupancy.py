from src.api.base_client import get
from src.utils.output import print_response

def show_rack_occupancy(args):
    route = f"/racks/{args.id}/occupancy"

    response = get(route)

    print_response(response)

def register_command_show_rack_occupancy(subparser):
    parser = subparser.add_parser(
        "show-occupancy",
        help="Show occupancy of a single rack"
    )

    parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="Rack ID"
    )

    parser.set_defaults(func=show_rack_occupancy)