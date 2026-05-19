from api.base_client import post
from utils.output import print_response

def create_object(args):
    route = "/objects"

    data = {
        "name": args.name,
        "obj-type-id": args.type_id
    }

    response = post(route, data)

    print_response(response)

def register_command_create_object(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new object"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Object name"
    )

    parser.add_argument(
        "--type-id",
        type=int,
        required=True,
        help="Object type ID"
    )

    parser.set_defaults(func=create_object)