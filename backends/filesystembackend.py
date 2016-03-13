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
        pickle.dump(job, open(self.file_name, 'wb'))
        
    def get_job(self):
        try:
            return pickle.load(open(self.file_name, 'rb'))
        except:
            return None
        