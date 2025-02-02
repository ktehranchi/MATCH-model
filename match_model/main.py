# Copyright (c) 2015-2019 The Switch Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0, which can be found at http://www.apache.org/licenses/LICENSE-2.0.

"""Script to handle match <cmd> calls from the command line."""
from __future__ import print_function

import sys, os
import match_model

# print "running {} as {}.".format(__file__, __name__)


def main():
    cmds = ["solve", "solve-scenarios", "test", "--version"]
    if len(sys.argv) >= 2 and sys.argv[1] in cmds:
        # If users run a script from the command line, the location of the script
        # gets added to the start of sys.path; if they call a module from the
        # command line then an empty entry gets added to the start of the path,
        # indicating the current working directory. This module is often called
        # from a command-line script, but we want the current working
        # directory in the path because users may try to load local modules via
        # the configuration files, so we make sure that's always in the path.
        sys.path[0] = ""

        # adjust the argument list to make it look like someone ran "python -m <module>" directly
        cmd = sys.argv[1]
        sys.argv[0] += " " + cmd
        del sys.argv[1]
        if cmd == "--version":
            print("MATCH model version " + match_model.__version__)
            return 0
        if cmd == "solve":
            from .solve import main
        elif cmd == "solve-scenarios":
            from .solve_scenarios import main
        elif cmd == "test":
            from .test import main
        main()
    else:
        print(
            "Usage: {} {{{}}} ...".format(
                os.path.basename(sys.argv[0]), ", ".join(cmds)
            )
        )
        print("Use one of these commands with --help for more information.")


if __name__ == "__main__":
    main()
