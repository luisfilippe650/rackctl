from src.api.rackspace.rows_client import put

def add_location_to_row(args):
    route = f"/rows/{args.row_id}/{args.location_id}"

    response = put(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_add_location_to_row(subparser):
    parser = subparser.add_parser(
        "add-location",
        help="Add location to row"
    )

    parser.add_argument(
        "row_id",
        type=int,
        help="ID of row"
    )

    parser.add_argument(
        "location_id",
        type=int,
        help="ID of location"
    )

    parser.set_defaults(func=add_location_to_row)