import unittest

from volume.volume_util import remap_value


class TestVolumeUtil(unittest.TestCase):
    def test_map_value(self):
        self.assertEqual(remap_value(50, 0, 100, 0, 100), 50)
        self.assertEqual(remap_value(20, 0, 40, 0, 100), 50)
        self.assertEqual(remap_value(50, 0, 100, 20, 100), 40)
        self.assertEqual(remap_value(500, 0, 1000, 0, 100), 50)
        self.assertEqual(remap_value(127, 255, 0, 0, 100), 50)
        self.assertEqual(remap_value(50, 0, 100, 255, 0), 127)
        self.assertEqual(remap_value(25, 0, 100, 255, 0), 191)
        self.assertEqual(
            remap_value(50, 0, 100, -111.75, 0, float_range=True, decimal_places=2),
            -55.87,
        )
        self.assertEqual(
            remap_value(-50, 0, -100, -111.75, 0, float_range=True, decimal_places=2),
            -55.87,
        )
        self.assertEqual(
            remap_value(25, 0, 100, -111.75, 0, float_range=True, decimal_places=2),
            -83.81,
        )
        self.assertEqual(
            remap_value(75, 0, 100, -111.75, 0, float_range=True, decimal_places=2),
            -27.94,
        )
        self.assertEqual(
            remap_value(75, 0, 100, 0, -111.75, float_range=True, decimal_places=2),
            -83.81,
        )
