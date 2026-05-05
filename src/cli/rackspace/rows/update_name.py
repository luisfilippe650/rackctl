from src.api.base_client import patch
from src.utils.output import print_response

def rename_row(args):
    route = f"/rows/{args.row_id}"

    data = {
        "name": args.name
    }

    response = patch(route, data)

    print_response(response)

def register_command_update_name(subparser):
    parser = subparser.add_parser(
        "rename",
        help="Rename a row"
    )

    parser.add_argument(
        "row_id",
        type=int,
        help="ID of the row"
    )

    parser.add_argument(
        "name",
        type=str,
        help="New row name"
    )

    parser.set_defaults(func=rename_row)