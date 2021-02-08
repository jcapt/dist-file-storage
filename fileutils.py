from uuid import uuid4

def gen_unique_filename(filename):
    uuid = str(uuid4())
    filename = filename + "." + uuid
    return (filename, uuid)

