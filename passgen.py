# MIT License
#
# Copyright (c) 2023 BJX
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import getpass
import hashlib

def get_master_password():
    while True:
        x = getpass.getpass("Please input your master password (e.g. My-SuperSecret-MasterPassw0rd)! ")
        y = getpass.getpass("Please input your master password again! ")
        if x != y:
            print("The master password inputs didn't match!")
        else:
            return x

def get_user():
    return input("Please input your user name (e.g. MyUser01)! ")

def get_website():
    return input("Please input the name of the website/service/host (e.g. gmail.com)! ")

def get_year():
    return input("Please input the year (e.g. 2023)! ")

def get_seed():
    return [ get_master_password(), get_user(), get_website(), get_year() ]

def get_hash(seed):
    h = hashlib.new("sha3_512", usedforsecurity=True)
    for x in seed:
        s = "before" + str(len(x)) + "in the middle" + x + "and after"
        h.update(s.encode())
    return sum((x << (i * 8)) for i, x in enumerate(h.digest()))

def index_by_hash(t, h):
    x = t[h % len(t)]
    return x, h // len(t)

def get_vowel(h):
    return index_by_hash("aeiou", h)

def get_consonant(h):
    return index_by_hash("bcdfghjklmnpqrstvwx", h)

def get_syllable(h):
    (c, h2) = get_consonant(h)
    (v, h3) = get_vowel(h2)
    return c + v, h3

def generate_password(h):
    pw = ""
    for i in range(3):
        (v, h) = get_vowel(h)
        (s1, h) = get_syllable(h)
        (s2, h) = get_syllable(h)
        (c, h) = get_consonant(h)
        pw += v.upper() + s1 + s2 + c + "-"
    return pw + str(h % 1000)

def main():
    print("The generated password is:", generate_password(get_hash(get_seed())))

main()
