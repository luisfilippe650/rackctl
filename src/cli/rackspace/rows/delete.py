from api.base_client import delete
from utils.output import print_response

def delete_row(args):
    route = f"/rows/{args.id}"

    response = delete(route)

    print_response(response)

def register_command_delete_rows(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a row by ID"
    )

    parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="ID of the row"
    )

    parser.set_defaults(func=delete_row)