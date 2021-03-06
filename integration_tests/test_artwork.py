#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Test the Artwork against live data in redis to ensure the Artwork data is valid/behaves."""

import unittest
from megacosm.generators.Artwork import Artwork
from config import IntegrationTestConfiguration
from fixtures import artwork, npc, gem, deity, phobia, motivation


class TestArtworkIntegration(unittest.TestCase):
    """ Test Artwork Integration """
    def setUp(self):
        """Create Redis Connection"""
        self.redis = IntegrationTestConfiguration.REDIS
        artwork.import_fixtures(self)
        gem.import_fixtures(self)
        npc.import_fixtures(self)
        phobia.import_fixtures(self)
        motivation.import_fixtures(self)
        deity.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_kinds(self):
        """ Test all the artwork kinds, subkinds, and their templates """
        for kind in self.redis.lrange('artwork_kind', 0, -1):
            for template in self.redis.lrange('artwork%s_template' % kind, 0, -1):
                artwork = Artwork(self.redis, {'kind': kind, 'template': template})
                self.assertEqual(kind, str(artwork.kind))

                self.assertNotIn('{', str(artwork))
                self.assertNotIn('}', str(artwork))
                self.assertNotIn('params', str(artwork))
            for subkind in self.redis.lrange("artwork%s_subkind" % kind, 0, -1):
                artwork = Artwork(self.redis, {'kind': kind, 'subkind': subkind})
                self.assertEqual(kind, str(artwork.kind))
                self.assertNotIn(kind, str(artwork))
                self.assertIn(subkind, str(artwork))

                self.assertNotIn('{', str(artwork))
                self.assertNotIn('}', str(artwork))
                self.assertNotIn('params', str(artwork))
