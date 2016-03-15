from baseexecutor import BaseExecutor
import importlib
import settings
import datetime
from state import State

class LocalExecutor(BaseExecutor):

    def __init__(self, backend):
        self.jobs = []
        super(LocalExecutor, self).__init__(backend)

    def start(self):
        self.jobs = self.backend.get_active_jobs() # To make sure we do not pick any Failed jobs

    def run(self):
        for job_id in self.jobs:
            job = jobs[job_id]
            if not job.next_steps:
                # Check if we should run the job
                job.finish()
            else:
                curr_step = job.curr_step
                if curr_step._is_executable(job):
                    # can execute the job?
                    step_name = curr_step.__class__.__name__
                    curr_step.run(job) # the job's curr step gets modified here.
                    job.completed_steps.append(step_name)
                    if job.next_steps:
                        job.state = State.RUNNING
            # Write the job back for processing in the future
            self.backend.save_job(job)
        else:
            print "Did not find any pending jobs"

    def shutdown(self):
        print "Shutthing down the localexecutor"
