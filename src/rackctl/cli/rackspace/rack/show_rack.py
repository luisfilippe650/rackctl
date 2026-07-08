from rackctl.api.base_client import get
from rackctl.cli.common import add_id_or_name_arguments, resolve_rack_id
from rackctl.utils.output import print_response

def get_rack_details(args):
    rack_id = resolve_rack_id(args)
    route = f"/racks/{rack_id}"

    response = get(route)

    print_response(response)

def register_command_show_rack(subparser):
    parser = subparser.add_parser(
        "show",
        help="Show details of a rack"
    )

    add_id_or_name_arguments(parser, id_help="Rack ID", name_help="Rack name")

    parser.set_defaults(func=get_rack_details)
