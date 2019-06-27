# -*- coding: utf-8 -*-

from os.path import sep

from sklearn_porter.language.LanguageABC import LanguageABC


class JavaScript(LanguageABC):
    KEY = 'js'
    LABEL = 'JavaScript'

    DEPENDENCIES = ['node']
    TEMP_DIR = 'js'
    SUFFIX = 'js'

    CMD_COMPILE = None

    # node estimator.js <args>
    CMD_EXECUTE = 'node {dest_dir}' + sep + '{dest_file}'

    TEMPLATES = {
        'init':         'var {name} = {value};',

        # if/else condition:
        'if':           'if ({0} {1} {2}) {{',
        'else':         '} else {',
        'endif':        '}',

        # Basics:
        'indent':       '    ',
        'join':         '; ',
        'type':         '{0}',

        # Arrays:
        'in_brackets':  '[{0}]',
        'arr[]':        'var {name} = [{values}];',  # var ages = [1, 2];
        'arr[][]':      'var {name} = [{values}];',
        'arr[][][]':    'var {name} = [{values}];',

        # Primitive data types:
        'int':          '',
        'double':       ''
    }
