from src.db.db_driver import DB
from src.utils.url import UrlUtils


class ProjectsData:
    @staticmethod
    def get(project_name):
        db = DB.read()
        projects = db['projects']
        return projects.get(project_name)

    @staticmethod
    def add(url):
        db = DB.read()
        projects = db['projects']

        name = UrlUtils.name(url)
        print(name)

        projects[name] = {
            'url': url,
        }

        DB.write(db)

    @staticmethod
    def all():
        db = DB.read()
        projects = db['projects']
        return projects
