from src.api.base_client import delete
from src.utils.output import print_response

def unmount_object(args):
    route = f"/mount/{args.id}"

    response = delete(route)

    print_response(response)

def register_command_unmount_object(subparser):
    parser = subparser.add_parser(
        "unmount",
        help="Unmount object from rack"
    )

    parser.add_argument(
        "--id",
        type=int,
        help="Object ID"
    )

    parser.set_defaults(func=unmount_object)