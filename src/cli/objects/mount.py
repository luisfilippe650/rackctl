from src.api.objects.mount_unmount_client import post

def mount_object(args):
    route = "/allocations"

    data = {
        "rack_id": args.rack_id,
        "object_id": args.object_id,
        "start_unit": args.start_unit,
        "height": args.height
    }

    response = post(route, data)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_mount_object(subparser):
    parser = subparser.add_parser(
        "mount",
        help="Mount object into a rack"
    )

    parser.add_argument("rack_id", type=int, help="Rack ID")
    parser.add_argument("object_id", type=int, help="Object ID")
    parser.add_argument("start_unit", type=int, help="Start unit")
    parser.add_argument("height", type=int, help="Object height")

    parser.set_defaults(func=mount_object)