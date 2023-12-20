#scr_main.py
#kevin fink
#kevin@shorecode.org
#Oct 7 2023

from pygame import mixer
import scr_gui as scg

def music():
    """
    This function loads a mp3 file and uses the pygame mixer to play it back through local speakers
    
    Returns:
    Does not return
    """
    mixer.init()
    mixer.music.load('05_busy-child-hyper-remix.mp3')
    mixer.music.play()

# Starts playing background music
music()

# Creates GUI class instance
gui = scg.ScrGui()

# Creates the main window and runs the GUI logic
gui.create_root()
