import math
import unittest

from result import Circle, Point, Polygon, Rectangle, Square


class TestPoint(unittest.TestCase):
    """Тесты для класса Point"""

    def setUp(self):
        """Создание тестовых точек"""
        self.point1 = Point(0, 0)
        self.point2 = Point(3, 4)
        self.point3 = Point(-1, -1)
        self.point4 = Point(3.5, 2.5)

    def test_point_creation(self):
        """Тест создания точки"""
        self.assertIsNotNone(self.point1)
        self.assertIsNotNone(self.point2)

    def test_point_x_coordinate(self):
        """Тест получения координаты X"""
        self.assertEqual(self.point1.x, 0)
        self.assertEqual(self.point2.x, 3)
        self.assertEqual(self.point3.x, -1)
        self.assertEqual(self.point4.x, 3.5)

    def test_point_y_coordinate(self):
        """Тест получения координаты Y"""
        self.assertEqual(self.point1.y, 0)
        self.assertEqual(self.point2.y, 4)
        self.assertEqual(self.point3.y, -1)
        self.assertEqual(self.point4.y, 2.5)

    def test_distance_same_point(self):
        """Тест расстояния между одинаковыми точками"""
        distance = self.point1.distance(self.point1)
        self.assertEqual(distance, 0)

    def test_distance_positive_coordinates(self):
        """Тест расстояния между точками с положительными координатами"""
        distance = self.point1.distance(self.point2)
        expected_distance = 5  # sqrt(3^2 + 4^2) = 5
        self.assertAlmostEqual(distance, expected_distance, places=7)

    def test_distance_negative_coordinates(self):
        """Тест расстояния между точками с отрицательными координатами"""
        distance = self.point1.distance(self.point3)
        expected_distance = math.sqrt(2)  # sqrt(1^2 + 1^2)
        self.assertAlmostEqual(distance, expected_distance, places=7)

    def test_distance_symmetry(self):
        """Тест симметричности расстояния"""
        distance1 = self.point1.distance(self.point2)
        distance2 = self.point2.distance(self.point1)
        self.assertAlmostEqual(distance1, distance2, places=7)

    def test_distance_with_float_coordinates(self):
        """Тест расстояния между точками с дробными координатами"""
        distance = self.point4.distance(self.point1)
        expected_distance = math.sqrt(3.5**2 + 2.5**2)
        self.assertAlmostEqual(distance, expected_distance, places=7)


class TestCircle(unittest.TestCase):
    """Тесты для класса Circle"""

    def setUp(self):
        """Создание тестовых кругов"""
        self.center = Point(0, 0)
        self.center2 = Point(1, 1)
        self.circle1 = Circle(self.center, 5)
        self.circle2 = Circle(self.center2, 2)
        self.circle3 = Circle(Point(0, 0), 0.5)

    def test_circle_creation(self):
        """Тест создания круга"""
        self.assertIsNotNone(self.circle1)

    def test_circle_center(self):
        """Тест получения центра круга"""
        center = self.circle1.center
        self.assertEqual(center.x, self.center.x)
        self.assertEqual(center.y, self.center.y)

    def test_circle_radius(self):
        """Тест получения радиуса"""
        self.assertEqual(self.circle1.radius, 5)
        self.assertEqual(self.circle2.radius, 2)
        self.assertEqual(self.circle3.radius, 0.5)

    def test_circle_area(self):
        """Тест вычисления площади круга"""
        area1 = self.circle1.area()
        expected_area1 = math.pi * 5**2
        self.assertAlmostEqual(area1, expected_area1, places=7)

        area2 = self.circle2.area()
        expected_area2 = math.pi * 2**2
        self.assertAlmostEqual(area2, expected_area2, places=7)

    def test_circle_perimeter(self):
        """Тест вычисления периметра (длины окружности)"""
        perimeter1 = self.circle1.perimeter()
        expected_perimeter1 = 2 * math.pi * 5
        self.assertAlmostEqual(perimeter1, expected_perimeter1, places=7)

        perimeter2 = self.circle2.perimeter()
        expected_perimeter2 = 2 * math.pi * 2
        self.assertAlmostEqual(perimeter2, expected_perimeter2, places=7)

    def test_circle_area_radius_relationship(self):
        """Тест связи между площадью и радиусом"""
        radius = 3
        circle = Circle(self.center, radius)
        area = circle.area()
        expected_area = math.pi * radius**2
        self.assertAlmostEqual(area, expected_area, places=7)

    def test_circle_with_different_centers(self):
        """Тест кругов с разными центрами"""
        circle1 = Circle(Point(0, 0), 3)
        circle2 = Circle(Point(5, 5), 3)

        self.assertAlmostEqual(circle1.area(), circle2.area(), places=7)
        self.assertAlmostEqual(
            circle1.perimeter(), circle2.perimeter(), places=7
        )


