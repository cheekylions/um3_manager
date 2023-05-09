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


def get_material_by_guid(url, material_guid):
    url += (url_leader + "/" + material_guid)
    
    response = requests.get(url)
    assert response.status_code == httpx.codes.ok
    
    return response.content


