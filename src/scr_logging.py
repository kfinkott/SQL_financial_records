#scr_logging.py
#kevin fink
#kevin@shorecode.org
#Oct 7 2023

import logging
import os

def set_logging(name, filename):
    """
    Creates the logger and configures the options
    
    Args:
    name ( _obj_ ) : Name for the logger
    filename ( _obj_ ) : Filename to write the log output to
    
    Returns:
    Does not return
    """
    
    # Checks for a logging directory and creates one if it does not exist
    if not os.path.isdir('logging'):
        os.mkdir('logging')
        
    # Create a logger
    logger = logging.getLogger(name)
    
    # Set up logging configuration
    logging.basicConfig(filename=f'logging/{filename}', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Create a file handler
    console_handle = logging.StreamHandler()
    
    # Add the file handler to the logger
    logger.addHandler(console_handle)

    return logger

