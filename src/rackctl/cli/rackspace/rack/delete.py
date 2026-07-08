from rackctl.api.base_client import delete
from rackctl.cli.common import add_id_or_name_arguments, resolve_rack_id
from rackctl.utils.output import print_response

def delete_rack(args):
    rack_id = resolve_rack_id(args)
    route = f"/racks/{rack_id}"

    response = delete(route)

    print_response(response)

def register_command_delete_rack(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a rack by ID"
    )

    add_id_or_name_arguments(parser, id_help="Rack ID", name_help="Rack name")

    parser.set_defaults(func=delete_rack)
