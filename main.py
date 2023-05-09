# Global Imports
import requests


# Local Imports
import um_auth # API Authentication
import um_store # Storage for variables
import um_materials # API Materials functions
import um_printer # API Printer Functions
import um_network # API Networking Functions
import um_printjob # API Current Print Job Functions
import um_system # API System Functions
import um_history # API History Functions
import um_camera # API Camera Functions


# Load

def __init__():
    # Run auth commands here?
    
    pass

# Functions

def get_url_by_name(name):
    url = um_store.url_open
    printer_loc = um_store.PRINTERS_BY_NAME.index(name)
    
    if printer_loc == -1: return False
    
    url += um_store.PRINTERS_BY_IP[printer_loc]
    url += um_store.url_api
    
    return url