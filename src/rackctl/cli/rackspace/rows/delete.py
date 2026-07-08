from rackctl.api.base_client import delete
from rackctl.cli.common import add_id_or_name_arguments, resolve_row_id
from rackctl.utils.output import print_response

def delete_row(args):
    row_id = resolve_row_id(args)
    route = f"/rows/{row_id}"

    response = delete(route)

    print_response(response)

def register_command_delete_rows(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete a row by ID"
    )

    add_id_or_name_arguments(parser, id_help="Row ID", name_help="Row name")

    parser.set_defaults(func=delete_row)
