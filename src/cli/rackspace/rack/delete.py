from src.api.rackspace.rack_client import delete

def delete_rack(args):
    route = f"/racks/{args.rack_id}"

    response = delete(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_delete_rack(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a rack by ID"
    )

    parser.add_argument(
        "rack_id",
        type=int,
        help="Rack ID"
    )

    parser.set_defaults(func=delete_rack)