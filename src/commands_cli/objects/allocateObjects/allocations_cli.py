from src.api.objects.allocateObjects_client import post

def allocate(args):

    route = "/allocations"

    data = {
        "rack_id": args.rack_id,
        "object_id": args.object_id,
        "start_unit": args.start_unit,
        "height": args.height
    }

    response = post(route,data)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_allocate(subparser):
    allocate_parser = subparser.add_parser(
        "allocate",
        help="allocate object at rack"
    )

    allocate_parser.add_argument(
        "rack_id",
        type=int,
        help="rack id"
    )

    allocate_parser.add_argument(
        "object_id",
        type=int,
        help="object id"
    )

    allocate_parser.add_argument(
        "start_unit",
        type=int,
        help="initial unit for allocation"
    )

    allocate_parser.add_argument(
        "height",
        type=int,
        help="size of allocation units"
    )

    allocate_parser.set_defaults(func=allocate)