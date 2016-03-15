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
            job.curr_step = job.workflow.flow['ScheduleDelivery']
        except Exception, e:
            print "Error while processing PickOrderFromHub for job - %s" %(job.id)
            job.state = State.FAILED
        finally:
            job.save()
        
class ScheduleDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(ScheduleDelivery, self).__init__(next_steps, dependencies)
        
    def run(self, job):
        try:
            print "ScheduleDelivery for job - %s" %(job.id)
            job.curr_step = job.workflow.flow['ProcessDelivery']
        except Exception, e:
            print e
            print "Error while processing ScheduleDelivery for job - %s" %(job.id)
            job.state = State.FAILED
        finally:
            job.save()

class ProcessDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(ProcessDelivery, self).__init__(next_steps, dependencies)
        
    def run(self, job):
        try:
            print "ProcessDelivery for job - %s" %(job.id)
            job.curr_step = job.workflow.flow[job.data['nextStep']] 
        except:
            print "Error while processing 'ProcessDelivery' for job - %s" %(job.id)
            job.state = State.FAILED
        finally:
            job.save()
        
class SuccessfulDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(SuccessfulDelivery, self).__init__(next_steps, dependencies)
        
    def run(self, job):
        try:
            print "SuccessfulDelivery for job - %s " %(job.id)
            job.curr_step = None
        except:
            print "Error while processing 'ProcessDelivery' for job - %s" %(job.id)
            job.state = State.FAILED
        finally:
            job.save()
        
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
            print "Error while processing 'ProcessDelivery' for job - %s" %(job.id)
            job.state = State.FAILED
        finally:
            job.save()
            
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
            print "Error while processing 'ProcessDelivery' for job - %s" %(job.id)
            job.state = State.FAILED
        finally:
            job.save()
