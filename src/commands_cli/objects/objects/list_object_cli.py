from src.api.objects.objects_client import get

def get_obj(args):
    route = "/objects"

    response = get(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_get_objects(subparser):
    get_objects_parser = subparser.add_parser(
        "list",
        help="List all objects"
    )

    get_objects_parser.set_defaults(func=get_obj)
