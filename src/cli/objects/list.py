from src.api.objects.objects_client import get
from src.utils.output import print_response

def list_objects(_):
    route = "/objects"

    response = get(route)

    print_response(response)

def register_command_list_objects(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all objects"
    )

    parser.set_defaults(func=list_objects)