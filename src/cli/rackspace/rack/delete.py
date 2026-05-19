from api.base_client import delete
from utils.output import print_response

def delete_rack(args):
    route = f"/racks/{args.id}"

    response = delete(route)

    print_response(response)

def register_command_delete_rack(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a rack by ID"
    )

    parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="Rack ID"
    )

    parser.set_defaults(func=delete_rack)