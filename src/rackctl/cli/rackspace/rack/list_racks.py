from rackctl.api.base_client import get
from rackctl.cli.common import add_pagination_arguments, pagination_params
from rackctl.utils.output import print_response

def list_racks(args):
    route = "/racks/"

    response = get(route, params=pagination_params(args))

    print_response(response)

def register_command_list_racks(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all racks"
    )

    add_pagination_arguments(parser)

    parser.set_defaults(func=list_racks)
