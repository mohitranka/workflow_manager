from state import State
class BaseBackend(object):
    def get_active_jobs(self):
        output = {}
        jobs = self.get_jobs()
        for job_id in jobs:
            job = jobs[job_id]
            if job.state in (State.INITIALIZED, State.RUNNING):
                output[job_id] = job
        return output
        
    def get_job(self, job_id):
        return self.get_jobs()[job_id]
        
    def save_job(self, job):
        raise NotImplementedError("Method save_job is not implemented")
        
    def get_jobs(self):
        raise NotImplementedError("Method get_jobs is not implemented")