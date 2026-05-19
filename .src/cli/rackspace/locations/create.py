from api.base_client import post
from utils.output import print_response

def create_location(args):
    data = {
        "name": args.name
    }

    response = post("/locations", data)

    print_response(response)

def register_command_create_location(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new location"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Location name"
    )

    parser.set_defaults(func=create_location)