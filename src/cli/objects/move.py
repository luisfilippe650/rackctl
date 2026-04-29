from src.api.objects.move_client import post

def move_object(args):
    route = "/move"

    data = {
        "object_id": args.object_id,
        "source_rack_id": args.source_rack_id,
        "destination_rack_id": args.destination_rack_id,
        "start_unit": args.start_unit,
        "height": args.height
    }

    response = post(route, data)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_move_object(subparser):
    parser = subparser.add_parser(
        "move",
        help="Move object to another rack"
    )

    parser.add_argument("object_id", type=int, help="Object ID")
    parser.add_argument("source_rack_id", type=int, help="Source rack ID")
    parser.add_argument("destination_rack_id", type=int, help="Destination rack ID")
    parser.add_argument("start_unit", type=int, help="Start unit")
    parser.add_argument("height", type=int, help="Object height")

    parser.set_defaults(func=move_object)