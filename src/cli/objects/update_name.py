from src.api.base_client import patch
from src.utils.output import print_response

def rename_object(args):
    route = f"/objects/{args.object_id}"

    data = {
        "name": args.name
    }

    response = patch(route, data)

    print_response(response)

def register_command_rename_object(subparser):
    parser = subparser.add_parser(
        "rename",
        help="Rename an object"
    )

    parser.add_argument(
        "object_id",
        type=int,
        help="Object ID"
    )

    parser.add_argument(
        "name",
        type=str,
        help="New object name"
    )

    parser.set_defaults(func=rename_object)