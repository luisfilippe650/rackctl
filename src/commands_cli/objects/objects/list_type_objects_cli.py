from src.api.objects.objects_client import get_types

def get_obj_types(args):
    route = "/objects/types"

    response = get_types(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_get_objects_types(subparser):
    get_objects_types_parser = subparser.add_parser(
        "types",
        help="List all objects types"
    )

    get_objects_types_parser.set_defaults(func=get_obj_types)