class TestPolygon(unittest.TestCase):
    """Тесты для класса Polygon (треугольник)"""

    def setUp(self):
        """Создание тестовых многоугольников"""
        # Треугольник со сторонами 3, 4, 5 (прямоугольный)
        self.triangle = Polygon([Point(0, 0), Point(3, 0), Point(0, 4)])

        # Квадрат со стороной 2
        self.square_polygon = Polygon(
            [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        )

    def test_polygon_creation(self):
        """Тест создания многоугольника"""
        self.assertIsNotNone(self.triangle)

    def test_triangle_area(self):
        """Тест площади треугольника"""
        area = self.triangle.area()
        expected_area = 6  # (3 * 4) / 2 = 6
        self.assertAlmostEqual(area, expected_area, places=7)

    def test_triangle_perimeter(self):
        """Тест периметра треугольника"""
        perimeter = self.triangle.perimeter()
        expected_perimeter = 3 + 4 + 5  # 12
        self.assertAlmostEqual(perimeter, expected_perimeter, places=7)

    def test_square_polygon_area(self):
        """Тест площади квадрата как многоугольника"""
        area = self.square_polygon.area()
        expected_area = 4  # 2 * 2
        self.assertAlmostEqual(area, expected_area, places=7)

    def test_square_polygon_perimeter(self):
        """Тест периметра квадрата как многоугольника"""
        perimeter = self.square_polygon.perimeter()
        expected_perimeter = 8  # 2 + 2 + 2 + 2
        self.assertAlmostEqual(perimeter, expected_perimeter, places=7)

    def test_polygon_positive_area(self):
        """Тест что площадь многоугольника положительная"""
        area = self.triangle.area()
        self.assertGreater(area, 0)


class TestRectangle(unittest.TestCase):
    """Тесты для класса Rectangle"""

    def setUp(self):
        """Создание тестовых прямоугольников"""
        # Прямоугольник 3x4
        self.rect1 = Rectangle(
            [Point(0, 0), Point(3, 0), Point(3, 4), Point(0, 4)]
        )

        # Прямоугольник 2x5
        self.rect2 = Rectangle(
            [Point(0, 0), Point(2, 0), Point(2, 5), Point(0, 5)]
        )

    def test_rectangle_creation(self):
        """Тест создания прямоугольника"""
        self.assertIsNotNone(self.rect1)

    def test_rectangle_area(self):
        """Тест площади прямоугольника"""
        area1 = self.rect1.area()
        expected_area1 = 12  # 3 * 4
        self.assertAlmostEqual(area1, expected_area1, places=7)

        area2 = self.rect2.area()
        expected_area2 = 10  # 2 * 5
        self.assertAlmostEqual(area2, expected_area2, places=7)

    def test_rectangle_perimeter(self):
        """Тест периметра прямоугольника"""
        perimeter1 = self.rect1.perimeter()
        expected_perimeter1 = 14  # 2 * (3 + 4)
        self.assertAlmostEqual(perimeter1, expected_perimeter1, places=7)

        perimeter2 = self.rect2.perimeter()
        expected_perimeter2 = 14  # 2 * (2 + 5)
        self.assertAlmostEqual(perimeter2, expected_perimeter2, places=7)

    def test_rectangle_center(self):
        """Тест получения центра прямоугольника"""
        center = self.rect1.center
        self.assertEqual(center.x, 1.5)
        self.assertEqual(center.y, 2)

        center2 = self.rect2.center
        self.assertEqual(center2.x, 1)
        self.assertEqual(center2.y, 2.5)

    def test_rectangle_is_polygon(self):
        """Тест что прямоугольник является многоугольником"""
        self.assertIsInstance(self.rect1, Polygon)

    def test_rectangle_centered_at_origin(self):
        """Тест прямоугольника с центром в начале координат"""
        rect = Rectangle(
            [
                Point(-1, -1),
                Point(1, -1),
                Point(1, 1),
                Point(-1, 1),
            ]
        )
        center = rect.center
        self.assertEqual(center.x, 0)
        self.assertEqual(center.y, 0)


class TestSquare(unittest.TestCase):
    """Тесты для класса Square"""

    def setUp(self):
        """Создание тестовых квадратов"""
        # Квадрат со стороной 3
        self.square1 = Square(
            [Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3)]
        )

        # Квадрат со стороной 5
        self.square2 = Square(
            [Point(0, 0), Point(5, 0), Point(5, 5), Point(0, 5)]
        )

    def test_square_creation(self):
        """Тест создания квадрата"""
        self.assertIsNotNone(self.square1)

    def test_square_area(self):
        """Тест площади квадрата"""
        area1 = self.square1.area()
        expected_area1 = 9  # 3 * 3
        self.assertAlmostEqual(area1, expected_area1, places=7)

        area2 = self.square2.area()
        expected_area2 = 25  # 5 * 5
        self.assertAlmostEqual(area2, expected_area2, places=7)

    def test_square_perimeter(self):
        """Тест периметра квадрата"""
        perimeter1 = self.square1.perimeter()
        expected_perimeter1 = 12  # 4 * 3
        self.assertAlmostEqual(perimeter1, expected_perimeter1, places=7)

        perimeter2 = self.square2.perimeter()
        expected_perimeter2 = 20  # 4 * 5
        self.assertAlmostEqual(perimeter2, expected_perimeter2, places=7)

    def test_square_center(self):
        """Тест получения центра квадрата"""
        center = self.square1.center
        self.assertEqual(center.x, 1.5)
        self.assertEqual(center.y, 1.5)

        center2 = self.square2.center
        self.assertEqual(center2.x, 2.5)
        self.assertEqual(center2.y, 2.5)

    def test_square_is_rectangle(self):
        """Тест что квадрат является прямоугольником"""
        self.assertIsInstance(self.square1, Rectangle)

    def test_square_area_equals_side_squared(self):
        """Тест формулы площади квадрата"""
        side_length = 4
        square = Square(
            [
                Point(0, 0),
                Point(side_length, 0),
                Point(side_length, side_length),
                Point(0, side_length),
            ]
        )
        area = square.area()
        expected_area = side_length**2
        self.assertAlmostEqual(area, expected_area, places=7)

    def test_square_perimeter_equals_4_times_side(self):
        """Тест формулы периметра квадрата"""
        side_length = 4
        square = Square(
            [
                Point(0, 0),
                Point(side_length, 0),
                Point(side_length, side_length),
                Point(0, side_length),
            ]
        )
        perimeter = square.perimeter()
        expected_perimeter = 4 * side_length
        self.assertAlmostEqual(perimeter, expected_perimeter, places=7)

    def test_square_centered_at_origin(self):
        """Тест квадрата с центром в начале координат"""
        square = Square(
            [
                Point(-2, -2),
                Point(2, -2),
                Point(2, 2),
                Point(-2, 2),
            ]
        )
        center = square.center
        self.assertEqual(center.x, 0)
        self.assertEqual(center.y, 0)


if __name__ == "__main__":
    unittest.main()
