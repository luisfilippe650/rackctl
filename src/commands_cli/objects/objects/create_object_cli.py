from src.api.objects.objects_client import post

def add_object(args):

    route = "/objects"

    data = {
        "name": args.name,
        "objtype_id": args.obj_type
    }

    response = post(route,data)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_add_objects(subparser):
    add_objects_parser = subparser.add_parser(
        "add",
        help="Add objects"
    )

    add_objects_parser.add_argument(
        "object_name",
        type=str,
        help="object name"
    )

    add_objects_parser.add_argument(
        "obj_type",
        type=int,
        help="object type"
    )

    add_objects_parser.set_defaults(func=add_object)