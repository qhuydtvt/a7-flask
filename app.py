from flask import Flask
import mlab
from models.task import Task
from flask_restful import Api
from resources.task_resource import *

mlab.connect()
app = Flask(__name__)
api = Api(app)

# for i in range(10):
#     task = Task(name="a7-{0}".format(i), local_id="`o2iu3o-{0}".format(i), done=False)
#     task.save()

# all_tasks = Task.objects()
# for task in all_tasks:
#     print(mlab.item2json(task))

# my_task = Task.objects(name="HuyMad_Quan xinh gai,ot cong").first()
# print(mlab.item2json((my_task)))

api.add_resource(TaskListRes, "/tasks")
api.add_resource(TaskRes, "/tasks/<task_id>")

if __name__ == '__main__':
    app.run()