import yaml
import json
import os
from dotenv import load_dotenv, find_dotenv

def load_config_yaml():
    config_yaml = yaml.load(open("../../config.yaml"), Loader=yaml.FullLoader)
    return config_yaml

def load_ocm_base_url():
    config_yaml = load_config_yaml()
    return config_yaml['ocm']['base_url']

def load_ocm_raw_json_path():
    config_yaml = load_config_yaml()
    return config_yaml['paths']['ocm_raw_json_path']

def load_ocm_api_key():
    load_dotenv(find_dotenv(usecwd=True))
    API_KEY = os.environ["OCM_API_KEY"]
    return API_KEY