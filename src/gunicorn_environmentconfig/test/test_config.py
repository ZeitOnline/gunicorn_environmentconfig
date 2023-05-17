from unittest import mock
import gunicorn_environmentconfig
import os


def test_extracts_environment_variables_with_prefix():
    result = {}
    with mock.patch.dict(os.environ, {
            'gunicorn.one': 'value1',
            'gunicorn.two': 'value2',
            'unrelated': 'foobar'}):
        gunicorn_environmentconfig.apply(result)
    assert result == {'one': 'value1', 'two': 'value2'}


def test_evaluates_literal_values():
    result = {}
    with mock.patch.dict(os.environ, {'gunicorn.foo__literal__': '["1"]'}):
        gunicorn_environmentconfig.apply(result)
    assert result == {'foo': ["1"]}
