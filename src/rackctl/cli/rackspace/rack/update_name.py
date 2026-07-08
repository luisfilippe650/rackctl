from rackctl.api.base_client import patch
from rackctl.cli.common import add_id_or_name_arguments, resolve_rack_id
from rackctl.utils.output import print_response

def rename_rack(args):
    rack_id = resolve_rack_id(args, name_attr="current_name")
    route = f"/racks/{rack_id}"

    data = {
        "name": args.name
    }

    response = patch(route, data)

    print_response(response)

def register_command_rename_rack(subparser):
    parser = subparser.add_parser(
        "rename",
        help="Rename a rack"
    )

    add_id_or_name_arguments(
        parser,
        name_flag="--current-name",
        name_dest="current_name",
        id_help="Rack ID",
        name_help="Current rack name"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="New rack name"
    )

    parser.set_defaults(func=rename_rack)
