from src.api.rackspace.rows_client import delete
from src.utils.output import print_response

def delete_row(args):
    route = f"/rows/{args.row_id}"

    response = delete(route)

    print_response(response)


def register_command_delete_rows(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a row by ID"
    )

    parser.add_argument(
        "row_id",
        type=int,
        help="ID of the row"
    )

    parser.set_defaults(func=delete_row)