from src.api.objects.allocateObjects_client import delete

def unallocated(args):

    route = f"/allocations/{args.object_id}"

    response = delete(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_unallocated(subparser):
    unallocated_parser = subparser.add_parser(
        "unallocated",
        help="unallocated object at rack"
    )

    unallocated_parser.add_argument(
        "rack_id",
        type=int,
        help="rack id"
    )

    unallocated_parser.set_defaults(func=unallocated)