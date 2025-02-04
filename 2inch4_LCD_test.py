import logging
import time

import spidev as SPI
from PIL import Image, ImageDraw, ImageFont

from display import LCD_2inch4

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
logging.basicConfig(level=logging.DEBUG)
try:
    # display with hardware SPI:
    """Warning!!!Don't  creation of multiple displayer objects!!!"""
    # disp = LCD_2inch4.LCD_2inch4(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_2inch4.LCD_2inch4()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    img = Image.open("project_image.png")
    img = img.rotate(270)
    disp.ShowImage(img)
    time.sleep(10)
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
