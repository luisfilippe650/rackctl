from cli.rackspace.rack.create import register_command_create_rack
from cli.rackspace.rack.delete import register_command_delete_rack
from cli.rackspace.rack.list_racks import register_command_list_racks
from cli.rackspace.rack.occupancy import register_command_racks_occupancy
from cli.rackspace.rack.show_occupancy import register_command_show_rack_occupancy
from cli.rackspace.rack.show_rack import register_command_show_rack
from cli.rackspace.rack.update_name import register_command_rename_rack


def register_rack_commands(subparsers):
    rack_parser = subparsers.add_parser(
        "racks",
        help="Manage racks"
    )

    rack_sub = rack_parser.add_subparsers(
        dest="action",
        required=True
    )

    register_command_list_racks(rack_sub)
    register_command_create_rack(rack_sub)
    register_command_delete_rack(rack_sub)
    register_command_rename_rack(rack_sub)
    register_command_show_rack(rack_sub)
    register_command_racks_occupancy(rack_sub)
    register_command_show_rack_occupancy(rack_sub)