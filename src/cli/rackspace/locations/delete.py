from src.api.rackspace.locations_client import delete

def delete_location(args):
    route = f"/locations/{args.location_id}"

    response = delete(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


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