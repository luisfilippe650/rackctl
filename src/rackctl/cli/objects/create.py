from rackctl.api.base_client import post
from rackctl.utils.output import print_response

def create_object(args):
    route = "/objects/"

    data = {
        "name": args.name,
        "objtype_id": args.type_id,
        "label": args.label,
        "asset_no": args.asset_no,
        "comment": args.comment
    }

    response = post(route, data)

    print_response(response)

def register_command_create_object(subparser):
    parser = subparser.add_parser(
        "create",
        help="Create a new object"
    )

    parser.add_argument(
        "--name",
        type=str,
        required=True,
        help="Object name"
    )

    parser.add_argument(
        "--type-id",
        type=int,
        required=True,
        help="Object type ID"
    )
    parser.add_argument("--label", type=str, help="Object label")
    parser.add_argument("--asset-no", type=str, help="Object asset number/service tag")
    parser.add_argument("--comment", type=str, help="Object comment")

    parser.set_defaults(func=create_object)
