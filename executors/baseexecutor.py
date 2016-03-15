"""
"""
import settings
from ..utils import get_executor


class BaseExecutor(object):
    """
    """

    def __init__(self, backend):
        self.backend = backend

    def save_job(self, job):
        self.backend.save_job(job)

    def start(self):
        raise NotImplementedError(
            "start method is not implemented for the executor %s" % self.__class__.__name__)

    def run(self):
        raise NotImplementedError(
            "run method is not implemented for the executor %s" % self.__class__.__name__)

    def shutdown(self):
        raise NotImplementedError(
            "shutdown method is not implemented for the executor %s" % self.__class__.__name__)

if __name__ == '__main__':
    executor = get_executor(settings.DEFAULT_EXECUTOR,
                            settings.DEFAULT_BACKEND)
    executor.start()
    executor.run()