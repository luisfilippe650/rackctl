import argparse
from src.cli.objects import register_objects_commands
from src.cli.rackspace.locations import register_locations_commands
from src.cli.rackspace.rack import register_rack_commands
from src.cli.rackspace.rows import register_rows_commands


def main():
    parser = argparse.ArgumentParser(
        prog="rackctl",
        description="CLI for RackTables API"
    )

    subparsers = parser.add_subparsers(
        dest="resource",
        required=True
    )

    register_locations_commands(subparsers)
    register_rack_commands(subparsers)
    register_rows_commands(subparsers)
    register_objects_commands(subparsers)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()