from src.api.base_client import put
from src.utils.output import print_response

def add_location_to_row(args):
    route = f"/rows/{args.row_id}/{args.location_id}"

    response = put(route)

    print_response(response)

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