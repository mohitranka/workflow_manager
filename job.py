"""
Module to manage Job class and its interface
"""
import datetime
import uuid
from state import State
from utils import get_executor

class Job(object):
    """
    class to manage Job (in memory) and its interface. Job is the realization of the
    workflow instance, in memory, which executor operations on.
    """
    def __init__(self, workflow, executor_class, backend_class, curr_step, data = {}, start_date=None, state=State.INITIALIZED, completed_steps=[]):
        self.id = str(uuid.uuid4())
        self.workflow = workflow
        self.executor_class = executor_class
        self.backend_class = backend_class
        self.start_date = start_date or datetime.datetime.utcnow()
        self.end_date = None
        self.state = state
        self.curr_step = curr_step
        self.data = data
        self.completed_steps = completed_steps

    def enqueue_job(job):
        executor = get_executor(job.executor_class, job.backend_class)
        executor.save_job(job)

    def update_state(self, new_state):
        assert new_state in State._valid_states
        self.state = new_state

    def finish(self):
        self.update_state(State.COMPLETED)
        self.end_date = datetime.datetime.utcnow()

    def clone(self, curr_step=None, data=None, start_date=None, state=None, completed_steps=None):
        if not curr_step:
            curr_step = self.curr_step
        if not data:
            data = self.data
        if not state:
            state = State.INITIALIZED
        if not completed_steps:
            completed_steps = self.completed_steps
        return Job(self.workflow, self.executor_class, self.backend_class, curr_step, data, start_date, state, completed_steps)

    def modify_data(self, new_data):
        self.data = new_data
