"""This module is used to drive different usecases for the workflow manager
"""
from executors.utils import get_executor
from job import Job
from workflow.ecommerce.schema import EcommerceWorkflow

executor = get_executor('LocalExecutor', 'FileSystemBackend')

def create_a_job():
    workflow = EcommerceWorkflow()
    job = Job(workflow, 'LocalExecutor', 'FileSystemBackend', workflow.root)
    executor.save_job(job)
    return job.id
    
def pickup(job_id):
    job = executor.get_job(job_id)
    
def schedule(job_id):
    job = executor.get_job(job_id)
    
def mark_successful(job_id):
    job = executor.get_job(job_id)
    job.data['nextStep'] = 'SuccessfulDelivery'
    executor.save_job(job)
    
def mark_customernotreachable(job_id):
    job = executor.get_job(job_id)
    job.data['nextStep'] = 'SuccessfulDelivery'
    executor.save_job(job)
    
if __name__ == '__main__':
    import sys
    step = int(sys.argv[1])
    if step == 0:
        print create_a_job()
    if step == 1:
        schedule(sys.argv[2])
    if step == 2:
        mark_successful(sys.argv[2])
    if step == 3:
        mark_customernotreachable(sys.argv[2])