from src.api.rackspace.rows_client import delete_row_location


def delete_row_location_command(args):
    route = f"/rows/{args.row_id}/{args.location_id}"

    response = delete_row_location(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_delete_row_location(subparser):
    delete_parser = subparser.add_parser(
        "delete-location",
        help="Delete location from a row"
    )

    delete_parser.add_argument(
        "row_id",
        type=int,
        help="ID of the row"
    )

    delete_parser.add_argument(
        "location_id",
        type=int,
        help="ID of the location"
    )

    delete_parser.set_defaults(func=delete_row_location_command)