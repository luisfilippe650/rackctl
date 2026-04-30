from src.api.rackspace.rack_client import patch
from utils.output import print_response

def rename_rack(args):
    route = f"/racks/{args.rack_id}"

    data = {
        "name": args.name
    }

    response = patch(route, data)

    print_response(response)


def register_command_rename_rack(subparser):
    parser = subparser.add_parser(
        "rename",
        help="Rename a rack"
    )

    parser.add_argument(
        "rack_id",
        type=int,
        help="Rack ID"
    )

    parser.add_argument(
        "name",
        type=str,
        help="New rack name"
    )

    parser.set_defaults(func=rename_rack)