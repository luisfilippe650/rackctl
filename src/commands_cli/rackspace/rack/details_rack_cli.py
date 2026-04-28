from src.api.rackspace.rack_client import get_details


def get_rack_details(args):
    route = f"/racks/{args.rack_id}"

    response = get_details(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_get_racks(subparser):
    get_rack_details_parser = subparser.add_parser(
        "details",
        help="details single rack"
    )

    get_rack_details_parser.set_defaults(func=get_rack_details)
