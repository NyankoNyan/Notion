from . import base


def stage(cause=None):
    node = base.Notion(name="stage")
    node.cause = cause
    return node


def collection(*args, **kwargs):
    return base.Notion(*args, **kwargs)


def instance(child, parent):
    notion = base.Notion(chapter="proto")
    notion.child = child
    notion.parent = parent