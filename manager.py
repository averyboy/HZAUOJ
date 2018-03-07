import os
from app import create_app,db
from app.models import User,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app=create_app('default')
manager=Manager(app)
migrate=Migrate(app,db)

def make_all_context():
    return dict(app=app,db=db,User=User,Role=Role)
manager.add_commmand('shell',Shell(make_context=make_all_context))
migrate.add_commmand('db',MigrateCommand)

if __name__=='__main__':
    manager.run()