from src.api.rackspace.rack_client import delete

def delete_racks(args):

    route = f"/racks/{args.rack_id}"

    response = delete(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_delete_racks(subparser):
    delete_racks_parser = subparser.add_parser(
        "delete",
        help="delete rack"
    )

    delete_racks_parser.add_argument(
        "rack_id",
        type=int,
        help="ID of rack"
    )

    delete_racks_parser.set_defaults(func=delete_racks)