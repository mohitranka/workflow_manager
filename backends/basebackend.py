from utils import State
class BaseBackend(object):
    def get_active_jobs(self):
        output = {}
        jobs = self.get_jobs()
        for job_id in jobs:
            job = jobs[job_id]
            if job.state in (State.INITIALIZED, State.RUNNING):
                output[job_id] = job
        return output