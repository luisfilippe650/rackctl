from src.api.rackspace.rack_client import get_single_occupancy


def get_rack_occupancy_single(args):
    route = f"/racks/{args.rack_id}/occupancy"

    response = get_single_occupancy(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_get_rack_single_occupancy(subparser):
    get_rack_single_occupancy_parser = subparser.add_parser(
        "occupancy",
        help="List single rack occupancy"
    )

    get_rack_single_occupancy_parser.add_argument(
        "rack_id",
        type=int,
        help="rack id for view occupancy"
    )

    get_rack_single_occupancy_parser.set_defaults(func=get_rack_occupancy_single)
