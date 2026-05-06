from src.api.base_client import post
from src.utils.output import print_response

def mount_object(args):
    route = "/mount"

    data = {
        "rack_id": args.id,
        "object_id": args.object_id,
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

    parser.add_argument("--id", type=int,required=True, help="Rack ID")
    parser.add_argument("--object-id", type=int,required=True, help="Object ID")
    parser.add_argument("--start-unit", type=int,required=True, help="Start unit")
    parser.add_argument("--height", type=int,required=True, help="Object height")

    parser.set_defaults(func=mount_object)