from rackctl.api.base_client import get
from rackctl.cli.common import add_id_or_name_arguments, resolve_rack_id
from rackctl.utils.output import print_response

def show_rack_occupancy(args):
    rack_id = resolve_rack_id(args)
    route = f"/racks/{rack_id}/occupancy"

    response = get(route, params={"include_objects": args.include_objects})

    print_response(response)

def register_command_show_rack_occupancy(subparser):
    parser = subparser.add_parser(
        "show-occupancy",
        help="Show occupancy of a single rack"
    )

    add_id_or_name_arguments(parser, id_help="Rack ID", name_help="Rack name")
    parser.add_argument("--include-objects", action="store_true", help="Include allocated objects")

    parser.set_defaults(func=show_rack_occupancy)
