# Import
import requests
import httpx

# Constants
url_leader = "materials"


def get_all_materials(url):
    url += url_leader
    
    response = requests.get(url)
    assert response.status_code == httpx.codes.ok
    
    return response.content