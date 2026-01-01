# Иерархия для системы заказа репродукции.
# Она реализует наследование вида так как предметы искусства могут быть разных типов: картины, скульптуры, ювелирные украшения и т.д.
# Они имеют разные этапы создания и возможные действия над ними, но в также могут иметь общие методы, которые их объединяют.
# Но также предметы искусства могут быть защещены авторским правом или наоборот не защищены. И в зависимости от авторского права будут
# выполненые разные подготовильные этапы или проверки возможности законно создать репродукцию.
from abc import ABC, abstractmethod


class Reproduction:

    def __itni__(self, art_type: "PieceOfArt", copyright_type: "Copyright"):
        self._art_type: PieceOfArt = art_type
        self._copyright_type: Copyright = copyright

    def make_art(self):
        if self._copyright_type.check_legitimacy():
            self._art_type.create()


class PieceOfArt(ABC):

    @abstractmethod
    def create(self):
        pass


class Jewelry(PieceOfArt):

    def __init__(self):
        self._material = None
        self._gem = None

    def create(self):
        print("Create Jewelry")


class Photo(PieceOfArt):

    def __init__(self):
        self._image = None

    def create(self):
        print("Create Photo")


class Copyright(ABC):

    @abstractmethod
    def check_legitimacy(self) -> bool:
        pass


class FreeToUse(Copyright):

    def check_legitimacy(self) -> bool:
        return True


class ProtectedByLaw(Copyright):

    def check_legitimacy(self) -> bool:
        return False
