from src.api.objects.objects_client import get_types


def list_object_types(args):
    route = "/objects/types"

    response = get_types(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_list_object_types(subparser):
    parser = subparser.add_parser(
        "types",
        help="List all object types"
    )

    parser.set_defaults(func=list_object_types)