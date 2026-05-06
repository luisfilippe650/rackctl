from src.api.base_client import post
from src.utils.output import print_response

def create_row(args):
    route = "/rows"

    data = {
        "name": args.name
    }

    response = post(route, data)

    print_response(response)

def register_command_create_rows(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new row"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Row name"
    )

    parser.set_defaults(func=create_row)