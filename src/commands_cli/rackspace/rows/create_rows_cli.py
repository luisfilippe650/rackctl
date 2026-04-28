from src.api.rackspace.rows_client import post


def add_row(args):
    route = "/rows"

    data = {
        "name": args.row_name
    }

    response = post(route, data)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_add_row(subparser):
    add_row_parser = subparser.add_parser(
        "add",
        help="Add row"
    )

    add_row_parser.add_argument(
        "row_name",
        type=str,
        help="Row name"
    )

    add_row_parser.set_defaults(func=add_row)