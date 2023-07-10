import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/maria/Downloads"

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.scr_path} foi criado!")
    def on_deleted(self, event):
        print(f"Opa, alguém excluiu {event.scr_path}")
    


event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()