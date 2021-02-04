import requests
import os

REGISTRY_VOLUME_URL = "http://localhost:3001"

class FileRegistry():
    def __init__(self):
        self.session = requests.Session()

    def register(self, entity_id, filename, metadata={}):
        return self.session.put(self.file_path(entity_id, filename))

    def deregister(self, entity_id, filename):
        return self.session.delete(self.file_path(entity_id, filename))

    def get_file_metadata(self, entity_id, filename):
        return self.session.get(self.file_path(entity_id, filename))

    def file_path(self, entity_id, filename):
        name = os.path.join(REGISTRY_VOLUME_URL, entity_id, filename)
        print(name)
        return name

