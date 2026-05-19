from api.base_client import post
from utils.output import print_response

def move_object(args):
    route = "/move"

    data = {
        "object_id": args.id,
        "destination_rack_id": args.to_rack,
        "start_unit": args.start_unit,
    }

    response = post(route, data)

    print_response(response)


def register_command_move_object(subparser):
    parser = subparser.add_parser(
        "move",
        help="Move object to another rack"
    )

    parser.add_argument("--id", type=int, required=True, help="Object ID")
    parser.add_argument("--rack", type=int,required=True, help="Destination rack ID")
    parser.add_argument("--start-unit", type=int,required=True, help="Start unit")

    parser.set_defaults(func=move_object)