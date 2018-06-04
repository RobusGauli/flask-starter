from collections import defaultdict

class ConfigMetaType(type):
    _config_registry = defaultdict(dict)

    def __new__(cls, clsname, bases, clsdict):
        _class_instance = super().__new__(cls, clsname, bases, clsdict)
        if '__name__' in clsdict:
            cls._config_registry[clsdict['__name__']] = _class_instance
        return _class_instance

    @classmethod
    def create_config(cls):
        return cls._config_registry

class ConfigBase(metaclass=ConfigMetaType):
    pass

__all__ = ['ConfigBase']
