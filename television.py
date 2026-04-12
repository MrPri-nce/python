class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__channel = self.min_channel
        self.__volume = self.min_volume

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            if self.__channel < self.max_channel:
                self.__channel += 1
            else:
                self.__channel = self.min_channel

    def channel_down(self):
        if self.__status:
            if self.__channel > self.min_channel:
                self.__channel -= 1
            else:
                self.__channel = self.max_channel


    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.muted = False
            if self.__volume < self.max_volume:
                self.__volume += 1
            else:
                self.__volume = self.min_volume

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.muted = False
            if self.__volume > self.min_volume:
                self.__volume -= 1
            else:
                self.__volume = self.max_volume

    def __str__(self):
        power_status = 'True' if self.__status else 'False'
        muted_status = 'True' if self.__muted else 'False'
        return f'Power = {power_status}, Channel = {self.__channel}, Volume = {self.__volume}, Muted = {muted_status}'

