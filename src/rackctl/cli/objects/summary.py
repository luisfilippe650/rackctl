from rackctl.api.base_client import get
from rackctl.cli.common import add_id_or_name_arguments, resolve_object_id
from rackctl.utils.output import print_response


def get_object_summary(args):
    object_id = resolve_object_id(args)
    response = get(
        f"/summary/{object_id}",
        params={"include_options": args.include_options}
    )
    print_response(response)


def register_command_get_object_summary(subparser):
    parser = subparser.add_parser(
        "summary",
        help="Show an object's attributes"
    )

    add_id_or_name_arguments(parser, id_help="Object ID", name_help="Object name")
    parser.add_argument(
        "--include-options",
        action="store_true",
        help="Include dictionary options for select attributes"
    )
    parser.set_defaults(func=get_object_summary)
