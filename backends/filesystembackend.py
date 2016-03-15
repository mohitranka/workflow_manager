import os
import pickle
import settings
from basebackend import BaseBackend


class FileSystemBackend(BaseBackend):

    def __init__(self, file_name=settings.DEFAULT_FILESYSTEM_FILE):
        self.file_name = file_name
        # Create file if does not exists
        if not os.path.exists(file_name):
            f = open(file_name, 'wb')
            pickle.dump({},f)
            f.close()

    def save_job(self, job):
        data = {job.id: job}
        jobs = self.get_jobs()
        jobs.update(data)
        pickle.dump(jobs, open(self.file_name, 'wb'))

    def get_jobs(self):
        return pickle.load(open(self.file_name, 'rb'))
