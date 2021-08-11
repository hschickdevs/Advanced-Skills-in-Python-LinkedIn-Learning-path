# basic contextmanager framework
from contextlib import contextmanager


@contextmanager
def simple_context_manager(obj):
    try:
        # do something
        yield
    finally:
        # wrap up
        pass
