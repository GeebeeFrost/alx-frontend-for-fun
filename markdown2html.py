#!/usr/bin/python3
"""This script takes 2 arguments: a markdown file and an html file."""
import sys
import os


def markdown2html():
    """Reads a markdown file and writes it to an html file."""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    markdown2html()
