#!/usr/bin/env python3

import sys
import argparse
from mail_sender_client.api_client import check_addr, send, validate


def parse_args():
    parser = argparse.ArgumentParser(
        description="Send mails through Mail Sender"
    )

    sp_action = parser.add_subparsers()
    _build_send_subparser(sp_action)
    _build_validation_subparser(sp_action)

    arg_parser = parser

    # Parse argument
    args = arg_parser.parse_args()

    # Execute correct function, or print usage
    if hasattr(args, "func"):
        args.func(parsed_args=args)
    else:
        arg_parser.print_help()
        sys.exit(1)


def _build_send_subparser(sp_action):
    sp_send = sp_action.add_parser("send", aliases=["s"], help=("send mail"))
    sp_send.add_argument(
        "-f", "--from", metavar="src", type=str,
        help=(
            "sender's name (address is chosen automatically by Mail Sender "
            "Daemon)"
        )
    )
    sp_send.add_argument(
        "-t", "--to", metavar="address", type=str, nargs="+",
        help="Receivers addresses", required=True
    )
    sp_send.add_argument(
        "-c", "--cc", metavar="address", type=str, nargs="*",
        help="Carbon Copy addresses"
    )
    sp_send.add_argument(
        "-b", "--bcc", metavar="address", type=str, nargs="*",
        help="blind carbon copy addresses"
    )
    sp_send.add_argument(
        "-r", "--reply_to", metavar="address", type=str, nargs="*",
        help="Reply-To addresses"
    )
    sp_send.add_argument("-s", "--subject", type=str, help="Subject")
    sp_send.add_argument("-T", "--text", type=str, help="Text content")
    sp_send.add_argument("-H", "--html", type=str, help="HTML content")

    sp_send.set_defaults(func=send_mail)
    return sp_send


def _build_validation_subparser(sp_action):
    sp_val = sp_action.add_parser(
        "valid", aliases=["v"], help=("email validation")
    )
    sp_val.add_argument(
        "-c", "--check", dest="check", action="store_true",
        help=("check an email validation status on all compatible providers")
    )
    sp_val.add_argument(
        "address", type=str, help=("email address")
    )

    sp_val.set_defaults(func=validation)
    return sp_val


def send_mail(parsed_args):
    args = ("from", "to", "cc", "bcc", "reply_to", "subject", "text", "html")
    params = {
        a: getattr(parsed_args, a) for a in args
        if getattr(parsed_args, a, None)
    }
    return send(**params)


def validation(parsed_args):
    address = parsed_args.address
    if parsed_args.check:
        return check_addr(address)
    else:
        return validate(address)


if __name__ == "__main__":
    parse_args()
