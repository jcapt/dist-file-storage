from uuid import uuid4

def gen_unique_filename(filename):
    return filename + "." + str(uuid4())

