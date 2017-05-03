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
    def _setup_shell(self, connection=None):
        """
        Overriden setup function that will disable the echo on the device on
        the shell and set a pexpect-safe prompt.
        """
        spawn = self._get_connection(connection)

        # Wait initial prompt
        spawn.expect(
            self._initial_prompt, timeout=self._timeout
        )

        # Remove echo
        spawn.sendline('stty -echo')
        spawn.expect(
            self._initial_prompt, timeout=self._timeout
        )

        # Change prompt to a pexpect secure prompt
        spawn.sendline(
            'export PS1={}'.format(PExpectBashShell.FORCED_PROMPT)
        )
        self._prompt = PExpectBashShell.FORCED_PROMPT

        # Brute force solving prompt setting bug
        spawn.expect(
            self._prompt, timeout=self._timeout
        )

        spawn.sendline(
            'export PS1={}; clear'.format(PExpectBashShell.FORCED_PROMPT)
        )
        spawn.expect(
            self._prompt, timeout=self._timeout
        )

        spawn.sendline(
            'export PS1={}'.format(PExpectBashShell.FORCED_PROMPT)
        )
        spawn.expect(
            self._prompt, timeout=self._timeout
        )

        spawn.sendline(
            'export PS1={}'.format(PExpectBashShell.FORCED_PROMPT)
        )
        spawn.expect(
            self._prompt, timeout=self._timeout
        )
        spawn.sendline(
            'export PS1={};clear'.format(PExpectBashShell.FORCED_PROMPT)
        )
        spawn.expect(
            self._prompt, timeout=self._timeout
        )
        spawn.sendline(
            'export PS1={}'.format(PExpectBashShell.FORCED_PROMPT)
        )
        spawn.expect(
            self._prompt, timeout=self._timeout
        )

        spawn.sendline(
            'export PS1={};'.format(PExpectBashShell.FORCED_PROMPT)
        )


__all__ = ['DockerShell', 'DockerBashShell']
