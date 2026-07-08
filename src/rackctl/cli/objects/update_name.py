from rackctl.api.base_client import patch
from rackctl.cli.common import add_id_or_name_arguments, resolve_object_id
from rackctl.utils.output import print_response

def rename_object(args):
    object_id = resolve_object_id(args, name_attr="current_name")
    route = f"/objects/{object_id}"

    data = {}
    if args.name is not None:
        data["name"] = args.name
    if args.comment is not None:
        data["comment"] = args.comment

    response = patch(route, data)

    print_response(response)

def register_command_rename_object(subparser):
    parser = subparser.add_parser(
        "rename",
        help="Rename or update an object"
    )

    add_id_or_name_arguments(
        parser,
        name_flag="--current-name",
        name_dest="current_name",
        id_help="Object ID",
        name_help="Current object name"
    )
    parser.add_argument("--name", type=str, help="New object name")
    parser.add_argument("--comment", type=str, help="New object comment")

    parser.set_defaults(func=rename_object)
