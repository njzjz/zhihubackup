import argparse

from .backup import loop as backup_zhihu


def main():
    # zhihubackup <username>
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()
    backup_zhihu(args.username)
