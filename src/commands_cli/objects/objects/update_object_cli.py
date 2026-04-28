from src.api.objects.objects_client import patch

def patch_obj(args):

    route = f"/objects/{args.obj_id}"

    data = {
        "name": args.obj_name
    }

    response = patch(route,data)

    print("Status:", response.status_code)
    print("Response:", response.text)

def register_command_patch_obj(subparser):
    patch_obj_parser = subparser.add_parser(
        "rename",
        help="rename object"
    )

    patch_obj_parser.add_argument(
        "obj_id",
        type=int,
        help="object id for alter name"
    )

    patch_obj_parser.add_argument(
        "obj_name",
        type=str,
        help="object name"
    )

    patch_obj_parser.set_defaults(func=patch_obj)