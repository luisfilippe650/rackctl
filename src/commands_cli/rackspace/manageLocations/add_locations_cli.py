from src.api.rackspace.manageLocations_client import post

#funcao que ira enviar os dados para api
def add_locations(args):

    data = {
        "name": args.name
    }

    response = post("/locations", data)

    print("Status: ", response.status_code)
    print("Response: ", response.text)


def register_command_add_locations(subparsers):
    location_add_parser = subparsers.add_parser(
        "add location",
        help="create new location"
    )

    location_add_parser.add_argument(
        "name",
        type=str,
        help="Resource name"
    )

    location_add_parser.set_defaults(func=add_locations)