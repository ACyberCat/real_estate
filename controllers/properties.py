from cgitb import reset
import re
from odoo import http
from odoo.http import request
import json
import logging
import sys

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s", "%m-%d-%Y %H:%M:%S"
)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler(
    "C:/Program Files/odoo15/server/odoo/addons/real_estate/controllers/logs.txt"
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

_logger.addHandler(file_handler)
_logger.addHandler(stdout_handler)


class MyController(http.Controller):
    # return json array of properties
    @http.route("/my_url/some_html", type="http")
    def some_html(self):
        parser=['name','description','expected_price']
        here = http.request.env["estate.properties"].search([])
        jason = here.jsonify(parser)
        _logger.info(jason)
        return json.dumps(jason)

    @http.route("/my_url/some_json", type="json")
    def some_json(self):
        jason = json.dumps({"sample_dictionary": "This is a sample JSON dictionary"})
        return jason
