from src.api.objects.objects_client import delete
from src.utils.output import print_response

def delete_object(args):
    route = f"/objects/{args.object_id}"

    response = delete(route)

    print_response(response)


def register_command_delete_object(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete an object by ID"
    )

    parser.add_argument(
        "object_id",
        type=int,
        help="Object ID"
    )

    parser.set_defaults(func=delete_object)