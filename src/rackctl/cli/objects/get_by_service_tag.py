from rackctl.api.base_client import get
from rackctl.utils.output import print_response


def get_object_by_service_tag(args):
    response = get("/objects/by-service-tag", params={"service_tag": args.service_tag})
    print_response(response)


def register_command_get_object_by_service_tag(subparser):
    parser = subparser.add_parser(
        "by-service-tag",
        help="Get an object by service tag"
    )

    parser.add_argument("--service-tag", type=str, required=True, help="Object service tag")
    parser.set_defaults(func=get_object_by_service_tag)
