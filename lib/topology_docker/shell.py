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

"""
Docker shell helper class module.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from topology.platforms.shell import PExpectShell


class DockerShell(PExpectShell):
    """
    Shell class for Docker nodes.

    See :class:`topology.platforms.shell.PExpectShell`.
    """

    def __init__(
        self, container, shell, prompt, initial_command=None,
        initial_prompt=None, password=None, password_match='[pP]assword:',
        prefix=None, timeout=None, encoding='utf-8'
    ):
        self._container = container
        self._shell = shell

        super(DockerShell, self).__init__(
            prompt, initial_command, initial_prompt, password, password_match,
            prefix, timeout, encoding
        )

    def _get_connect_command(self):
        return 'docker exec -i -t {} {}'.format(self._container, self._shell)


__all__ = ['DockerShell']
