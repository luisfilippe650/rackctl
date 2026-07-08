from rackctl.api.base_client import get
from rackctl.utils.output import print_response


def get_status(_):
    response = get("/status")
    print_response(response)


def register_status_command(subparsers):
    parser = subparsers.add_parser(
        "status",
        help="Check API and database status"
    )

    parser.set_defaults(func=get_status)
