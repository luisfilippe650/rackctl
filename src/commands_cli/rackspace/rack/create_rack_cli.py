from src.api.rackspace.rack_client import post

def add_rack(args):

    route = "/racks"

    data = {
        "name": args.name,
        "rack_height": args.height,
        "row_id": args.row_id
    }

    response = post(route,data)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_add_racks(subparser):
    add_rack_parser = subparser.add_parser(
        "add",
        help="Add row"
    )

    add_rack_parser.add_argument(
        "rack_name",
        type=str,
        help="rack name"
    )

    add_rack_parser.add_argument(
        "height",
        type=int,
        help="rack height"
    )
    add_rack_parser.add_argument(
        "row_id",
        type=int,
        help="row id"
    )

    add_rack_parser.set_defaults(func=add_rack)