import argparse
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait
from glob import glob
from os.path import join

from .api import get_jar_name, upload_component


def _upload(url, user_id, password, pom_name_with_path, jar_name_with_path):
    print(f"Start uploading {pom_name_with_path}")
    upload_component(url, user_id, password, pom_name_with_path, jar_name_with_path)
    print(f"Completely upload {pom_name_with_path}")


def parse_args():
    parser = argparse.ArgumentParser(description="Nexus repository 에 pom과 jar 파일을 대량 업로드 합니다")
    parser.add_argument("-url", required=True, help="Nexus repository URL")
    parser.add_argument("-userid", required=True, help="Nexus 에 접속할 사용자 아이디")
    parser.add_argument("-password", required=True, help="Nexus 에 접속할 사용자 비밀번호")
    parser.add_argument("-path", required=True, help="업로드할 파일이 있는 로컬 경로")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    url = args.url
    user_id = args.userid
    password = args.password
    path = args.path

    pom_names_with_path = glob(join(path, "**/*.pom"), recursive=True)
    jar_names_with_path = [get_jar_name(pom_name_with_path) for pom_name_with_path in pom_names_with_path]

    print("Upload files...")
    print(f"pom: {len(pom_names_with_path)}")
    print(f"jar: {len(list(filter(lambda x: x, jar_names_with_path)))}")

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(_upload, url, user_id, password, pom_name_with_path, jar_name_with_path)
            for pom_name_with_path, jar_name_with_path in zip(pom_names_with_path, jar_names_with_path)
        ]
        wait(futures, return_when=ALL_COMPLETED)
