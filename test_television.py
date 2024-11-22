import pytest
from television import Television

class Test:

    def setup_method(self):
        self.t1 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):

        self.t1.power()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 0'
        self.t1.power()
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 0'
        self.t1.power()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 0'

    def test_mute(self):

        self.t1.power()
        self.t1.volume_up()
        self.t1.mute()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 0'
        self.t1.mute()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 1'
        self.t1.power()
        self.t1.mute()
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 1'
        self.t1.mute()
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 1'


    def test_channel_up(self):

        self.t1.channel_up()
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.channel_up()
        assert str(self.t1) == 'Power = True, Channel = 1, Volume = 0'
        self.t1.channel_up()
        self.t1.channel_up()
        self.t1.channel_up()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):

        self.t1.channel_down()
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.channel_down()
        assert str(self.t1) == 'Power = True, Channel = 3, Volume = 0'
        self.t1.channel_down()
        self.t1.channel_down()
        self.t1.channel_down()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self):

        self.t1.volume_up()
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.volume_up()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 1'
        self.t1.mute()
        self.t1.volume_up()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 2'
        self.t1.volume_up()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):

        self.t1.volume_down()
        assert str(self.t1) == 'Power = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.volume_up()
        self.t1.volume_up()
        self.t1.volume_down()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 1'
        self.t1.volume_up()
        self.t1.mute()
        self.t1.volume_down()
        assert str(self.t1) == 'Power = True, Channel = 0, Volume = 1'