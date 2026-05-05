from src.api.base_client import delete
from src.utils.output import print_response

def delete_location_from_row(args):
    route = f"/rows/{args.row_id}/{args.location_id}"

    response = delete(route)

    print_response(response)

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