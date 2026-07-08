from rackctl.api.base_client import put
from rackctl.cli.common import resolve_location_id, resolve_row_id
from rackctl.utils.output import print_response

def add_location_to_row(args):
    row_id = resolve_row_id(args, id_attr="row", name_attr="row_name")
    location_id = resolve_location_id(args, id_attr="location", name_attr="location_name")
    route = f"/rows/{row_id}/{location_id}"

    response = put(route)

    print_response(response)

def register_command_add_location_to_row(subparser):
    parser = subparser.add_parser(
        "add-location",
        help="Add location to row"
    )

    row_group = parser.add_mutually_exclusive_group(required=True)
    row_group.add_argument("--row", type=int, help="Row ID")
    row_group.add_argument("--row-name", type=str, help="Row name")

    location_group = parser.add_mutually_exclusive_group(required=True)
    location_group.add_argument("--location", type=int, help="Location ID")
    location_group.add_argument("--location-name", type=str, help="Location name")

    parser.set_defaults(func=add_location_to_row)
