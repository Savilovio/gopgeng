# -*- coding: utf-8 -*-
import pygame
from pygame import *
class NewSpam(object):           # directly inherit from object
pass
NewSpam.__bases__
(<type 'object'>,)
class IntSpam(int):              # indirectly inherit from object...
pass
IntSpam.__bases__
(<type 'int'>,) 
IntSpam.__bases__[0].__bases__   # ... because int inherits from object  
(<type 'object'>,)