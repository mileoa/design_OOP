import math
from abc import ABC, abstractmethod
from typing import Sequence


class PointATD(ABC):

    @abstractmethod
    def __init__(self, x: float, y: float):
        """'
        Создает точку с координатами (x, y)
        """
        pass

    # Запросы
    @property
    @abstractmethod
    def x(self) -> float:
        """
        Возвращает координату x
        """
        pass

    @property
    @abstractmethod
    def y(self) -> float:
        """
        Возвращает координату y
        """
        pass

    @abstractmethod
    def distance(self, point: "PointATD") -> float:
        """
        Возвращает расстояние до указанной точки
        """
        pass


class ShapeATD(ABC):

    @abstractmethod
    def __init__(self):
        """
        Постусловие: Создает фигуру
        """
        pass

    # Запросы
    @abstractmethod
    def area(self) -> float:
        """
        Возвращает площадь фигуры
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Возвращает периметр фигуры
        """
        pass


class ShapeWithCenterATD(ShapeATD):

    # Запросы
    @property
    @abstractmethod
    def center(self) -> PointATD:
        """
        Возвращает центр фигуры
        """
        pass


class CircleATD(ShapeWithCenterATD):

    @abstractmethod
    def __init__(self, center: PointATD, radius: float):
        """
        Предусловие: радиус не может быть отрицательными
        Постусловие: Создает круг заданного радиуса с центром в заданной точке
        """
        pass

    # Запросы
    @abstractmethod
    def radius(self) -> float:
        """
        Возвращает радиус
        """
        pass


class PolygonATD(ShapeATD):

    @abstractmethod
    def __init__(self, vertexes: Sequence[PointATD]):
        """
        Предусловие: многоугольник содержит минимум 3 вершины
        Постусловие: Создает многоугольник с вершинами в указанных
        точках по порядку
        """
        pass


# Наследование, множественное наследование
class RectangleATD(ShapeWithCenterATD, PolygonATD):

    @abstractmethod
    def __init__(self, vertexes: Sequence[PointATD]):
        """
        Предусловие: должно быть 4 вершины. Углы между всеми прямыми,
        которые проведены между последовательными вершинами должны
        составлять 90 градусов.
        Постусловие: создан прямоугольник
        """
        pass


# Наследование
class SquareATD(RectangleATD):

    @abstractmethod
    def __init__(self, vertexes: Sequence[PointATD]):
        """
        Предусловие: должно быть 4 вершины. Углы между всеми прямыми,
        которые проведены между последовательными вершинами должны
        составлять 90 градусов. Все прямые должно быть одной длинны.
        Постусловие: создан квадрат
        """
        pass


class Point(PointATD):
    def __init__(self, x: float, y: float):
        self._x: float = x
        self._y: float = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def distance(self, point: PointATD) -> float:
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Circle(CircleATD):

    def __init__(self, center: Point, radius: float):
        self._center: Point = center  # Композиция
        self._radius: float = radius

    def area(self) -> float:
        return math.pi * (self._radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius


class Polygon(PolygonATD):

    def __init__(self, vertexes: Sequence[PointATD]):
        if len(vertexes) < 3:
            raise ValueError("Amount of vertexes can't be less than 3")
        self._vertexes: Sequence[PointATD] = vertexes  # Композиция

    def area(self) -> float:
        vertexes_amount: int = len(self._vertexes)
        result: float = 0.0
        for i in range(vertexes_amount):
            x1, y1 = self._vertexes[i].x, self._vertexes[i].y
            x2, y2 = (
                self._vertexes[(i + 1) % vertexes_amount].x,
                self._vertexes[(i + 1) % vertexes_amount].y,
            )
            result += x1 * y2 - x2 * y1
        return abs(result) / 2

    def perimeter(self) -> float:
        result: float = 0.0
        vertexes_amount: int = len(self._vertexes)
        for i in range(vertexes_amount):
            result += self._vertexes[i].distance(
                self._vertexes[(i + 1) % vertexes_amount]
            )
        return result


# Наследование, полиморфизм
class Rectangle(RectangleATD, Polygon):

    def __init__(self, vertexes: Sequence[PointATD]):
        if len(vertexes) != 4:
            raise ValueError("Rectangle must contain 4 vertexes")
        if not self._is_corners_valid(vertexes):
            raise ValueError(
                "Rectangle must have all corners equal 90 degrees",
            )
        self._vertexes: Sequence[PointATD] = vertexes  # Композиция
        self._center: PointATD = self._calculate_center(
            self._vertexes[0], self._vertexes[2]
        )  # Композиция

    @property
    def center(self) -> PointATD:
        return self._center

    def _is_corners_valid(self, vertexes: Sequence[PointATD]) -> bool:
        """
        Проверяет, что все углы прямоугольника равны 90 градусам.

        Использует скалярное произведение векторов:
        если скалярное произведение двух векторов равно 0,
        то угол между ними составляет 90 градусов.
        """
        for i in range(4):
            prev_point = vertexes[(i - 1) % 4]
            current_point = vertexes[i]
            next_point = vertexes[(i + 1) % 4]

            vector1 = (
                prev_point.x - current_point.x,
                prev_point.y - current_point.y,
            )
            vector2 = (
                next_point.x - current_point.x,
                next_point.y - current_point.y,
            )

            dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

            if abs(dot_product) > 0:
                return False

        return True

    def _calculate_center(
        self, left_up_point: PointATD, right_bottom_point: PointATD
    ) -> PointATD:
        return Point(
            (left_up_point.x + right_bottom_point.x) / 2,
            (left_up_point.y + right_bottom_point.y) / 2,
        )


# Наследование, полиморфизм
class Square(Rectangle, SquareATD):

    def __init__(self, vertexes: Sequence[PointATD]):
        if len(vertexes) != 4:
            raise ValueError("Rectangle must contain 4 vertexes")
        if not self._is_corners_valid(vertexes):
            raise ValueError(
                "Rectangle must have all corners equal 90 degrees",
            )
        if not self._is_length_valid(vertexes):
            raise ValueError(
                "Square must have all sides equal",
            )
        self._vertexes: Sequence[PointATD] = vertexes  # Композиция
        self._center: PointATD = self._calculate_center(
            self._vertexes[0], self._vertexes[2]
        )  # Композиция

    def _is_length_valid(self, vertexes: Sequence[PointATD]) -> bool:
        sides_length: list[float] = []
        vertexes_amount: int = len(vertexes)
        for i in range(vertexes_amount):
            sides_length.append(
                vertexes[i].distance(vertexes[(i + 1) % vertexes_amount])
            )

        for i in range(1, vertexes_amount):
            if sides_length[0] != sides_length[i]:
                return False
        return True
