===================================
Docker Platform Engine for Topology
===================================

Docker based Platform Engine plugin for the Network Topology Framework.

License
=======

::

   Copyright (C) 2015-2016 Hewlett Packard Enterprise Development LP

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.

Changelog
=========

1.1.7 (2017-08-25)
------------------

New
~~~
- Added logic to deal with unmatched bash prompts. [Javier Peralta]
- Add a more intelligent method to set bash. [Javier Peralta]



1.1.6 (2017-08-18)
------------------

New
~~~
- Configures shell delay to 1 second. [Javier Peralta]


1.1.5 (2017-07-25)
------------------

Changes
~~~~~~~
- Adding .gitchangelog. [Diego Antonio Hurtado Pimentel]
- Adding timeout. [Diego Antonio Hurtado Pimentel]


1.1.4 (2017-05-16)
------------------

Changes
~~~~~~~
- Revert "new: dev: Add workaround for bash prompt" [Javier Peralta]

  This reverts the prompt issue workaround, a proper fix is
  being made in topology repo.

Other
~~~~~
- Merge pull request #14 from saenzpa/undo-workaround. [Diego Hurtado]

  chg: dev: Revert "new: dev: Add workaround for bash prompt"


1.1.3 (2017-05-10)
------------------

New
~~~
- Add workaround for bash prompt. [Javier Peralta]

  Sometimes the foreced prompt is not setting correctly,
  sets it few more times to make sure it works.

Fix
~~~
- Minor fixing and removal of Python 2.7. [Diego Antonio Hurtado
  Pimentel]


1.1.2 (2017-02-21)
------------------

Fix
~~~
- Detect oobm links with passthrough switch. [Pablo Saenz]

Other
~~~~~
- Merge pull request #11 from saenzpa/multiple_oobm. [Pablo Saenz]

  fix: dev: Detect oobm links with passthrough switch.


1.1.1 (2016-11-23)
------------------

Fix
~~~
- Removing specific dependencies. [Diego Antonio Hurtado Pimentel]


1.1.0 (2016-11-23)
------------------

New
~~~
- Adding support for environment setting. [Diego Antonio Hurtado
  Pimentel]
- Added Dockerfile for future host container. [Carlos Miguel Jenkins
  Perez]
- Added logging for image being used and container data. [Carlos Miguel
  Jenkins Perez]
- All Docker nodes will now mount the /tmp/ directory in a
  /tmp/topology_{identifier}_{uid} folder on the host. The folder name
  can be retrieved with the .shared_dir attribute. [Carlos Miguel
  Jenkins Perez]
- Added a new test for default routes between host nodes. [Carlos Miguel
  Jenkins Perez]
- Added logging to docker exec calls and made the OpenSwitch script to
  output debug information by default. [Carlos Miguel Jenkins Perez]

  Also made topology 1.0.1 as the minimum version.

Changes
~~~~~~~
- Added implementation of the Topology 1.8 _get_services_address()
  method on nodes and updated shell registration to use
  _register_shell() method. [Carlos Miguel Jenkins Perez]
- Modifying metadata in if condition in node.py. [fonsecamau]
- Removing privileged option for hosts and using cap-add instead.
  [fonsecamau]
- Bumping version to release 1.6.0. [Diego Antonio Hurtado Pimentel]
- Fixing LTS version temporarily while we create a testing image.
  [Carlos Miguel Jenkins Perez]
- Adding a little more documentation on the image attribute. [Diego
  Antonio Hurtado Pimentel]
- Bumping version to release 1.5.0. [Carlos Miguel Jenkins Perez]
- Moving away support nodes specific tests to their own repositories.
  [Carlos Miguel Jenkins Perez]
- Bumping version to release 1.4.0. [Carlos Miguel Jenkins Perez]
- Migrated all nodes shells to new Topology shell API. [Carlos Miguel
  Jenkins Perez]
- The binds attribute can now be injected and extended by users. [Carlos
  Miguel Jenkins Perez]
- Bumping version to release 1.3.0. [Carlos Miguel Jenkins Perez]
- Bumping version to release 1.2.0. [Carlos Miguel Jenkins Perez]
- Moved away node loading logic now that it is present in topology
  1.1.0. [Carlos Miguel Jenkins Perez]
- Bumping version number to 1.1.0. [Carlos Miguel Jenkins Perez]
- Added a changelog to the main README.rst file to prepare for minor
  release. [Carlos Miguel Jenkins Perez]

