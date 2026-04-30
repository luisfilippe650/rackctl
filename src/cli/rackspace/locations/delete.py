from src.api.rackspace.locations_client import delete
from src.utils.output import print_response

def delete_location(args):
    route = f"/locations/{args.location_id}"

    response = delete(route)

    print_response(response)


def register_command_delete_location(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a location"
    )

    parser.add_argument(
        "location_id",
        type=int,
        help="Location ID"
    )

    parser.set_defaults(func=delete_location)