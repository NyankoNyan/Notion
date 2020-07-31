from . import base

def stage(cause=None):
    node = base.Node(name="stage", chapter="proto")
    node.cause = cause
    return node

def collection(*args, **kwargs):
    return base.Node(*args, **kwargs)