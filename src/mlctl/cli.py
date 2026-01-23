import argparse
import logging
import sys
from mlctl import __version__

try:
    import argcomplete
except ImportError:
    argcomplete = None
    

# --------------------------------------------------
# Logging setup
# --------------------------------------------------

def setup_logging(verbose: bool):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )


# --------------------------------------------------
# Handlers
# --------------------------------------------------

def model_train(args):
    logging.info("Starting model training")
    print(f"Training model '{args.name}' for {args.epochs} epochs")
    print(f"Using dataset: {args.dataset}")


def model_deploy(args):
    logging.info("Deploying model")
    print(f"Deploying model '{args.name}' to environment '{args.env}'")


def model_list(args):
    print("Available models:")
    print("- churn_v1")
    print("- credit_risk_v2")


def data_ingest(args):
    logging.info("Ingesting data")
    print(f"Ingesting data from source: {args.source}")
    print(f"Format: {args.format}")


def data_validate(args):
    print(f"Validating dataset '{args.dataset}'")
    print("Validation successful ✅")


# --------------------------------------------------
# CLI Builder
# --------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Machine Learning Platform Control CLI"
    )

    # Global flags
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    parser.add_argument(
        "--config",
        help="Path to config file",
    )
    
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # --------------------------------------------------
    # model commands
    # --------------------------------------------------

    model_parser = subparsers.add_parser("model", help="Model operations")
    model_sub = model_parser.add_subparsers(dest="model_command", required=True)

    # model train
    train_parser = model_sub.add_parser("train", help="Train a model")
    train_parser.add_argument("--name", required=True, help="Model name")
    train_parser.add_argument("--dataset", required=True, help="Dataset name")
    train_parser.add_argument("--epochs", type=int, default=5, help="Number of epochs")
    train_parser.set_defaults(func=model_train)

    # model deploy
    deploy_parser = model_sub.add_parser("deploy", help="Deploy a model")
    deploy_parser.add_argument("--name", required=True, help="Model name")
    deploy_parser.add_argument(
        "--env",
        choices=["dev", "staging", "prod"],
        required=True,
        help="Deployment environment",
    )
    deploy_parser.set_defaults(func=model_deploy)

    # model list
    list_parser = model_sub.add_parser("list", help="List models")
    list_parser.set_defaults(func=model_list)

    # alias: model ls
    ls_parser = model_sub.add_parser("ls", help="Alias for list")
    ls_parser.set_defaults(func=model_list)

    # --------------------------------------------------
    # data commands
    # --------------------------------------------------

    data_parser = subparsers.add_parser("data", help="Data operations")
    data_sub = data_parser.add_subparsers(dest="data_command", required=True)

    # data ingest
    ingest_parser = data_sub.add_parser("ingest", help="Ingest data")
    ingest_parser.add_argument("--source", required=True, help="Data source")
    ingest_parser.add_argument(
        "--format",
        choices=["csv", "json", "parquet"],
        default="csv",
        help="Data format",
    )
    ingest_parser.set_defaults(func=data_ingest)

    # data validate
    validate_parser = data_sub.add_parser("validate", help="Validate dataset")
    validate_parser.add_argument("--dataset", required=True, help="Dataset name")
    validate_parser.set_defaults(func=data_validate)

    return parser


# --------------------------------------------------
# Entrypoint
# --------------------------------------------------

def main():
    parser = build_parser()
    
    if argcomplete is not None:
        argcomplete.autocomplete(parser)
    
    args = parser.parse_args()
    
    setup_logging(args.verbose)

    if args.config:
        logging.info(f"Using config file: {args.config}")

    # Dispatch command
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
