from glob import glob
from os.path import dirname, join

import requests


def upload_component(url, user_id, password, pom_name: str, jar_name: str = None) -> None:
    files = {"maven2.asset1": open(pom_name, "rb")}
    data = {"maven2.asset1.extension": "pom"}
    if jar_name:
        files["maven2.asset2"] = open(jar_name, "rb")
        data["maven2.asset2.extension"] = "jar"
    response = requests.post(
        url,
        auth=(user_id, password),
        files=files,
        data=data
    )
    return response.text


def get_jar_name(pom_name_with_path: str) -> str:
    jar_names = glob(join(dirname(pom_name_with_path), "*.jar"))
    if len(jar_names) >= 2:
        raise ValueError("Jar 파일이 2개 이상 존재합니다")
    return jar_names[0] if jar_names else None
 

def retrieve_components(url, user_id, password) -> dict:
    response = requests.get(url, auth=(user_id, password))
    return response.json()["items"]
