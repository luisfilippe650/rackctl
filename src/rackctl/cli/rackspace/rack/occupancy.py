from rackctl.api.base_client import get
from rackctl.cli.common import add_pagination_arguments, pagination_params
from rackctl.utils.output import print_response

def list_rack_occupancy(args):
    route = "/racks/occupancy"
    params = pagination_params(args)
    params["include_objects"] = args.include_objects

    response = get(route, params=params)

    print_response(response)

def register_command_racks_occupancy(subparser):
    parser = subparser.add_parser(
        "occupancy",
        help="List racks with occupancy"
    )

    add_pagination_arguments(parser)
    parser.add_argument("--include-objects", action="store_true", help="Include allocated objects")

    parser.set_defaults(func=list_rack_occupancy)
