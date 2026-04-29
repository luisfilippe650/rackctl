from src.api.objects.objects_client import delete

def delete_object(args):
    route = f"/objects/{args.object_id}"

    response = delete(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_delete_object(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete an object by ID"
    )

    parser.add_argument(
        "object_id",
        type=int,
        help="Object ID"
    )

    parser.set_defaults(func=delete_object)