from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from MarshalApp import create_app, db

app = create_app()
Migrate(app,db)
manager = Manager(app)
manager.add_command("nicedb",MigrateCommand)


if __name__ == '__main__':
    manager.run()