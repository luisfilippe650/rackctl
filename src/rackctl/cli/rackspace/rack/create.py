from rackctl.api.base_client import post
from rackctl.utils.output import print_response

def create_rack(args):
    route = "/racks"

    data = {
        "name": args.name,
        "rack_height": args.height,
        "row_id": args.row
    }

    response = post(route, data)

    print_response(response)

def register_command_create_rack(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a rack"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
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