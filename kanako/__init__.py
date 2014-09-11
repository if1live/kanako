#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import os
import sys
from jinja2 import Template
import json

def to_utf8(obj):
    try:
        return obj.decode('utf-8')
    except:
        return obj.decode('cp949')

def build_report(input_file, fixture):
    with open(input_file, 'rb') as f:
        content = to_utf8(f.read())

    template = Template(content)
    output = template.render(ctx=fixture)

    output_file = to_output_path(input_file)
    with open(output_file, 'wb') as f:
        f.write(output.encode('utf-8'))
        
    return output
        
        
def to_output_path(path):
    base_path, filename = os.path.split(path)
    base_name, ext = os.path.splitext(filename)
    
    path_sep = os.path.sep
    for x in base_path:
        if x in ('\\', '/'):
            path_sep = x
            break
    
    output = path_sep.join([base_path, '{0}-output{1}'.format(base_name, ext)])
    return output
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        # use fake fixture
        module_dir = os.path.abspath(os.path.dirname(__file__))
        json_path = os.path.join(module_dir, 'fake.json')
        with open(json_path) as json_file:
            json_data = json.load(json_file)
            build_report(sys.argv[1], json_data)
            
    elif len(sys.argv) == 3:
        with open(sys.argv[2]) as json_file:
            json_data = json.load(json_file)
            build_report(sys.argv[1], json_data)
    else:
        print('Usage: {0} <tex_file>'.format(sys.argv[0]))
        print('Usage: {0} <tex_file> <fixture_json>'.format(sys.argv[0]))
