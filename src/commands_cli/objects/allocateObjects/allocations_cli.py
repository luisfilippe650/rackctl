from api.requests_api.client import post




def register(subparsers):
    parser = subparsers.add_parser("alocar")

    parser.add_argument("--rack-id", type=int, required=True)
    parser.add_argument("--object-id", type=int, required=True)
    parser.add_argument("--unit-no", type=int, required=True)

    parser.set_defaults(func=allocation_object)