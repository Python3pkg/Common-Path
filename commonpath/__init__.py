# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2015 Florenz A. P. Hollebrandse
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

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

from collections import defaultdict, Counter
from os.path import sep, normpath
import sys


class CommonPath(object):
    def __init__(self, paths):
        #: List of paths to analyse
        self.paths = map(normpath, paths)
        #: Default maximum path depth to analyse
        self.default_max_depth = sys.maxsize

        split_paths = [p.split(sep) for p in self.paths]
        # Dict of list of unpacked paths with path depth level as keys
        # e.g. {0: ['', ''],
        #       1: ['/home', '/home', '/usr'],
        #       2: ['/home/user1', '/home/user1', '/usr/bin']}
        levels = defaultdict(list)
        for split_path in split_paths:
            for level, ele in enumerate(split_path):
                levels[level].append(sep.join(split_path[0:level + 1]))
        #print(levels)

        self.most_common = {}
        for level in levels:
            self.most_common[level] = Counter(levels[level]).most_common(1)[0]
            #print(level, self.most_common[level])

    def natural(self, max_depth=None):
        max_depth = max_depth or self.default_max_depth
        return

    def absolute(self, max_depth=None):
        max_depth = max_depth or self.default_max_depth
        max_count = 0
        result = None
        for i, common in self.most_common.items():
            if common[1] < max_count or i > max_depth - 1:
                break
            else:
                max_count = common[1]
                result = common[0]
        return result