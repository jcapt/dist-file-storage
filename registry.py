import requests
import os
import json

REGISTRY_VOLUME_URL = "http://localhost:3001"

class FileRegistry():
    def __init__(self):
        self.session = requests.Session()

    def register(self, entity_id, filename, metadata={}):
        return self.session.put(self.file_path(entity_id, filename), data=json.dumps(metadata))

    def deregister(self, entity_id, filename):
        return self.session.delete(self.file_path(entity_id, filename))

    def get_file_metadata(self, entity_id, filename):
        return self.session.get(self.file_path(entity_id, filename)).text

    def file_path(self, entity_id, filename):
        return os.path.join(REGISTRY_VOLUME_URL, entity_id, filename)

