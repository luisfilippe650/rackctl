from rackctl.api.base_client import post
from rackctl.cli.common import resolve_object_id, resolve_rack_id
from rackctl.utils.output import print_response

def mount_object(args):
    route = "/mount/"
    rack_id = resolve_rack_id(args, id_attr="rack", name_attr="rack_name")
    object_id = resolve_object_id(args, id_attr="object_id", name_attr="object_name")

    data = {
        "rack_id": rack_id,
        "object_id": object_id,
        "start_unit": args.start_unit,
        "height": args.height
    }

    response = post(route, data)

    print_response(response)

def register_command_mount_object(subparser):
    parser = subparser.add_parser(
        "mount",
        help="Mount object into a rack"
    )

    rack_group = parser.add_mutually_exclusive_group(required=True)
    rack_group.add_argument("--id", "--rack", dest="rack", type=int, help="Rack ID")
    rack_group.add_argument("--rack-name", type=str, help="Rack name")

    object_group = parser.add_mutually_exclusive_group(required=True)
    object_group.add_argument("--object-id", type=int, help="Object ID")
    object_group.add_argument("--object-name", type=str, help="Object name")

    parser.add_argument("--start-unit", type=int, required=True, help="Start unit")
    parser.add_argument("--height", type=int, required=True, help="Object height")

    parser.set_defaults(func=mount_object)