Fix
~~~
- Dev: Forcing docker.py version to 1.9.0. [Pablo Saenz]
- Adding topology master as a dependency. [Diego Antonio Hurtado
  Pimentel]
- Using correct attribute name. [Pablo Saenz]
- Skipping link creation for oobm. [Pablo Saenz]
- Adding logging mechanisms to psaenz fork. [Pablo Saenz]
- Dev: Forcing ubuntu image to 14.04. [Pablo Saenz]
- Real fix of the previous commit. [Carlos Miguel Jenkins Perez]

  Sleepy sleeeepyyyy.
- Fixed bug when a node failed to start and its not considered for the
  rollback. [Carlos Miguel Jenkins Perez]

  Also made the destroy and rollback best effort.
- Moving support nodes out of this repo. [Diego Antonio Hurtado
  Pimentel]
- Reduced polling frequency to reduce output in test and added minimal
  wait to improve test performance. [Carlos Miguel Jenkins Perez]
- Refactored and fixed many tests. [Carlos Miguel Jenkins Perez]
- Add bonding_masters to ip link set exceptions. [Agustin Meneses]

  This change is needed in order to use the Linux bonding driver, otherwise
  the tests will fail while setting up the ports.
- Setting version to auto. [Diego Antonio Hurtado Pimentel]
- Adding proper skip. [Diego Antonio Hurtado Pimentel]
- Fixed issue with command echo removal. [Carlos Miguel Jenkins Perez]
- Fixing to be compliant with new pep8 requirements. [Diego Antonio
  Hurtado Pimentel]
- Make regular for propmt more specific. [Mauricio Fonseca]
- Fixed URL of the repository now that it moved. [Carlos Miguel Jenkins
  Perez]
- Removing unused Toxin dockerfile (for now). [Carlos Miguel Jenkins
  Perez]
- Fixed bad name of a test. [Carlos Miguel Jenkins Perez]
- Output gets confused with switch prompt. [Mauricio Fonseca]

Other
~~~~~
- Merge pull request #10 from saenzpa/hpe_sync_with_logs. [Diego
  Hurtado]

  new: dev: Adding support for environment setting.
- Merge pull request #9 from saenzpa/restd_start. [Diego Hurtado]

  fix: dev: Adding topology master as a dependency.
- Merge pull request #7 from fonsecamau/master. [Pablo Saenz]

  chg: dev: Modifying metadata in if condition in node.py
- Merge pull request #6 from fonsecamau/master. [Pablo Saenz]

  chg: dev: Removing privileged option for hosts and using cap-add instead
- Merge pull request #5 from saenzpa/master_sync. [Pablo Saenz]

  Master sync
- Merge branch 'master' of github.com:saenzpa/topology_docker. [Pablo
  Saenz]
- Merge pull request #3 from saenzpa/revert-2-master. [Pablo Saenz]

  Revert "Pulling in fixes from Main project"
- Revert "Pulling in fixes from Main project" [Pablo Saenz]
- Merge pull request #2 from HPENetworking/master. [Pablo Saenz]

  Pulling in fixes from Main project
- Add: Dev: skipping link creation if oobmhost is present. [Pablo Saenz]
- Merge pull request #1 from HPENetworking/master. [Pablo Saenz]

  pulling from master
- Merge pull request #31 from HPENetworking/image_doc. [Carlos Jenkins]

  chg: doc: Adding a little more documentation on the image attribute.
- Merge pull request #24 from HPENetworking/new_shell_api_migration.
  [David Diaz Barquero]

  chg: dev: Migrated all nodes shells to new Topology shell API.
- Merge pull request #23 from HPENetworking/new_binds_attribute. [Carlos
  Jenkins]

  chg: usr: The binds attribute can now be injected and extended by users.
- Merge pull request #20 from HPENetworking/ddompe-patch-1. [Diego
  Hurtado]

  Improvements during initialization
- Fix bugs during initialization. [Diego Dompe]

  - Handle support for sync the port readiness with the newer openswitch images
  - Delay waiting for the cur_cfg, and handle  the case where the cfg is not ready yet better.
- Merge pull request #19 from agustin-meneses-fuentes/master. [Carlos
  Jenkins]

  fix: dev: Add bonding_masters to ip link set exceptions
- Merge pull request #14 from HPENetworking/auto_version. [Carlos
  Jenkins]

  fix: dev: Setting version to auto.
