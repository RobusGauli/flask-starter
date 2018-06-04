# -*- coding: utf-8 -*-
"""
    lib.config
    ~~~~~
    Exposes ConfigBase class that needs to subclassed by Config classes.
    It registers the class instance with the '__name__' being the key.
"""
from collections import defaultdict


class ConfigMetaType(type):
    """
        Metaclass for registering child class instances.
    """
    _config_registry = defaultdict(dict)
    # pylint: disable=bad-mcs-classmethod-argument

    def __new__(cls, clsname, bases, clsdict):
        _class_instance = super().__new__(cls, clsname, bases, clsdict)
        if '__name__' in clsdict:
            cls._config_registry[clsdict['__name__']] = _class_instance
        return _class_instance

    # pylint: disable=too-few-public-methods
    @classmethod
    def create_config(cls):
        """Returns config class instance registry"""
        return cls._config_registry

# pylint: disable=too-few-public-methods


class ConfigBase(metaclass=ConfigMetaType):
    """Base class whose metaclass is ConfigMetaType"""
    pass


__all__ = ['ConfigBase']
