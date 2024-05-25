from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)

    @abstractmethod
    def validate(self, value) -> None:
        ...
