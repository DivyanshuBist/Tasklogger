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
    print(services.checkouttask(title)["Error"])
    

@cli.command()
def status():
    returnmap=services.current_status()
    print(f"current task:-{returnmap['task']}")
    print(f"current logging:-{returnmap['logging']}")



@cli.command()
def start():
    print(services.starttasklogging()["Error"])

@cli.command()
def end():
    print(services.endtasklogging()["Error"])


