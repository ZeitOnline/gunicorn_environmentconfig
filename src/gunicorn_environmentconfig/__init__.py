from ast import literal_eval
import os


__version__ = '1.0.0.dev0'


def apply(cfg):
    environ = {}
    environ.update(os.environ)

    for key, value in environ.items():
        if not key.startswith('gunicorn.'):
            continue
        key = key.replace('gunicorn.', '', 1)
        if '__literal__' in key:
            key = key.replace('__literal__', '')
            value = literal_eval(value)
        cfg[key] = value
