from src.api.base_client import post
from src.utils.output import print_response

def create_object(args):
    route = "/objects"

    data = {
        "name": args.name,
        "obj-type_id": args.objtype_id
    }

    response = post(route, data)

    print_response(response)

def register_command_create_object(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new object"
    )

    parser.add_argument(
        "name",
        type=str,
        help="Object name"
    )

    parser.add_argument(
        "obj-type_id",
        type=int,
        help="Object type ID"
    )

    parser.set_defaults(func=create_object)