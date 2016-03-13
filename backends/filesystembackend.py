import os
import pickle
import settings
from basebackend import BaseBackend

class FileSystemBackend(BaseBackend):
    def __init__(self, file_name = settings.DEFAULT_FILESYSTEM_FILE):
        self.file_name = file_name
        # Create file if does not exists
        if not os.path.exists(file_name):
            f = open(file_name, 'a+')
            f.close()
    
    def save_job(self, job):
        data = {job.id: job}
        jobs = self.get_jobs()
        jobs.update(data)
        pickle.dump(jobs, open(self.file_name, 'wb'))
        
    def get_job(self, id):
        return self.get_jobs[id]
        
    def get_jobs(self):
        try:
            return pickle.load(open(self.file_name, 'rb'))
        except:
            return {}
        