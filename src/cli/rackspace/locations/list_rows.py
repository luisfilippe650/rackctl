from src.api.base_client import get
from src.utils.output import print_response

def list_locations_with_rows(_):
    response = get("/locations/rows")

    print_response(response)

def register_command_list_locations_rows(subparser):
    parser = subparser.add_parser(
        "list-rows",
        help="List locations with rows"
    )

    parser.set_defaults(func=list_locations_with_rows)