# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from os.path import exists
from os import makedirs
from shutil import copytree, Error, copy


def pytest_runtest_teardown(item):
    """
    pytest hook to move log files to appropriate test folder
    """
    logs_path = '/var/log/messages'
    if 'topology' in item.funcargs:
        if 'docker' in item.funcargs['topology'].engine:
            dirs = []
            for node in iter(item.funcargs['topology'].nodes):
                if hasattr(item.funcargs['topology'].get(node), 'shared_dir'):
                    node_obj = item.funcargs['topology'].get(node)
                    dirs.append(node_obj.shared_dir)
                    log_temp_dir = '/tmp/var_messages.log'.format(id(node_obj))
                    node_obj.send_command('cat {} > {}'
                                          .format(logs_path, log_temp_dir),
                                          shell='bash')
            if dirs:
                path_name = '/tmp/{}_{}'.format(item.name, str(id(item)))
                if not exists(path_name):
                    makedirs(path_name)
                for directory in dirs:
                    temp_dir = directory.replace('/tmp/', '')
                    try:
                        copytree(directory, '{}/{}'.format(path_name,
                                                           temp_dir))
                    except Error as err:
                        errors = err.args[0]
                        for error in errors:
                            src, dest, msg = error
                            print('Unable to copy file {}, Error {}'
                                  .format(src, msg))
