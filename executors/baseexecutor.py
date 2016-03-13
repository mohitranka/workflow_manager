class BaseExecutor(object):
    pass

if __name__ == '__main__':
    #Use for factory method as well
    import settings
    import importlib
    _class = settings.DEFAULT_EXECUTOR
    executor = getattr(importlib.import_module('executors.%s' % (_class.lower())), _class)()
    executor.run()
