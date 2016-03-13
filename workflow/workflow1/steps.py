from basestep import BaseStep

class Step1(BaseStep):
    def run(self, job):
        print "Running Step1 for job - %s" %(job.id)

class Step2(BaseStep):
    def run(self, job):
        print "Running Step2 for job - %s" %(job.id)
        
