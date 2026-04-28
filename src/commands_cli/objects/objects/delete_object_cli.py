from src.api.objects.objects_client import delete

def delete_object(args):

    route = f"/objects/{args.obj_id}"

    response = delete(route)

    print("Status:", response.status_code)
    print("Response:", response.text)


def register_command_delete_objects(subparser):
    delete_objects_parser = subparser.add_parser(
        "delete",
        help="delete objects"
    )

    delete_objects_parser.add_argument(
        "obj_id",
        type=int,
        help="ID of object"
    )

    delete_objects_parser.set_defaults(func=delete_object)