class BaseStep(object):
    def __init__(self, name, level, dependencies):
        self.id = id
        self.name = name
        self.dependencies = dependencies
        
    def run(self, job):
        raise NotImplementedError("run Method is not implemented for level %s" % (self.name) )