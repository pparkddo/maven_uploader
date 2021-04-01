# maven_uploader
로컬환경에서 [Nexus maven repository](https://www.sonatype.com/product/repository-oss)로 대량의 artifact 들을 업로드하는 스크립트입니다. [일반 maven repository](https://repo1.maven.org/maven2/)를 이용하지 못하는 환경(폐쇄망 등)에서 내부 nexus 저장소로 artifact 를 업로드하는 데 사용할 수 있습니다.

## Feature
- nexus 에서 제공하는 `rest api` 를 이용합니다.
- 업로드용 cli 를 제공합니다.
- 업로드 속도 향상을 위해 `ThreadPoolExecutor` 를 사용합니다.

## Environment
- Python 3.7
- Nexus 3.x

## Installation
```
git clone https://github.com/pparkddo/maven_uploader.git
pip install -r maven_uploader/requirements.txt
```

## Example
```
python -m maven_uploader -url http://test-repo/repository/maven-releases/ -userid admin -password admin123 -path C:\Users\Test\.m2\repository
```
cli 파라미터에 대한 설명은 `-h` 옵션으로 확인할 수 있습니다.

## Reference
- https://help.sonatype.com/repomanager3/rest-and-integration-api/components-api