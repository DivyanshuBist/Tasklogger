import click
from  cli.services import *

services:cliservices=None
@click.group()
def cli():
    global services
    services=cliservices()

@cli.command()
@click.argument('title')
def create(title:str):
    response:dict=services.createtask(title)
    if(response!=None and response["Error"]=='ok'):
        print("task added successfully")


@cli.command()
@click.argument('title')
def checkout(title:str):
    print(services.checkouttask(title))
    

@cli.command()
def status():
    print(services.current_status())


@cli.command()
def start():
    services.starttasklogging()

@cli.command()
def end():
    services.endtasklogging()


