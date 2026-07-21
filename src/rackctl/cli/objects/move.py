from rackctl.api.base_client import post
from rackctl.cli.common import resolve_object_id, resolve_rack_id
from rackctl.utils.output import print_response

def move_object(args):
    route = "/move/"
    object_id = resolve_object_id(args, id_attr="id", name_attr="name")
    destination_rack_id = resolve_rack_id(args, id_attr="rack", name_attr="rack_name")

    data = {
        "object_id": object_id,
        "destination_rack_id": destination_rack_id,
        "start_unit": args.start_unit,
        "source_rack_id": args.source_rack,
        "height": args.height
    }
    if args.source_rack_name is not None:
        data["source_rack_id"] = resolve_rack_id(args, id_attr="source_rack", name_attr="source_rack_name")

    response = post(route, data)

    print_response(response)


def register_command_move_object(subparser):
    parser = subparser.add_parser(
        "move",
        help="Move object to another rack"
    )

    object_group = parser.add_mutually_exclusive_group(required=True)
    object_group.add_argument("--id", type=int, help="Object ID")
    object_group.add_argument("--name", type=str, help="Object name")

    rack_group = parser.add_mutually_exclusive_group(required=True)
    rack_group.add_argument("--rack", type=int, help="Destination rack ID")
    rack_group.add_argument("--rack-name", type=str, help="Destination rack name")

    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument("--source-rack", type=int, help="Source rack ID")
    source_group.add_argument("--source-rack-name", type=str, help="Source rack name")

    parser.add_argument("--start-unit", type=int, required=True, help="Start unit")
    parser.add_argument("--height", type=int, help="Object height")

    parser.set_defaults(func=move_object)
