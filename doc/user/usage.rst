.. _usage-label:

Using MP3-Monitoring
====================

The program is a terminal program, so it runs from the terminal.

Calling with:

.. code-block:: none

    mp3monitoring

Furthermore, there are additional arguments:

.. option:: -h, --help

    show this help message and exit

.. option:: -v, --version

    show program's version number and exit

.. option:: --j, --job source target sleep

    Will add this job to the monitor list.
    source: source directory
    target: target directory
    sleep: sleep time between scanning in seconds
    recursive: ['True', 'False'] scan source folder recursively

.. option:: --reset_times

    Reset the latest check time from configuration.

.. option::--ignore_config

    Will not load or save the config file.

.. option:: --gui

   Open the gui.
