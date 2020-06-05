#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
from name import Name
import logging


class Street(Generator):

    def __init__(self, redis, features={}):

        Generator.__init__(self, redis, features)
        self.logger = logging.getLogger(__name__)
        


        self.name=Name(self.redis,'street')

    def __str__(self):
        return self.name.fullname.title()