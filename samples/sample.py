class GoodFieldsSample:
    def __init__(self):
        self._a = 0
        self._b = 0

    def three_fields(self):
        if self._a == self._b:
            self._a = 0


class BadFieldsSample:
    def __init__(self):
        self._a = 0
        self._b = 0
        self._third_field = 0

    def three_fields(self):
        self._third_field = 0
        self._b = self._third_field
        if self._a == self._b:
            self._a = self._third_field


class BadCollectionSample1:
    def __init__(self):
        self._a = []
        self._b = 0


class BadCollectionSample2:
    def __init__(self):
        self._a = [a for a in [1, 2, 3]]
        self._b = 0


class BadCollectionSample3:
    def __init__(self):
        self._a = list()
        self._b = 0


class BadCollectionSample4:
    def __init__(self):
        self._a = set()
        self._b = 0


class BadCollectionSample5:
    def __init__(self):
        self._a = (1, "a")
        self._b = 0


class BadCollectionSample6:
    def __init__(self):
        self._a = {"a": 1}
        self._b = 0


class GoodCollectionSample:
    def __init__(self):
        self._a = []


class BadIndentationSample:
    def __init__(self):
        self._a = 0

    def one_level_of_indent(self):
        self._a = 1
        if self._a > 1:
            self._a = 1

    def two_levels_of_indent_if(self):
        self._a = 1
        if self._a > 1:
            if self._a > 2:
                self._a = 1

    def two_levels_of_indent_for(self):
        self._a = 1
        for i in [1, 2]:
            if self._a > i:
                self._a = 1


class ElseSample:
    def __init__(self):
        self._a = 0

    def uses_else(self):
        self._a = 1
        if self._a > 1:
            self._a = 1
        else:
            self._a = 2


class JustOkSizeSample:
    def __init__(self):
        self._a = 0

    def method1(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1

    def method2(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1

    def method4(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1

    def method5(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1


class TooLargeSizeSample:
    def __init__(self):
        self._a = 0

    def method1(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1

    def method2(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1

    def method4(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1

    def method5(self):
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        self._a = 1
        # one too much
        self._a = 1


class BadProperties1:
    def __init__(self):
        self._temperature = 0
        self.public_property = 0

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


class BadProperties2:
    def __init__(self):
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
