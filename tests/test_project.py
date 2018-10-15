# coding: utf-8

import unittest
import httpretty
import json
from backlog.util import load_conf
from backlog.base import BacklogAPI

API_ENDPOINT = "https://{space}.backlog.jp/api/v2/{uri}"


class TestProject(unittest.TestCase):
    def setUp(self):
        self.conf = load_conf("./conf.default.yml")["backlog"]
        self.api = BacklogAPI(self.conf["space"], self.conf["api_key"])
        self.space = self.conf["space"]
        self.api_key = self.conf["api_key"]

    def test_list(self):
        pass

    def test_create(self):
        pass

    def test_get(self):
        pass

    def test_update(self):
        pass

    @httpretty.activate
    def test_users(self):
        # Project id given
        _projectIdOrKey = str(1000)

        expects = [
            {
                "id": 1,
                "userId": "admin",
                "name": "admin",
                "roleType": 1,
                "lang": "ja",
                "mailAddress": "eguchi@nulab.example"
            },
        ]

        httpretty.register_uri(
            httpretty.GET,
            API_ENDPOINT.format(
                space=self.space ,
                uri="projects/{projectIdOrKey}/users".format(projectIdOrKey=_projectIdOrKey)),
            body=json.dumps(expects)
        )

        resp = self.api.project.users(projectIdOrKey=_projectIdOrKey)
        self.assertEqual(expects, resp.json())

        # Project key given
        _projectIdOrKey = "sample"

        httpretty.register_uri(
            httpretty.GET,
            API_ENDPOINT.format(
                space=self.space,
                uri="projects/{projectIdOrKey}/users".format(projectIdOrKey=_projectIdOrKey)),
            body=json.dumps(expects)
        )

        resp = self.api.project.users(projectIdOrKey=_projectIdOrKey)
        self.assertEqual(expects, resp.json())


if __name__ == "__main__":
    unittest.main(warnings='ignore')