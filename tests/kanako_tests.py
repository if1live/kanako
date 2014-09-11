#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import kanako
import unittest
import os


class to_output_path_test(unittest.TestCase):
    def test_windows(self):
        input_path = 'd:\\kanako\\foo\\bar.tex'
        expected = 'd:\\kanako\\foo\\bar-output.tex'
        actual = kanako.to_output_path(input_path)
        self.assertEqual(actual, expected)
        
        input_path = 'd:/kanako/foo/bar.tex'
        expected = 'd:/kanako/foo/bar-output.tex'
        actual = kanako.to_output_path(input_path)
        self.assertEqual(actual, expected)
        
    def test_unix(self):
        input_path = '/kanako/foo/bar.tex'
        expected = '/kanako/foo/bar-output.tex'
        actual = kanako.to_output_path(input_path)
        self.assertEqual(actual, expected)
        
        
class build_report_test(unittest.TestCase):
    def test_run(self):
        ctx = {'name': 'foo'}
        expected = r'''
name:foo
\footnote{% hello }
'''.strip()
        input_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dummy.tex')
        actual = kanako.build_report(input_file, ctx)
        self.assertEqual(actual, expected)
        
        # check writed file
        output_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dummy-output.tex')
        with open(output_file) as f:
            output = f.read()
            self.assertEqual(output, expected)