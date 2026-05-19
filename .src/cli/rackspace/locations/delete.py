from api.base_client import delete
from utils.output import print_response

def delete_location(args):
    route = f"/locations/{args.id}"

    response = delete(route)

    print_response(response)

def register_command_delete_location(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a location"
    )

    parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="Location ID"
    )

    parser.set_defaults(func=delete_location)