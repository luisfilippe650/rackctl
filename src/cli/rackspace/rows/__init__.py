from cli.rackspace.rows.list import register_command_list_rows
from cli.rackspace.rows.list_racks import register_command_list_rows_racks
from cli.rackspace.rows.create import register_command_create_rows
from cli.rackspace.rows.delete import register_command_delete_rows
from cli.rackspace.rows.add_location import register_command_add_location_to_row
from cli.rackspace.rows.remove_location import register_command_remove_location
from cli.rackspace.rows.update_name import register_command_update_name


def register_rows_commands(subparsers):
    rows_parser = subparsers.add_parser(
        "rows",
        help="Manage rows"
    )

    rows_sub = rows_parser.add_subparsers(
        dest="action",
        required=True
    )

    register_command_list_rows(rows_sub)
    register_command_list_rows_racks(rows_sub)
    register_command_create_rows(rows_sub)
    register_command_delete_rows(rows_sub)
    register_command_add_location_to_row(rows_sub)
    register_command_remove_location(rows_sub)
    register_command_update_name(rows_sub)