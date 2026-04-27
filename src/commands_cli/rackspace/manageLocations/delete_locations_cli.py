from src.api.rackspace.manageLocations_client import delete

def delete_locations(args) -> None:
    data = args.id

    response = delete("/locations/", data)

    print("Status: ", response.status_code)
    print("Response: ", response.text)


def register_command_delete_locations(subparser):
    location_delete_parser = subparser.add_parser(
        "delete location",
        help="delete location"
    )

    location_delete_parser.add_argument(
        "id",
        type=int,
        help="Resource id"
    )

    location_delete_parser.set_defaults(func=delete_locations)