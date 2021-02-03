import requests

REGISTRY_VOLUME_URL = "http://localhost:3001"

class FileRegistry():
    def __init__(self):
        self.session = requests.Session()

    def register(self, entity_id, filename, metadata={}):
        return self.session.put(REGISTRY_VOLUME_URL + "/" + entity_id + "/" + filename, data=metadata)

    def deregister(self, entity_id, filename):
        return self.session.delete(REGISTRY_VOLUME_URL +"/"+entity_id + "/" + filename) 

    def get_file_metadata(self, path, filename):
        return self.session.get(REGISTRY_VOLUME_URL + "/" + entity_id + "/" + filename)

