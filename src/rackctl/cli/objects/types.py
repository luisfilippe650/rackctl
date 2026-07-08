from rackctl.api.base_client import get
from rackctl.cli.common import add_pagination_arguments, pagination_params
from rackctl.utils.output import print_response

def list_object_types(args):
    route = "/objects/types"

    response = get(route, params=pagination_params(args))

    print_response(response)

def register_command_list_object_types(subparser):
    parser = subparser.add_parser(
        "types",
        help="List all object types"
    )

    add_pagination_arguments(parser)

    parser.set_defaults(func=list_object_types)
