import sys
import requests


URL = "https://mail-sender.uber.aruhier.fr"


def send(*args, **kwargs):
    r = requests.post("{}/{}".format(URL.rstrip("/"), "send"), json=kwargs)
    if r.ok:
        print("Mail sent through {}".format(
            r.json()["provider_used"].title()
        ))
    elif r.status_code == 503:
        _print_error_status_by_provider(r.json())
        sys.exit(1)
    else:
        r.raise_for_status()


def check_addr(address):
    r = requests.get(
        "{}/{}/{}".format(URL.rstrip("/"), "validation", address),
    )
    if r.ok:
        for p in r.json()["providers"]:
            print("{}: {}".format(p["provider"].title(), p["validation"]))
    else:
        r.raise_for_status()


def validate(address):
    r = requests.post(
        "{}/{}/{}".format(URL.rstrip("/"), "validation", address),
    )
    if r.ok:
        print("Validation requested")
    elif r.status_code == 503:
        _print_error_status_by_provider(r.json())
        sys.exit(1)
    else:
        r.raise_for_status()


def _print_error_status_by_provider(json_data):
    for ps in json_data["providers"]:
        print(
            "{}: code {}, {}".format(
                ps["provider"], ps["status_code"], ps["msg"]
            ), file=sys.stderr
        )
