from pynq import Overlay, PL
from ws2812.general_const import *

ws2812_overlay = None


class ws2812():
    """Class which controls ws2812 filter hardware

    Attributes
    ----------
    bitfile : str
        Absolute path of bitstream file
    overlay : Overlay
        Gives access to bitstream overlay

    """

    def __init__(self):
        self.bitfile = BITFILE
        if PL.bitfile_name != self.bitfile:
            self.download_bitstream()

    def download_bitstream(self):
        """Download the bitstream

        Downloads the bitstream onto hardware using overlay class.
        Also gives you access to overlay.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        global ws2812_overlay
        ws2812_overlay = Overlay(self.bitfile)
        ws2812_overlay.download()
