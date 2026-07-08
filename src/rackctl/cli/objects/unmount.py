from rackctl.api.base_client import delete
from rackctl.cli.common import add_id_or_name_arguments, resolve_object_id
from rackctl.utils.output import print_response

def unmount_object(args):
    object_id = resolve_object_id(args)
    route = f"/mount/{object_id}"

    response = delete(route)

    print_response(response)

def register_command_unmount_object(subparser):
    parser = subparser.add_parser(
        "unmount",
        help="Unmount object from rack"
    )

    add_id_or_name_arguments(parser, id_help="Object ID", name_help="Object name")

    parser.set_defaults(func=unmount_object)
