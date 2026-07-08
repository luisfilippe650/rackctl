from rackctl.api.base_client import get
from rackctl.cli.common import add_pagination_arguments, pagination_params
from rackctl.utils.output import print_response


def get_dictionary(args):
    response = get(f"/dictionary/{args.chapter_id}", params=pagination_params(args))
    print_response(response)


def register_command_get_dictionary(subparser):
    parser = subparser.add_parser(
        "dictionary",
        help="List dictionary options for a chapter"
    )

    parser.add_argument("--chapter-id", type=int, required=True, help="Dictionary chapter ID")
    add_pagination_arguments(parser)
    parser.set_defaults(func=get_dictionary)
