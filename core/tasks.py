import os
import time
from queue import Queue
from threading import Thread

from job.models import JobInfo


que = Queue()


class Dispatcher:

    def __init__(self, job_id=None, file=None):
        self.job_id = job_id
        self.file = file

    def push(self):
        t = Thread(target=Tasks.product,
                   args=(que, self.job_id, self.file))
        t.setDaemon(True)
        t.start()

    def pop(self):
        t = Thread(target=Tasks.consume,
                   args=(que, ))
        t.setDaemon(True)
        t.start()


class Tasks:

    @staticmethod
    def product(que, job_id, file):
        """生成任务
        """
        que.put((job_id, file))

    @staticmethod
    def consume(que):
        """执行任务
        """
        while True:
            job_id, file = que.get()
            print(job_id, file)
            (JobInfo.objects.filter(is_deleted=False,
                                    job_id=job_id)
                            .update(status=1))

            Tasks.task(job_id, file)

            time.sleep(2)

    @staticmethod
    def task(job_id, file):
        print('--1--')
        os.system("python3 " + file)
        print("--2--")
        (JobInfo.objects.filter(is_deleted=False,
                                job_id=job_id)
                        .update(status=2))
