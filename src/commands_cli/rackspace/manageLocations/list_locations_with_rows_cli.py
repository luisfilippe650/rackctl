from src.api.rackspace.manageLocations_client import get_rows

def get_rack_with_rows() -> None:

    response = get_rows("/locations/rows")

    print("Status: ", response.status_code)
    print("Response: ", response.text)

def register_get_locations_with_rows(subparser):

    location_get_with_rows_parser = subparser.add_parser(
        "list location rows"
    )

    location_get_with_rows_parser.set_defaults(func=get_rack_with_rows)