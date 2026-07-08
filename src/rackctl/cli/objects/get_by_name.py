from rackctl.api.base_client import get
from rackctl.utils.output import print_response


def get_object_by_name(args):
    response = get("/objects/by-name", params={"name": args.name})
    print_response(response)


def register_command_get_object_by_name(subparser):
    parser = subparser.add_parser(
        "by-name",
        help="Get an object by name"
    )

    parser.add_argument("--name", type=str, required=True, help="Object name")
    parser.set_defaults(func=get_object_by_name)
