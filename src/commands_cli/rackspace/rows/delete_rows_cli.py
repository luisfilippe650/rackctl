from src.api.rackspace.rows_client import delete


def delete_row(args):
    route = f"/rows/{args.row_id}"

    response = delete(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_delete_row(subparser):
    delete_parser = subparser.add_parser(
        "delete",
        help="Delete a row"
    )

    delete_parser.add_argument(
        "row_id",
        type=int,
        help="ID of the row"
    )

    delete_parser.set_defaults(func=delete_row)