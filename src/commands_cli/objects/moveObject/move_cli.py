from src.api.objects.moveObjects_client import post

def move(args):

    route = "/move"

    data = {
        "object_id": args.obj_id,
        "source_rack_id": args.rack_origin_id,
        "destination_rack_id": args.rack_destination_id,
        "start_unit": args.start_unit,
        "height": args.height
    }

    response = post(route,data)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_move(subparser):
    move_parser = subparser.add_parser(
        "move",
        help="move objects in other rack"
    )

    move_parser.add_argument(
        "obj_id",
        type=int,
        help="id object"
    )

    move_parser.add_argument(
        "rack_origin_id",
        type=int,
        help="rack where the object is allocated"
    )

    move_parser.add_argument(
        "rack_destination_id",
        type=int,
        help="rack where the object will be allocated"
    )

    move_parser.add_argument(
        "start_unit",
        type=int,
        help="initial unit for allocation"
    )

    move_parser.add_argument(
        "height",
        type=int,
        help="size of allocation units"
    )

    move_parser.set_defaults(func=move)