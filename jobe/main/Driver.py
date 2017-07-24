import argparse
from jobe.main.Logger import Logger
from jobe.simulator.Simulator import Simulator
from jobe.simulator.ManualAI import ManualAI
from jobe.simulator.AutomaticAI import AutomaticAI
from jobe.real.Real import Real
from jobe.real.Wheels import Wheels


class Driver:
    """This class bootstraps everything so we're ready to go"""

    def __init__(self):
        """This constructor initializes the class appropriately"""
        self._prepare_args()
        self._prepare_logger()

    def _prepare_args(self):
        """This private method preps the args parser"""
        args_parser = argparse.ArgumentParser(
            description="This program will execute the Jobe logic, "
                        "either in simulation or real mode")

        # Add the mode argument
        args_parser.add_argument("mode",
                                 choices=[
                                     "manual_simulation",
                                     "simulation",
                                     "real"
                                 ],
                                 help="Indicate the execution mode")

        # Parse whatever the user has sent in
        self._args = args_parser.parse_args()

    def _prepare_logger(self):
        """This private method will get the logger up and running"""
        self._logger = Logger()

    def drive(self):
        """This method is the logical entry point for the class"""
        if self._args.mode == "manual_simulation":
            self._logger.write_to_log("Executing in manual simulation mode")

            # Execute the simulator in manual mode
            simulator = Simulator(ManualAI(self._logger))
            simulator.run()

        if self._args.mode == "simulation":
            self._logger.write_to_log("Executing in simulation mode")

            # Execute the simulator in automatic mode
            simulator = Simulator(AutomaticAI(self._logger))
            simulator.run()

        if self._args.mode == "real":
            self._logger.write_to_log("Executing in real mode")

            # Delay the imports to here, so code still runs on non-Pi computers
            from jobe.real.Camera import Camera
            from jobe.real.RealAI import RealAI

            # Execute the program in real-world mowing mode
            real = Real(RealAI(
                self._logger),
                Camera(self._logger),
                Wheels(self._logger)
            )
            real.run()

        # Close the logger now that we're done
        self._logger.close_log()
