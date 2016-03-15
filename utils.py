"""Utilities for workflow manager
"""
import importlib

def get_backend(_backend_class):
    """Returns the backend
    """
    backend = getattr(importlib.import_module('backends.%s' %
                                              (_backend_class.lower())), _backend_class)()
    return backend

def get_executor(_executor_class, _backend_class):
    """Returns the executor
    """
    backend = get_backend(_backend_class)
    executor = getattr(importlib.import_module('executors.%s' %
                                               (_executor_class.lower())), _executor_class)(backend)
    return executor