- Merge pull request #11 from walintonc/master. [Carlos Jenkins]

  new: usr: Add support to specifying the hostname for a node.
- Add support to specifying hostname for create_container. [Walinton
  Cambronero]

  - This allows that nodes can specify the hostname of choice
  - In the openswitch node, the default hostname is 'switch'
  - Clarify that tag must be specified in image param
- Merge pull request #6 from josedvq/master. [Carlos Jenkins]

  chg: dev: Added checks for Open vSwitch's required kernel module.
- Add: dev: Added checks for Open vSwitch's required kernel module.
  [Jose Vargas]
- Merge pull request #5 from HPENetworking/pep8-upgrade. [David Diaz
  Barquero]

  fix: dev: Fixing to be compliant with new pep8 requirements.
- Merge pull request #2 from fonsecamau/fix_cut_output. [Carlos Jenkins]

  fix: dev: Make vtysh shell regular expression for prompt more specific.
- Merge pull request #1 from josedvq/master. [Carlos Jenkins]

  new: dev: Added dockerfiles for Ryu and p4switch images.
- Add: dev: Added dockerfiles for Ryu and p4switch images. [Jose Vargas]
- Merge pull request #19 from hpe-networking/fix_cut_output. [Carlos
  Miguel Jenkins Perez]

  fix: dev: Output gets confused with switch prompt


1.0.0 (2016-01-06)
------------------

New
~~~
- Added a new auto-pull feature that automatically download any Docker
  image required. [Carlos Miguel Jenkins Perez]
- Mapping ports to port labels. [Mauricio Fonseca]
- Add OpenvSwitch node implementation. [David Diaz]
- Add docker file for toxin node. [David Diaz]
- Add bridge interface between toxin node and host for rest api. [David
  Diaz]

  This bridge interface is with a firewall to limit traffic to txnd rest api.
- Add toxin node. [David Diaz]
- Added documentation for the interpreted attributes. [Carlos Miguel
  Jenkins Perez]
- Added some attributes interpretation for ports (ipv4, ipv6, up) and
  links (up). [Carlos Miguel Jenkins Perez]
- Added two new methods to the base DockerNode that allow to pause and
  unpause the node. [Carlos Miguel Jenkins Perez]
- Added logging to the openswitch setup script. [Carlos Miguel Jenkins
  Perez]
- Added the ovs-vsctl shell to the openswitch nodes (reference it as
  vsctl). [Carlos Miguel Jenkins Perez]
- Added a new shell to the openswitch node to allow to execute commands
  in the switch network namespace. [Carlos Miguel Jenkins Perez]
- Added a test for unlink / relink. [Carlos Miguel Jenkins Perez]
- Added implementation of the relink and unlink calls. [Carlos Miguel
  Jenkins Perez]
- Added logic to create missing ports by parsing the hardware spec and
  added a script to wait for software to be ready. [Carlos Miguel
  Jenkins Perez]
- Allow the platform to be runned without global root privileges.
  [Carlos Miguel Jenkins Perez]
- Added a version of the ping test using the ip command. Sadly, not
  working at the moment. [Carlos Miguel Jenkins Perez]
- Bind volumes to docker switch. [David Diaz]
- Move link interface to swns if node is a switch. [David Diaz]
- Add send_command to docker nodes. [Diego Antonio Hurtado Pimentel]
- Add tuntap interfaces for no-linked ports. [David Diaz]
- Add test that builds a topo and ping. [David Diaz]
- Add ping to test. [David Diaz]
- Add start method on DockerNode. [David Diaz]
- Refactoring from topology_vsi. [David Diaz]
- Update requirements. [David Diaz]
- Initial repository layout from cookiecutter template. [Carlos Miguel
  Jenkins Perez]

Changes
~~~~~~~
- Moved all default images to use the public docker hub registry as now
  the images are available in it. [Carlos Miguel Jenkins Perez]
- Removing Toxin related node and test as it will not be part of the
  first public release. [Carlos Miguel Jenkins Perez]
- Changed URLs, version number and requirements for public release.
  [Carlos Miguel Jenkins Perez]
- Avoid moving new oobm interface to swns namespace. [David Diaz]
- Removed deprecated feature to change images using environment
  variables as the attribute injection feature supersede it. [Carlos
  Miguel Jenkins Perez]
- Minor changes on openswitch setup script. [Carlos Miguel Jenkins
  Perez]
