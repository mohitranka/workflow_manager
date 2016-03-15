import datetime
class BaseStep(object):

    def __init__(self, next_steps, dependencies):
        self.next_steps = next_steps
        self.dependencies = dependencies

    def run(self, job):
        raise NotImplementedError(
            "run Method is not implemented for level %s" % (self.name))

    def _is_executable(self, job):
        can_execute = set(job.completed_steps).intersection(
            set(self.dependencies)) == set(self.dependencies)
        can_execute = can_execute and datetime.datetime.utcnow() >= job.start_date
        return can_execute
