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

from time import sleep
from pexpect import TIMEOUT
from topology.platforms.shell import PExpectShell, PExpectBashShell


class DockerExecMixin(object):
    """
    Docker ``exec`` connection mixin for the Topology shell API.

    This class implements a ``_get_connect_command()`` method that allows to
    interact with a shell through a ``docker exec`` interactive command, and
    extends the constructor to request for container related parameters.

    :param str container: Container unique identifier.
    :param str command: Command to be executed with the ``docker exec`` that
     will launch an interactive session.
    """

    def __init__(self, container, command, *args, **kwargs):
        self._container = container
        self._command = command
        super(DockerExecMixin, self).__init__(*args, **kwargs)

    def _get_connect_command(self):
        return 'docker exec -i -t {} {}'.format(
            self._container, self._command
        )


class DockerShell(DockerExecMixin, PExpectShell):
    """
    Generic ``docker exec`` shell for unspecified interactive session.
    """


class DockerBashShell(DockerExecMixin, PExpectBashShell):
    """
    Specialized ``docker exec`` shell that will run and setup a bash
    interactive session.
    """
    def __init__(self, *args, **kwargs):
        super(DockerBashShell, self).__init__(*args, **kwargs)
        self.delay_after_echo = 0.5

    def _setup_shell(self, connection=None):
        super(DockerBashShell, self)._setup_shell(connection)
        spawn = self._get_connection(connection)
        attempts = 10
        expected_matches = [
            r'(?<!export PS1=){}'.format(self._prompt),
            r'export PS1=.*',
            TIMEOUT
        ]
        for num in range(attempts):
            index = spawn.expect(expected_matches, timeout=self._timeout)

            # Successfully set prompt
            if index == 0:
                print('Matched Forced prompt')
                break

            # Echo is not off
            elif index == 1:
                spawn.sendline('stty -echo')
                print('Matched export PS1 prompt')
                sleep(self._delay_after_echo_off)
                spawn.expect(
                    self._prompt, timeout=self._timeout
                )
                spawn.sendline('export PS1={}'.format(self._prompt))

            # Prompt is not properly set
            elif index == 2:
                print('Matched TIMEOUT')
                spawn.sendline('export PS1={}'.format(self._prompt))

            else:
                raise Exception(
                    'Unexpected prompt appears while setting bash prompt'
                )

        else:
            raise Exception('Unable to set up bash after 10 attempts')

        for num in range(attempts):
            # This is an expected timeout, so we want to reduce time waited.
            index = spawn.expect([self._prompt, TIMEOUT], timeout=5)
            if index == 0:
                continue
            else:
                break
        else:
            raise Exception('Unable to consume all extra bash prompts')
        spawn.sendline(' ')

__all__ = ['DockerShell', 'DockerBashShell']