- Refactored all send_commands to docker_exec to avoid using pexpect.
  [Carlos Miguel Jenkins Perez]
- Minor style changes and added txnd process as class attribute to track
  if it dies. [Carlos Miguel Jenkins Perez]
- Port up / down is now a competence of the engine node, and
  unlink/relink were modified to call the enode method. [Carlos Miguel
  Jenkins Perez]
- Removing pytest-xdist as is not used by default in the tox file.
  Please re-add it when setup. [Carlos Miguel Jenkins Perez]
- Simplified the implementation of the openswitch setup script to check
  by it's own the already created ports. [Carlos Miguel Jenkins Perez]
- Include the identifier in the container name for easy identification
  and avoid clash of shared directories. [Carlos Miguel Jenkins Perez]
- Refactored the setup logic to be performed on the container side and
  thus allows to drop pyyaml requirement from topology_docker. [Carlos
  Miguel Jenkins Perez]
- Setting the default timeout for the ovs-vsctl to 60 seconds to reduce
  timeout issues. [Carlos Miguel Jenkins Perez]
- Minor style change. [Carlos Miguel Jenkins Perez]
- Change container naming to allow parallel test running. [David Diaz]
- Small change in documentation to make easy copy - paste of commands.
  [Carlos Miguel Jenkins Perez]
- Refactored the call to privileged commands. [Carlos Miguel Jenkins
  Perez]
- Normalized tests style. [Carlos Miguel Jenkins Perez]
- Because this uses docker and thus it takes too much time to run a
  topology test and because some tests do not implement the rollback I
  setup pytest to exit at first failure. [Carlos Miguel Jenkins Perez]
- Changed the approach to build network interfaces, now the platform
  does it instead of the nodes. [Carlos Miguel Jenkins Perez]
- Improved error handling when a build command fails and set the bash
  terminal to dumb as default to avoid issues with control characters.
  [Carlos Miguel Jenkins Perez]
- Asserting success of the build commands to avoid passing an badly
  built engine node. [Carlos Miguel Jenkins Perez]
- Removed deprecated attribute delay in DockerShell. [Carlos Miguel
  Jenkins Perez]
- Refactored the initialization procedure for OpenSwitch node. [Carlos
  Miguel Jenkins Perez]
- Refactored the DockerNode to be an abstract class and created a new
  HostNode. [Carlos Miguel Jenkins Perez]
- Changed the whole shell communication process so it doesn't use waits
  for the output and is reliable. [Carlos Miguel Jenkins Perez]
- Moved iface_name function into a utils module to remove a circular
  dependency. [Carlos Miguel Jenkins Perez]
- Added documentation placeholders. [Carlos Miguel Jenkins Perez]
- Moved the base docker node out of the platform module into a new
  submodule inside node. [Carlos Miguel Jenkins Perez]
- Refactored topology_docker to remove OpenSwitch specific logic.
  [Carlos Miguel Jenkins Perez]
- Renamed test for module to match policy. [Carlos Miguel Jenkins Perez]
- Removed graphviz installation instructions as the tox doesn't use the
  autoplot flags. [Carlos Miguel Jenkins Perez]
- Changed logic to create interfaces as fp{num} temporarily. [Carlos
  Miguel Jenkins Perez]
- Convert bytestring from console output to UTF8 by default. (This can
  byte later) [Carlos Miguel Jenkins Perez]
- Minimal changes on testsuite. [David Diaz]
- Replace uses of call for proper send_command. [David Diaz]
- Update internal documentation. [David Diaz]

Fix
~~~
- Renamed test to match naming standard. [Carlos Miguel Jenkins Perez]
- Fixed all un-asserted commands to be asserted using assert_batch.
  [Carlos Miguel Jenkins Perez]
- Normalized documentation as per peer review request. [Carlos Miguel
  Jenkins Perez]
- Replaced all manual docker exec calls to use the private _docker_exec
  method. [Carlos Miguel Jenkins Perez]
- Fixing style in documentation and some minor formatting issues.
  [Carlos Miguel Jenkins Perez]
- Fixed documentation, dead code, and inconsistent and bad use of
  keyword arguments. [Carlos Miguel Jenkins Perez]
- Removed unused constructor params and changed container docker execs
  to use check_call/check_output/Popen. [valverdi]
