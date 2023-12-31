#env_key.py
#kevin fink
#kevin@shorecode.org
#Sept 24 2023

from cryptography.fernet import Fernet
import os
import getpass
from typing import Union

def save_key(env_var: str) -> Fernet.generate_key:
    """
    Saves a generated encryption key to Linux environment variables
    
    Args:
    env_var (str) : Name of the environment variable
    
    Returns:
    Fernet.generate_key: Returns a string describing the encryption key
    """
    key: str = Fernet.generate_key()
    with open(os.path.expanduser('~/.profile'), 'r') as outfile:
        profile_contents = outfile.readlines()
        with open(os.path.expanduser('~/.profile.bak'), 'w') as fn:
            fn.writelines(profile_contents)        
        for pc in profile_contents:
            if env_var in pc:
                profile_contents.remove(pc)
    with open(os.path.expanduser('~/.profile'), 'w') as outfile:
        profile_contents.append(f'export {env_var}="{key.decode()}"\n')
        outfile.writelines(profile_contents)
    print('You must reload the OS for the new key to be saved properly')
    return key


def get_key(env_var: str) -> str:
    """
    Gets the key from Linux envirionment variables
    
    Args:
    env_var (str) : Name of the environment variable
    
    Returns:
    str: String describing the encryption key
    """
    key: str = os.getenv(env_var)
    return key


def decrypt_passwd(env_var: Union[str, None]=None, passwd: Union[str, None]=None, key: Union[str, None]=None) -> str:
    """
    Decrypts a password using the key stored in environment variables or a supplied key
    
    Args:
    env_var (str=None) : Name of the environment variable
    key (str=None) : String describing the key
    passwd (str=None) : Password to be decrypted
    
    Returns:
    str: Unencrypted password
    """
    print(key)
    if key == None:
        key = os.getenv(env_var)
    if passwd == None:
        passwd = getpass.getpass('Run this script in terminal to hide the password input\nPlease input the password to decrypt:')
    cipher_suite: Fernet = Fernet(key)
    return cipher_suite.decrypt(passwd).decode()

def encrypt_passwd(env_var: Union[str, None]=None, passwd: Union[str, None]=None, key: Union[str, None]=None) -> str:
    """
    Encrypts a password that is provided by manual input (stdin) or a password that is passsed as an argument
    
    Args:
    env_var (str) : Name of the Linux environment variable that contains the key
    passwd (str=None) : String describing the password
    key (str=None) : String describing the key
    
    Returns:
    Returns the encrypted string representing the password
    """    
    if passwd == None:
        passwd = getpass.getpass('Run this script in terminal to hide the password input\nPlease input the password to encrypt:')
    if key == None:
        key = os.getenv(env_var)
    cipher_suite = Fernet(key)
    if len(passwd) > 0:
        return cipher_suite.encrypt(passwd.encode()).decode()
    return ''
