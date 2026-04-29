from src.api.rackspace.rows_client import delete_row_location


def delete_location_from_row(args):
    route = f"/rows/{args.row_id}/{args.location_id}"

    response = delete_row_location(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_remove_location(subparser):
    parser = subparser.add_parser(
        "delete-location",
        help="Delete location from a row"
    )

    parser.add_argument(
        "row_id",
        type=int,
        help="ID of the row"
    )

    parser.add_argument(
        "location_id",
        type=int,
        help="ID of the location"
    )

    parser.set_defaults(func=delete_location_from_row)