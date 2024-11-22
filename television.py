
class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:

        """
        Initializes four variables for the television.
        status: whether or not the television is powered
        muted: whether or not the television is muted
        volume: the volume of the television
        channel: the channel of the television
        """

        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:

        """
        Toggles the television on or off.
        :return: None
        """

        self.__status = not self.__status

    def mute(self) -> None:

        """
        Toggles the television between muted and unmuted.
        The television's volume will be remembered while muted.
        :return: None
        """

        if not self.__status:
            return
        self.__muted = not self.__muted

    def channel_up(self) -> None:

        """
        Increments the television's channel by 1.
        If at the maximum channel, it will loop back to the minimum channel.
        :return: None
        """

        if not self.__status:
            return
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1


    def channel_down(self) -> None:

        """
        Decrements the television's channel by 1.
        If at the minimum channel, it will loop back to the maximum channel.
        :return: None
        """

        if not self.__status:
            return
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self) -> None:

        """
        Increments the television's volume by 1.
        This will unmute the television if it is muted.
        If at the maximum volume, no volume change will happen.
        :return: None
        """

        if not self.__status:
            return
        self.__muted = False
        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1


    def volume_down(self) -> None:

        """
        Decrements the television's volume by 1.
        This will unmute the television if it is muted.
        If at the minimum volume, no volume change will happen.
        :return: None
        """

        if not self.__status:
            return
        self.__muted = False
        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:

        """
        Generates a string with the format 'Power = [status], Channel = [channel], Volume = [volume]'
        :return: The formatted string.
        """

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME if self.__muted else self.__volume}'

