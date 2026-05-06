from src.api.base_client import post
from src.utils.output import print_response

def move_object(args):
    route = "/move"

    data = {
        "object_id": args.id,
        "source_rack_id": args.from_rack,
        "destination_rack_id": args.to_rack,
        "start_unit": args.start_unit,
        "height": args.height
    }

    response = post(route, data)

    print_response(response)


def register_command_move_object(subparser):
    parser = subparser.add_parser(
        "move",
        help="Move object to another rack"
    )

    parser.add_argument("--id", type=int, required=True, help="Object ID")
    parser.add_argument("--from-rack", type=int,required=True, help="Source rack ID")
    parser.add_argument("--to-rack", type=int,required=True, help="Destination rack ID")
    parser.add_argument("--start-unit", type=int,required=True, help="Start unit")
    parser.add_argument("--height", type=int,required=True, help="Object height")

    parser.set_defaults(func=move_object)