from src.api.rackspace.rows_client import patch

def patch_rows(args):

    route = f"/rows/{args.row_id}"

    data = {
        "name": args.row_name
    }

    response = patch(route,data)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_patch_rows(subparser):
    patch_rows_parser = subparser.add_parser(
        "rename",
        help="rename row"
    )

    patch_rows_parser.add_argument(
        "row_id",
        type=int,
        help="id row for alter name"
    )

    patch_rows_parser.add_argument(
        "row_name",
        type=str,
        help="row name"
    )

    patch_rows_parser.set_defaults(func=patch_rows)