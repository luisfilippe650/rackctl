from src.api.objects.objects_client import post

def create_object(args):
    route = "/objects"

    data = {
        "name": args.name,
        "objtype_id": args.objtype_id
    }

    response = post(route, data)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_create_object(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new object"
    )

    parser.add_argument(
        "name",
        type=str,
        help="Object name"
    )

    parser.add_argument(
        "objtype_id",
        type=int,
        help="Object type ID"
    )

    parser.set_defaults(func=create_object)