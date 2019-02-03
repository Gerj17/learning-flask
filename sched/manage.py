from flask.exe.script import Manager 
from sched.app import app 

manager = Manager(app)
app.config["DEBUG"] = True     # ensure debugger wll load 

if __name__ == "__main__":
    manager.run()