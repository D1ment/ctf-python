# -*- coding: utf-8 -*-
import hashlib

m = '4850B7446BBB20AAD140E7B0A964A57D'
k = '2453148193'


EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

en = "abcdefghijklmnopqrstuvwxyz"

RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

digits = "1234567890"

space = " "

p = ",.-!?;:'\"/()"

op = "+-*/:^()<>="

all_spec = "`~!@#$%^&*-_=+\\|/?.>,< '\";:[]{}"

class ABCIterator:
    firstuse_flag = True
    stop = None

    def __init__(self, start="", stop=None, start_len=None, stop_len=None, abc=en+EN+digits+all_spec):
        assert len(abc) > 0

        if start_len is not None:

            assert start_len > 0

            #assert start == ""

            self.current_str = list(abc[0]*start_len)

        else:

            self.current_str = list(filter(lambda x: x in abc, start))

        if stop_len is not None:

            assert (start_len is None) or (start_len <= stop_len)
            assert stop_len > 0

            self.stop = list(abc[0]*(stop_len+1)) # т.к. итератор работает с полуотрезками

        else:

            if stop is not None: self.stop = list(filter(lambda x: x in abc, stop))

        self.abc = list(abc)

    def __iter__(self):

        return self

    def next(self):

        if (self.stop is not None) and (self.stop == self.current_str):

            raise StopIteration

        if self.current_str == []:

            self.current_str.append(self.abc[0])

            self.firstuse_flag = False

            return self.abc[0]

        elif self.firstuse_flag:

            self.firstuse_flag = False

            return "".join(self.current_str)

        offset = 0

        while offset < len(self.current_str):
            if self.current_str[offset] != self.abc[-1]:
                self.current_str[offset] = self.abc[self.abc.index(self.current_str[offset])+1]
                # выпендрёшь для полуотрезка
                if (self.stop is not None) and (self.current_str == self.stop):
                    raise StopIteration
                return "".join(self.current_str)
            self.current_str[offset] = self.abc[0]
            offset += 1
        self.current_str = [self.abc[0]] + self.current_str
        # опять же оно же
        if (self.stop is not None) and (self.current_str == self.stop):
            raise StopIteration
        return "".join(self.current_str)

#===============
m = hashlib.md5()
j = 0
for i in ABCIterator(start_len=1, stop_len=10):
    md = k + i
    mdd = m.hexdigest()
    j += 1
    if j % 1000000 == 0:
        print(j, len(i))
    if mdd == m:
        print(md)
        break
