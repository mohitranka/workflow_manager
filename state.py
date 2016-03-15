class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()
        
class State(object):
    INITIALIZED=0
    RUNNING=1
    SUCCESS=2
    FAILED=3
    COMPLETED=4
    
    @classmethod
    def _valid_states(_cls):
        return [getattr(_cls, name) for name in dir(_cls) if not name.startswith('_')]
        
    _valid_states = ClassProperty(_valid_states)
    
if __name__ == '__main__':
    print State._valid_states
    