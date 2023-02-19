#!/usr/bin/env python3
from jinja2 import Environment, PackageLoader
import argparse
import getpass
from .grouped_iterator import grouped_iterator
import exifread
import os
import sys


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Bootstrap Gallery Generator")
    parser.add_argument("files", metavar="FILES", nargs="*")
    parser.add_argument("-T", "--template", default="gallery.jinja2.html")
    parser.add_argument("-t", "--title", default="Gallery")
    parser.add_argument("-a", "--author", default=getpass.getuser())
    parser.add_argument("-p", "--thumbnail-prefix")
    parser.add_argument(
        "-o",
        "--output",
        default="index.html",
        type=argparse.FileType("w", encoding="utf-8"),
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    environment = Environment(loader=PackageLoader("bootstrap_gallery_generator"))
    template = environment.get_template(args.template)
    dictionary = {
        "author": args.author,
        "title": args.title,
        "rows": grouped_iterator(args.files, 4),
        "allfiles": args.files
    }
    if args.thumbnail_prefix:
        dictionary["prefix"] = args.thumbnail_prefix
    args.output.write(template.render(dictionary))


if __name__ == "__main__":
    main()
