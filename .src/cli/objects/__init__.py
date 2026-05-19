from cli.objects.create import register_command_create_object
from cli.objects.delete import register_command_delete_object
from cli.objects.list import register_command_list_objects
from cli.objects.mount import register_command_mount_object
from cli.objects.move import register_command_move_object
from cli.objects.types import register_command_list_object_types
from cli.objects.unmount import (register_command_unmount_object)
from cli.objects.update_name import register_command_rename_object


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
    register_command_create_object(objects_sub)
    register_command_delete_object(objects_sub)
    register_command_rename_object(objects_sub)
    register_command_list_object_types(objects_sub)
    register_command_mount_object(objects_sub)
    register_command_unmount_object(objects_sub)
    register_command_move_object(objects_sub)