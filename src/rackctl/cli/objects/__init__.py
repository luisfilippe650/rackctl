from rackctl.cli.objects.create import register_command_create_object
from rackctl.cli.objects.delete import register_command_delete_object
from rackctl.cli.objects.dictionary import register_command_get_dictionary
from rackctl.cli.objects.get_by_name import register_command_get_object_by_name
from rackctl.cli.objects.get_by_service_tag import register_command_get_object_by_service_tag
from rackctl.cli.objects.list import (
    register_command_list_all_objects,
    register_command_list_objects,
)
from rackctl.cli.objects.mount import register_command_mount_object
from rackctl.cli.objects.move import register_command_move_object
from rackctl.cli.objects.types import register_command_list_object_types
from rackctl.cli.objects.unmount import (register_command_unmount_object)
from rackctl.cli.objects.update_name import register_command_rename_object
from rackctl.cli.objects.summary import register_command_get_object_summary
from rackctl.cli.objects.update import register_command_update_object


def register_objects_commands(subparsers):
    objects_parser = subparsers.add_parser(
        "objects",
        help="Manage objects"
    )

    objects_sub = objects_parser.add_subparsers(
        dest="action",
        required=True
    )

    register_command_list_objects(objects_sub)
    register_command_list_all_objects(objects_sub)
    register_command_create_object(objects_sub)
    register_command_delete_object(objects_sub)
    register_command_get_dictionary(objects_sub)
    register_command_get_object_by_name(objects_sub)
    register_command_get_object_by_service_tag(objects_sub)
    register_command_rename_object(objects_sub)
    register_command_update_object(objects_sub)
    register_command_get_object_summary(objects_sub)
    register_command_list_object_types(objects_sub)
    register_command_mount_object(objects_sub)
    register_command_unmount_object(objects_sub)
    register_command_move_object(objects_sub)
