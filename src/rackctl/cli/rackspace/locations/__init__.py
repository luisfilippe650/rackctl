from rackctl.cli.rackspace.locations.create import register_command_create_location
from rackctl.cli.rackspace.locations.delete import register_command_delete_location
from rackctl.cli.rackspace.locations.list import register_command_list_locations
from rackctl.cli.rackspace.locations.list_rows import register_command_list_locations_rows


def register_locations_commands(subparsers):
    locations_parser = subparsers.add_parser(
        "locations",
        help="Manage locations"
    )

    locations_sub = locations_parser.add_subparsers(
        dest="action",
        required=True
    )

    register_command_create_location(locations_sub)
    register_command_delete_location(locations_sub)
    register_command_list_locations(locations_sub)
    register_command_list_locations_rows(locations_sub)