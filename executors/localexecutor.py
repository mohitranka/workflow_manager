from baseexecutor import BaseExecutor
import importlib
import settings
import datetime

class LocalExecutor(BaseExecutor):
    def __init__(self):
        _class = settings.DEFAULT_BACKEND
        self.backend = getattr(importlib.import_module('backends.%s' % (_class.lower())), _class)()

    def run(self):
        jobs = self.backend.get_active_jobs()
        for job_id in jobs:
            # can execute the job?
            job = jobs[job_id]
            can_execute = set(job.completed_steps).intersection(set(job.curr_step.dependencies)) == set(job.curr_step.dependencies)
            can_execute = can_execute and datetime.datetime.utcnow() >= job.start_date
            if can_execute:
                job.completed_steps.append(job.curr_step.level)
                job.curr_step.run(job)
            #Write the job back for processing in the future
            self.backend.save_job(job)
        else:
            print "Did not find any pending jobs"