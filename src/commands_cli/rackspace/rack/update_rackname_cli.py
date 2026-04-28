from src.api.rackspace.rack_client import patch

def patch_racks(args):

    route = f"/racks/{args.rack_id}"

    data = {
        "name": args.rack_name
    }

    response = patch(route,data)

    print("Status:", response.status_code)
    print("Response:", response.text)

def register_command_patch_rows(subparser):
    patch_rows_parser = subparser.add_parser(
        "rename",
        help="rename row"
    )

    patch_rows_parser.add_argument(
        "rack_id",
        type=int,
        help="rack id for alter name"
    )

    patch_rows_parser.add_argument(
        "rack_name",
        type=str,
        help="rack name"
    )

    patch_rows_parser.set_defaults(func=patch_racks)