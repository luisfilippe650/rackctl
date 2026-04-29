from src.api.objects.mount_unmount_client import delete

def unmount_object(args):
    route = f"/allocations/{args.object_id}"

    response = delete(route)

    print("Status:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)


def register_command_unmount_object(subparser):
    parser = subparser.add_parser(
        "unmount",
        help="Unmount object from rack"
    )

    parser.add_argument(
        "object_id",
        type=int,
        help="Object ID"
    )

    parser.set_defaults(func=unmount_object)