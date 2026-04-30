from src.api.objects.objects_client import get_types
from src.utils.output import print_response

def list_object_types(_):
    route = "/objects/types"

    response = get_types(route)

    print_response(response)


def register_command_list_object_types(subparser):
    parser = subparser.add_parser(
        "types",
        help="List all object types"
    )

    parser.set_defaults(func=list_object_types)