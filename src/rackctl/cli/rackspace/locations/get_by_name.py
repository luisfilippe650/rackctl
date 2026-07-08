from rackctl.api.base_client import get
from rackctl.utils.output import print_response


def get_location_by_name(args):
    response = get("/locations/by-name", params={"name": args.name})
    print_response(response)


def register_command_get_location_by_name(subparser):
    parser = subparser.add_parser(
        "by-name",
        help="Get a location by name"
    )

    parser.add_argument("--name", type=str, required=True, help="Location name")
    parser.set_defaults(func=get_location_by_name)
