from ..basestep import BaseStep

class PickOrderFromHub(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(PickOrderFromHub, self).__init__('PickOrderFromHub', next_steps, dependencies)
        
    def run(self, job):
        print "PickOrderFromHub for job - %s" %(job.id)
        
class ScheduleDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(ScheduleDelivery, self).__init__('ScheduleDelivery', next_steps, dependencies)
        
    def run(self, job):
        print "ScheduleDelivery for job - %s" %(job.id)

class ProcessDelivery(BaseStep):
    def __init__(self, level, dependencies):
        super(ProcessDelivery, self).__init__('ProcessDelivery', next_steps, dependencies)
        
    def run(self, job):
        print "ProcessDelivery for job - %s" %(job.id)
        
class SuccessfulDelivery(BaseStep):
    def __init__(self, level, dependencies):
        super(ScheduleDelivery, self).__init__('SuccessfulDelivery', next_steps, dependencies)
        
    def run(self):
        print "SuccessfulDelivery for job - %s " %(job.id)
        
class CustomerNotReachable(BaseStep):
    def __init__(self, level, dependencies):
        super(CustomerNotReachable, self).__init__('CustomerNotReachable', next_steps, dependencies)
    
    def run(self):
        print "CustomerNotReachable for job - %s " % (job.id)
        # Reenque the task to the queue.
        new_job = job.clone()
        new_job
        
class ReseduleDelivery(BaseStep):
    def __init__(self, next_steps, dependencies):
        super(ReseduleDelivery, self).__init__('ReseduleDelivery', next_steps, dependencies)
        