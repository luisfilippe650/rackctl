from rackctl.api.base_client import post
from rackctl.cli.common import resolve_row_id
from rackctl.utils.output import print_response

def create_rack(args):
    route = "/racks"
    row_id = resolve_row_id(args, id_attr="row", name_attr="row_name")

    data = {
        "name": args.name,
        "rack_height": args.height,
        "row_id": row_id,
        "asset_no": args.asset_no
    }

    response = post(route, data)

    print_response(response)

def register_command_create_rack(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a rack"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Rack name"
    )

    parser.add_argument(
        "--height",
        type=int,
        default=42,
        help="Rack height"
    )

    row_group = parser.add_mutually_exclusive_group(required=True)
    row_group.add_argument("--row", type=int, help="Row ID")
    row_group.add_argument("--row-name", type=str, help="Row name")

    parser.add_argument("--asset-no", type=str, help="Rack asset number")

    parser.set_defaults(func=create_rack)
