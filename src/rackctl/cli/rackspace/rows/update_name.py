from rackctl.api.base_client import patch
from rackctl.cli.common import add_id_or_name_arguments, resolve_row_id
from rackctl.utils.output import print_response

def rename_row(args):
    row_id = resolve_row_id(args, name_attr="current_name")
    route = f"/rows/{row_id}"

    data = {
        "name": args.name
    }

    response = patch(route, data)

    print_response(response)

def register_command_update_name(subparser):
    parser = subparser.add_parser(
        "rename",
        help="Rename a row"
    )

    add_id_or_name_arguments(
        parser,
        name_flag="--current-name",
        name_dest="current_name",
        id_help="Row ID",
        name_help="Current row name"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="New row name"
    )

    parser.set_defaults(func=rename_row)
