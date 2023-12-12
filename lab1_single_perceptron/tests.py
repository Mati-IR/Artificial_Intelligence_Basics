import unittest
from point import Point
from point_generator import PointGenerator

class MyTestCase(unittest.TestCase):
    def test_Point(self):
        point = Point(1, 2, 3)
        self.assertEqual(point.get_coordinates(), [1, 2])
        self.assertEqual(point.get_label(), 3)
        point.set_coordinates(4, 5)
        point.set_label(6)
        self.assertEqual(point.get_coordinates(), [4, 5])
        self.assertEqual(point.get_label(), 6)
        self.assertEqual(str(point), "Point: 4, 5, 6")
        self.assertEqual(repr(point), "Point: 4, 5, 6")

    def test_PointGenerator(self):
        # 1 if bigger than 1*x + 0, -1 if smaller or equal
        fun = lambda x, y: 1 if (y > x) else -1
        generator = PointGenerator(fun)
        points = generator.generate(10)
        self.assertEqual(len(points), 10)
        for point in points:
            self.assertEqual(len(point.get_coordinates()), 2)
            expected_label = 1 if (fun(point.get_coordinates()[0], point.get_coordinates()[1]) < int(point.get_coordinates()[1])) else -1
            print(f"point: {point}\nexpected_label: {expected_label}")
            self.assertEqual(point.get_label(), expected_label)



if __name__ == '__main__':
    unittest.main()
