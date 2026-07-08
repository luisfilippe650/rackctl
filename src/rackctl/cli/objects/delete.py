from rackctl.api.base_client import delete
from rackctl.cli.common import add_id_or_name_arguments, resolve_object_id
from rackctl.utils.output import print_response

def delete_object(args):
    object_id = resolve_object_id(args)
    route = f"/objects/{object_id}"

    response = delete(route)

    print_response(response)

def register_command_delete_object(subparser):
    parser = subparser.add_parser(
        "delete",
        help="Delete an object by ID"
    )

    add_id_or_name_arguments(parser, id_help="Object ID", name_help="Object name")

    parser.set_defaults(func=delete_object)
