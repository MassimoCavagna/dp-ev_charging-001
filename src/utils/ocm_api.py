import json
import requests
import yaml
from utils.config import load_ocm_base_url, load_ocm_raw_json_path

def download_ocm_poi_data(params: dict):
    OCM_BASE_URL = load_ocm_base_url()
    try:
        r = requests.get(OCM_BASE_URL, params=params, timeout=300)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    return r.json()

def write_poi_data_to_file(pois: dict, run_id: int):
    OCM_RAW_JSON_FILE = load_ocm_raw_json_path()
    with open (f"{OCM_RAW_JSON_FILE}/pois_italy_{run_id}.json", 'w') as f:
        json.dump(pois, f)