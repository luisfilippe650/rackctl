from rackctl.api.base_client import delete
from rackctl.utils.output import print_response

def delete_object(args):
    route = f"/objects/{args.id}"

    response = delete(route)

    print_response(response)

def register_command_delete_object(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete an object by ID"
    )

    parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="Object ID"
    )

    parser.set_defaults(func=delete_object)