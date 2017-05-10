import argparse


class Executor:
    """This is the main driver class for the program. It handles argument
    parsing, among other things"""

    def __init__(self):
        """This constructor initializes the class appropriately"""
        self._prepare_args()

    def _prepare_args(self):
        """This private method preps the args parser"""
        args_parser = argparse.ArgumentParser(
            description="This program will execute the Jobe logic, "
                        "either in simulation or real mode")
        args_parser.add_argument("mode",
                                 choices=[
                                     "run_simulation",
                                     "execute"
                                 ],
                                 help="Indicate the execution mode")
        self._args = args_parser.parse_args()

    def initiate_process(self):
        if self._args.mode == "run_simulation":
            print("simulation")
        if self._args.mode == "execute":
            print("execute")
