import json
import requests
import yaml
from config import load_ocm_base_url

def download_ocm_poi_data(params: dict):
    OCM_BASE_URL = load_ocm_base_url()
    r = requests.get(OCM_BASE_URL, params=params, timeout=300)
    r.raise_for_status()
    return r.json()