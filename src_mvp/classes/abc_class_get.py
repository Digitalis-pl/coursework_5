from abc import ABC, abstractmethod


class Get(ABC):

    @abstractmethod
    def get_information(self):
        pass

    @abstractmethod
    def sort_info(self):
        pass
