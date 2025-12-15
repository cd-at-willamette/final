from pgl import GWindow, GImage
from ColorObj import ColorObj

# For your convenience - 700 worked well for me
GWINDOW_SIZE = 700
MAX_BRIGHTNESS = 255

# For your convenience - the URL of rbgs.json
URL = "https://cd-public.github.io/courses/cs1/exams/rgbs.json"

gw = GWindow(GWINDOW_SIZE, GWINDOW_SIZE)

# Main Function
def flag(region):
    # This sample code creates a pixel array that is uninitialized
    # TODO: Update the body of this function to create a flag
    # Prob0: Implemement "read_rgbs" and update ColorObj.
    # Prob1: I recommend calculations over the window size and the number of colors.
    # Prob2: I recommend a dictionary of colors-to-ints that are incorporated into Prob0 calcs.
    #        You will need to use the "region" argument for this problem.
    # Prob3: Update ColorObj
    # Prob4: Update ColorObj
    rojo = ColorObj(None)
    parr = [[rojo.get_color_at(row,col) for row in range(GWINDOW_SIZE)] for col in range(GWINDOW_SIZE)]
    return parr

# Helper Function
# Likely useful in Prob0
def read_rgbs():
    return

gw.add(GImage(flag('Qullasuyu')))

