from src.api.rackspace.locations_client import get_rows

def list_locations_with_rows(args):
    response = get_rows("/locations/rows")

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_list_locations_rows(subparser):
    parser = subparser.add_parser(
        "list-rows",
        help="List locations with rows"
    )

    parser.set_defaults(func=list_locations_with_rows)