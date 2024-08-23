from abc import ABC, abstractmethod

class BaseDatosServices(ABC):

    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass

    @abstractmethod
    def select_all(self):
        pass

    @abstractmethod
    def select_by_id(self, intity_id):
        pass