- Fixed some small error in the documentation. [valverdi]
- Update code to work with changes on master. [David Diaz]
- Make changes according to review on #2. [David Diaz]
- Adding timeouts for openswitch script. [Diego Antonio Hurtado
  Pimentel]
- Bring-up interfaces AFTER resuming the node. [Carlos Miguel Jenkins
  Perez]
- To stop networking on pause/unpause now all interfaces of a enode are
  set up/down. [Carlos Miguel Jenkins Perez]
- Fixed a race condition in where a shell was started, expected and
  prompt, but the hostname wasn't final and thus the initial prompt
  never matched. [Carlos Miguel Jenkins Perez]
- Added clean-up for the linked netns. [Carlos Miguel Jenkins Perez]
- Fixed the ping test to now only use normal host nodes to avoid weird
  failures caused by openswitch images. [Carlos Miguel Jenkins Perez]
- Allow to set image explictly and do not override with environment.
  Environment only must override the default image. [Carlos Miguel
  Jenkins Perez]
- Fixed minor documentation issue. [Carlos Miguel Jenkins Perez]
- Fixed yet another trailing whitespace in commands. [Carlos Miguel
  Jenkins Perez]
- Removing trailing whitespaces in some commands. [Carlos Miguel Jenkins
  Perez]
- Implemented the rollback hook in docker platform. [Carlos Miguel
  Jenkins Perez]
- Finished pending documentation. [Carlos Miguel Jenkins Perez]
- Fixed ping test to use ip command. [Carlos Miguel Jenkins Perez]
- Fix bugs in refactors. [David Diaz]
- Added a default 'host' type that can be easily overriden by a plugin.
  [Carlos Miguel Jenkins Perez]
- Fixed missing documentation in code and documentation. [Carlos Miguel
  Jenkins Perez]
- It is no longer required to run the topology platform as root. [Carlos
  Miguel Jenkins Perez]
- Set the docker topology platform as default. [Carlos Miguel Jenkins
  Perez]
- Correct netns on test ping. [David Diaz]
- Fixed bad default shell for some commands. [Carlos Miguel Jenkins
  Perez]
- Fixed copy-paste ups with platform key. [Carlos Miguel Jenkins Perez]
- Added DockerPlatform to topology entrypoint. [Carlos Miguel Jenkins
  Perez]
- Fixed hardwired image identifier. [Carlos Miguel Jenkins Perez]
- Fixed default shell inheritance and bad named attribute. [Carlos
  Miguel Jenkins Perez]
- Link wasn't going up. [David Diaz]
- Minimal change on test to support python3. [David Diaz]

Other
~~~~~
- Merge pull request #17 from hpe-networking/ops_oobm. [Carlos Miguel
  Jenkins Perez]

  chg: dev: Avoid moving new oobm interface to swns namespace
- Merge pull request #15 from hpe-networking/after_autopull. [David Diaz
  Barquero]

  Refactored code, fixed minor issues and code quality.
- Merge pull request #7 from hpe-networking/docker_auto_pull. [David
  Diaz Barquero]

  new: usr: Added a new auto-pull feature that automatically download any Docker image required.
- Merge pull request #12 from hpe-networking/host_image_bug. [Carlos
  Miguel Jenkins Perez]

  dev: fix: Fixing image passing.
- Dev: fix: Fixing image passing. [Diego Antonio Hurtado Pimentel]
- Merge pull request #8 from hpe-networking/docker_tmp. [David Diaz
  Barquero]

  Mapping port to port labels for openswitch in topology
- Merge pull request #4 from hpe-networking/send_command_to_docker_exec.
  [David Diaz Barquero]

  chg: dev: Refactored all send_commands to docker_exec to avoid using pexpect.
- Merge pull request #1 from hpe-networking/openvswitch_node. [Carlos
  Miguel Jenkins Perez]

  new: dev: Adding p4switch, openvswitch and ryu node types.
- Add: dev: Added tests and some metadata options. [valverdi]
- Add: dev: Adding supervisor support, waits and some tests. [valverdi]
- Add: dev: Adding p4 switch test. [valverdi]
- Add: dev: Adding some openvswitch tests. [valverdi]
- Merge pull request #3 from hpe-networking/dockerfiles. [Carlos Miguel
  Jenkins Perez]

  new: dev: Add docker file for toxin node
- Merge pull request #2 from hpe-networking/toxin. [Carlos Miguel
  Jenkins Perez]

  new: dev: Added a Toxin node for packet generation.
