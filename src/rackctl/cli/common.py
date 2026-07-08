from rackctl.api.base_client import get
from rackctl.utils.output import print_response


def add_pagination_arguments(parser):
    parser.add_argument("--page", type=int, default=1, help="Page number")
    parser.add_argument("--per-page", type=int, default=50, help="Items per page")


def pagination_params(args):
    return {
        "page": args.page,
        "per_page": args.per_page
    }


def resolve_resource_id(resource, name, id_keys):
    response = get(f"/{resource}/by-name", params={"name": name})
    if response.status_code >= 400:
        print_response(response)

    data = response.json().get("data", {})
    for key in id_keys:
        if key in data:
            return data[key]

    raise SystemExit(f"Unable to resolve {resource} ID from response.")


def resolve_location_id(args, id_attr="id", name_attr="name"):
    value = getattr(args, id_attr, None)
    if value is not None:
        return value
    return resolve_resource_id("locations", getattr(args, name_attr), ("location_id", "id"))


def resolve_row_id(args, id_attr="id", name_attr="name"):
    value = getattr(args, id_attr, None)
    if value is not None:
        return value
    return resolve_resource_id("rows", getattr(args, name_attr), ("row_id", "id"))


def resolve_rack_id(args, id_attr="id", name_attr="name"):
    value = getattr(args, id_attr, None)
    if value is not None:
        return value
    return resolve_resource_id("racks", getattr(args, name_attr), ("rack_id", "id"))


def resolve_object_id(args, id_attr="id", name_attr="name"):
    value = getattr(args, id_attr, None)
    if value is not None:
        return value
    return resolve_resource_id("objects", getattr(args, name_attr), ("object_id", "id"))


def add_id_or_name_arguments(
    parser,
    id_flag="--id",
    name_flag="--name",
    id_dest="id",
    name_dest="name",
    id_help="ID",
    name_help="Name"
):
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(id_flag, dest=id_dest, type=int, help=id_help)
    group.add_argument(name_flag, dest=name_dest, type=str, help=name_help)
