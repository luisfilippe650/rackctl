from rackctl.cli.objects import register_objects_commands
from rackctl.cli.rackspace.locations import register_locations_commands
from rackctl.cli.rackspace.rack import register_rack_commands
from rackctl.cli.rackspace.rows import register_rows_commands
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="rackctl",
        description="CLI for RackTables API"
    )

    subparsers = parser.add_subparsers(
        dest="resource",
        required=False
    )

    register_locations_commands(subparsers)
    register_rack_commands(subparsers)
    register_rows_commands(subparsers)
    register_objects_commands(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        print("\nRackCTL - CLI for RackTables")
        print("Use --help to see available commands\n")
        parser.print_help()


if __name__ == "__main__":
    main()