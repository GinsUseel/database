import os
import json
import logging
from lightdb import LightDB

class dbuser:
    def __init__(self, filename):
        if not filename.endswith('.us'):
            self.logger.error('Error: Filename must end with ".us"')
            return None
        self.filename = filename
        self.db = LightDB(self.filename)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    @classmethod
    def create(cls, filename):
        return cls(filename)    
    
    def add(self, table, value):
        if table in self.db:
            self.logger.error(f'Error: Table "{table}" already exists')
        else:
            self.db[table] = value
            self.db.save()

    def set(self, table, new_value):
        if table in self.db:
            self.db[table] = new_value
            self.db.save()
        else:
            self.logger.error(f'Error: Table "{table}" not found')

    def get(self, table):
        if table in self.db:
            return self.db[table]
        else:
            return None

    def save(self):
        self.db.save()

    def rm(self, table):
        if table in self.db:
            del self.db[table]
        else:
            self.logger.error(f'Error: Table "{table}" not found')