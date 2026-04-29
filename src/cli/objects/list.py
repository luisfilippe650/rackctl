from src.api.objects.objects_client import get

def list_objects(args):
    route = "/objects"

    response = get(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_list_objects(subparser):
    parser = subparser.add_parser(
        "list",
        help="List all objects"
    )

    parser.set_defaults(func=list_objects)