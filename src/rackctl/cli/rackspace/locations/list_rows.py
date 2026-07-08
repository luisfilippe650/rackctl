from rackctl.api.base_client import get
from rackctl.cli.common import add_pagination_arguments, pagination_params
from rackctl.utils.output import print_response

def list_locations_with_rows(args):
    response = get("/locations/rows", params=pagination_params(args))

    print_response(response)

def register_command_list_locations_rows(subparser):
    parser = subparser.add_parser(
        "list-rows",
        help="List locations with rows"
    )

    add_pagination_arguments(parser)

    parser.set_defaults(func=list_locations_with_rows)
