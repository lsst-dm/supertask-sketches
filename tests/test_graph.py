#!/usr/bin/env python

from __future__ import print_function, division, absolute_import

import sys
import os
import unittest
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import repodb
import repodb.tests


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.backend = repodb.tests.makeBackend()

    def testCreateTables(self):
        pass

    def testUniverseGraph(self):
        graph = self.backend.makeGraph(repodb.COMMON_UNITS)
        self.assertItemsEqual(graph.units.keys(), repodb.COMMON_UNITS)
        for UnitClass, names, values in repodb.tests.EXAMPLE_DATA:
            for unit, data in zip(graph.units[UnitClass], values):
                for i, name in enumerate(names):
                    attr = getattr(unit, name)
                    if isinstance(attr, repodb.Unit):
                        self.assertEqual(attr.id, data[i])
                    elif isinstance(attr, datetime.datetime):
                        self.assertEqual(
                            attr,
                            datetime.datetime.fromtimestamp(data[i])
                        )
                    else:
                        self.assertEqual(
                            attr,
                            data[i],
                            msg="{}.{}".format(UnitClass.__name__, name)
                        )


if __name__ == "__main__":
    unittest.main()
