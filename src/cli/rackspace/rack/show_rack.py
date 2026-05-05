from src.api.base_client import get
from src.utils.output import print_response

def get_rack_details(args):
    route = f"/racks/{args.rack_id}"

    response = get(route)

    print_response(response)

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