from src.api.rackspace.rows_client import put


def add_location_to_row(args):

    route = f"/rows/{args.row_id}/{args.location_id}"

    response = put(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_add_location_to_row(subparser):
    add_location_parser = subparser.add_parser(
        "add-location",
        help="Add location at row"
    )

    add_location_parser.add_argument(
        "row_id",
        type=int,
        help="ID of row"
    )

    add_location_parser.add_argument(
        "location_id",
        type=int,
        help="ID of location"
    )

    add_location_parser.set_defaults(func=add_location_to_row)