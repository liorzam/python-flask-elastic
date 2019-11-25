from abc import ABC, abstractmethod


class BaseESMigration(ABC):
    def __init__(self, es_object, es_index):
        self._es_object = es_object
        self.es_index = es_index

    @abstractmethod
    def execute(self):
        pass
