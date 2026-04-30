from src.api.rackspace.rack_client import delete
from src.utils.output import print_response

def delete_rack(args):
    route = f"/racks/{args.rack_id}"

    response = delete(route)

    print_response(response)


def register_command_delete_rack(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a rack by ID"
    )

    parser.add_argument(
        "rack_id",
        type=int,
        help="Rack ID"
    )

    parser.set_defaults(func=delete_rack)