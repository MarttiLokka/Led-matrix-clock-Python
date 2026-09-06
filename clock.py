#!/usr/bin/env python
import time
from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT


def main():
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=90, blocks_arranged_in_reverse_order=True)
    device.contrast(10)

    toggle = False  # Toggle the second indicator every half second
    while True:
        toggle = not toggle
        hours = datetime.now().strftime('%H')
        minutes = datetime.now().strftime('%M')
        with canvas(device) as draw:
            text(draw, (0, 1), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (15, 1), ":" if toggle else " ", fill="white", font=proportional(TINY_FONT))
            text(draw, (17, 1), minutes, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.5)


if __name__ == "__main__":
    main()
