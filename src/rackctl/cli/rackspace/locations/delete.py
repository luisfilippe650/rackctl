from rackctl.api.base_client import delete
from rackctl.cli.common import add_id_or_name_arguments, resolve_location_id
from rackctl.utils.output import print_response

def delete_location(args):
    location_id = resolve_location_id(args)
    route = f"/locations/{location_id}"

    response = delete(route)

    print_response(response)

def register_command_delete_location(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a location"
    )

    add_id_or_name_arguments(parser, id_help="Location ID", name_help="Location name")

    parser.set_defaults(func=delete_location)
