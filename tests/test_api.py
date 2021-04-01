import unittest
from os.path import join

from maven_uploader.api import get_jar_name


def get_test_path():
    import os
    return os.path.dirname(os.path.realpath(__file__))


class ApiTest(unittest.TestCase):

    def test_get_jar_name(self):
        test_repository_path = join(get_test_path(), "resources", "repository", "com", "test")

        # pom 이름과 jar 이름이 같은 경우
        pom1_path = join(test_repository_path, "a", "1.0.0")
        pom1 = join(pom1_path, "a-1.0.0.pom")
        self.assertEqual(get_jar_name(pom1), join(pom1_path, "a-1.0.0.jar"))

        # pom 이름과 jar 이름이 다른 경우
        pom2_path = join(test_repository_path, "b", "2.0.0")
        pom2 = join(pom2_path, "b-test-2.0.0.pom")
        self.assertEqual(get_jar_name(pom2), join(pom2_path, "b-2.0.0.jar"))
            
        # pom 파일만 있는 경우
        pom3_path = join(test_repository_path, "c", "3.0.0")
        pom3 = join(pom3_path, "c-3.0.0.pom")
        self.assertEqual(get_jar_name(pom3), None)
