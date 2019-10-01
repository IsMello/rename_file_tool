import os
import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('old_name')
@click.argument('new_name')


def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(os.listdir('.'))


if __name__ == '__main__':
    rename_file()



