import json
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'db.json')


class DB:
    @staticmethod
    def read():
        return json.loads(open(file_path, 'r').read())

    @staticmethod
    def write(db):
        return open(file_path, 'w').write(json.dumps(db))
