import os
from time import sleep
from rich.console import Console

console = Console()
tasks = [f"task {n}" for n in range(1, 5)]

with console.status("[bold green]Working on the files...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
print("File loading and initializing....") 
os.system('python burning_Memory.py')
