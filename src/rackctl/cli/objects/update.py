from rackctl.api.base_client import patch
from rackctl.cli.common import add_id_or_name_arguments, resolve_object_id
from rackctl.utils.output import print_response

def update_object(args):
    object_id = resolve_object_id(args, name_attr="current_name")
    updates = {}

    for assignment in args.set_values:
        if "=" not in assignment:
            raise SystemExit(f"Invalid --set value '{assignment}'; expected FIELD=VALUE.")
        field, value = assignment.split("=", 1)
        field = field.strip()
        if not field:
            raise SystemExit("The field name in --set cannot be empty.")
        updates[field] = value

    for field in args.clear:
        updates[field] = {"clear": True}

    if not updates:
        raise SystemExit("Provide at least one --set or --clear option.")

    response = patch(f"/summary/{object_id}", updates)
    print_response(response)


def register_command_update_object(subparser):
    parser = subparser.add_parser(
        "update",
        help="Update fixed fields or dynamic attributes of an object"
    )

    add_id_or_name_arguments(
        parser,
        name_flag="--current-name",
        name_dest="current_name",
        id_help="Object ID",
        name_help="Current object name"
    )
    parser.add_argument(
        "--set",
        dest="set_values",
        action="append",
        default=[],
        metavar="FIELD=VALUE",
        help="Set a field or attribute; may be repeated"
    )
    parser.add_argument(
        "--clear",
        action="append",
        default=[],
        metavar="ATTRIBUTE",
        help="Clear a dynamic attribute; may be repeated"
    )
    parser.set_defaults(func=update_object)
