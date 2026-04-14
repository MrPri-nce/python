import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    def test_init(self):
        tv = Television()
        self.assertEqual("Power = False, Channel = 0, Volume = 0", str(tv))

    def test_power(self):
        tv = Television()
        tv.power()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", str(tv))

    def test_mute(self):
        tv = Television()
        tv.power()
        tv.mute()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", str(tv))

    def test_channel_up(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        self.assertEqual("Power = True, Channel = 1, Volume = 0", str(tv))

    def test_channel_down(self):
        tv = Television()
        tv.power()
        tv.channel_down()
        self.assertEqual("Power = True, Channel = 3, Volume = 0", str(tv))


    def test_volume_up(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        self.assertEqual("Power = True, Channel = 0, Volume = 1", str(tv))


    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_down()
        self.assertEqual("Power = True, Channel = 0, Volume = 0", str(tv))