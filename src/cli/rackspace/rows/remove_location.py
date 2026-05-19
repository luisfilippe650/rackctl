from api.base_client import delete
from utils.output import print_response

def delete_location_from_row(args):
    route = f"/rows/{args.row}/{args.location}"

    response = delete(route)

    print_response(response)

def register_command_remove_location(subparser):
    parser = subparser.add_parser(
        "delete-location",
        help="Delete location from a row"
    )

    parser.add_argument(
        "--row",
        type=int,
        required=True,
        help="ID of the row"
    )

    parser.add_argument(
        "--location",
        type=int,
        required=True,
        help="ID of the location"
    )

    parser.set_defaults(func=delete_location_from_row)