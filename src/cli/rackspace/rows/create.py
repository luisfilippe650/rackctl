from src.api.rackspace.rows_client import post

def create_row(args):
    route = "/rows"

    data = {
        "name": args.name
    }

    response = post(route, data)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_create_rows(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new row"
    )

    parser.add_argument(
        "name",
        type=str,
        help="Row name"
    )

    parser.set_defaults(func=create_row)