from rackctl.api.base_client import get
from rackctl.cli.common import add_pagination_arguments, pagination_params
from rackctl.utils.output import print_response

def get_rows_racks(args):
    route = "/rows/racks"

    response = get(route, params=pagination_params(args))

    print_response(response)

def register_command_list_rows_racks(subparser):
    parser = subparser.add_parser(
        "list-racks",
        help="List all rows with racks"
    )

    add_pagination_arguments(parser)

    parser.set_defaults(func=get_rows_racks)
