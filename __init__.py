# -*- coding: utf-8 -*-
'''
Created on 2017. 8. 30.
@author: HyechurnJang
'''

import os
import types
import pygics

#===============================================================================
# Register Resource Path
#===============================================================================
_extag_rsc = pwd() + '/resource'
_cache_data = {}
@pygics.api('GET', 'resource')
def get(req, *argv, **kargs):
    
    class CacheData(types.FileType):
        def __init__(self, path):
            self.fd = open(path, 'rb')
            self.data = self.fd.read()
            self.path = path
        
        @property
        def name(self): return self.path
        def read(self): return self.data
        def close(self): return None
    
    path = '/'.join(argv)
    file_path = '%s/%s' % (_extag_rsc, path)
    if file_path in _cache_data: return _cache_data[file_path]
    else:
        if not os.path.exists(file_path): raise Exception('could not find %s' % path)
        cache_data = CacheData(file_path)
        _cache_data[file_path] = cache_data
        return cache_data

# Register ExTags
from tags import GRID