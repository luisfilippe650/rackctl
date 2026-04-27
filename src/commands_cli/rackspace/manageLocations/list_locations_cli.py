from src.api.rackspace.manageLocations_client import get

def get_locations() -> None:
    response = get("/locations")

    print("Status: ", response.status_code)
    print("Response: ", response.text)


def register_command_get_locations(subparser):
    location_get_parser = subparser.add_parser(
        "list location",
        help="list locations"
    )

    location_get_parser.set_defaults(func=get_locations)