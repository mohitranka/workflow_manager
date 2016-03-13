from baseexecutor import BaseExecutor
import importlib
import settings

class LocalExecutor(BaseExecutor):
    def __init__(self):
        _class = settings.DEFAULT_BACKEND
        self.backend = getattr(importlib.import_module('backends.%s' % (_class.lower())), _class)()

    def run(self):
        job = self.backend.get_job()
        if job:
            # can execute the job?
            can_execute = set(job.completed_steps).intersection(set(job.curr_step.dependencies)) == set(job.curr_step.dependencies)
            if can_execute:
                curr_step = job.workflow.get_step(job.curr_step.id + 1)
                curr_step.run(job)
                job.curr_step = curr_step
            #Write the job back for processing in the future
            self.backend.save_job(job)
        else:
            print "Did not find any pending jobs"