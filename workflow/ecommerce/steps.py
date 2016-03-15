import importlib
import datetime
from state import State
from ..basestep import BaseStep

class PickOrderFromHub(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(PickOrderFromHub, self).__init__(next_steps, dependencies)
        
    def run(self, job):
        try:
            print "PickOrderFromHub for job - %s" %(job.id)
            job.curr_step = job.workflow['ScheduleDelivery']
        except:
            job.state = State.FAILED
        
class ScheduleDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(ScheduleDelivery, self).__init__(next_steps, dependencies)
        
    def run(self, job):
        try:
            print "ScheduleDelivery for job - %s" %(job.id)
            job.curr_step = job.workflow['ProcessDelivery']
        except:
            job.state = State.FAILED

class ProcessDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(ProcessDelivery, self).__init__(next_steps, dependencies)
        
    def run(self, job):
        try:
            print "ProcessDelivery for job - %s" %(job.id)
            job.curr_step = job.workflow[job.data['nextStep']] 
        except:
            job.state = State.FAILED
        
class SuccessfulDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(SuccessfulDelivery, self).__init__(next_steps, dependencies)
        
    def run(self, job):
        try:
            print "SuccessfulDelivery for job - %s " %(job.id)
            job.curr_step = None
        except:
            job.state = State.FAILED
        
class CustomerNotReachable(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(CustomerNotReachable, self).__init__(next_steps, dependencies)
    
    def run(self, job):
        try:
            print "CustomerNotReachable for job - %s " % (job.id)
            # Reenque the task to the queue.
            new_job = job.clone(start_date=job.start_date + datetime.timedelta(days=1))
            job.enqueue_job(new_job)
            print "Enqueued new_job %s for execution later" % (new_job.id)
            job.curr_step = None
        except:
            job.state = State.FAILED
            
class ReseduleDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(ReseduleDelivery, self).__init__(next_steps, dependencies)
    
    def run(self, job):
        try:
            print "ReseduleDelivery for job - %s " % (job.id)
            new_job = job.clone(start_date=job.data['scheduled_delivery_date'])
            job.enqueue_job(new_job)
            print "Job rescheduled for delivery by the customer. ID: " %(new_job.id)
            job.curr_step = None
        except:
            job.state = State.FAILED