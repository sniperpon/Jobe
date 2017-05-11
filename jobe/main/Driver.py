import argparse
from jobe.main.Logger import Logger
from jobe.main.Brain import Brain
from jobe.virtual.Stopover import StopOver
from jobe.eyes.SimulationCamera import SimulationCamera
from jobe.eyes.RealCamera import RealCamera
from jobe.legs.SimulationMover import SimulationMover
from jobe.legs.RealMover import RealMover



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
        if self._args.mode == "simulation":
            self._logger.write_to_log("Executing in simulation mode")

            # Prepare the simulation module instances
            yard = StopOver()
            brain = Brain(
                self._logger,
                SimulationCamera(yard),
                SimulationMover(yard)
            )

        if self._args.mode == "real":
            self._logger.write_to_log("Executing in real mode")

            # Prepare the actual execution module instances
            brain = Brain(self._logger, RealCamera(), RealMover())

        # Kick off the main loop!
        brain.loop()

        # Close the logger now that we're done
        self._logger.close_log()
