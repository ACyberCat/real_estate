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
        jason = '{"property names" : ['
        estate_properties = http.request.env["estate.properties"]
        property_ids = estate_properties.search([])
        for propertee in property_ids:
            _logger.info(propertee.name)
            if jason != '{"property names" : [':
                jason += ", "
            jason += '"' + propertee.name + '"'
            _logger.info(jason)
        jason += "]}"
        json.dumps(jason)
        _logger.info(jason)
        return jason

    # exists method
    @http.route("/my_url/another_html", type="http")
    def another_html(self):
        jason = '{"exists" : '
        estate_properties = http.request.env["estate.properties"]
        property_ids = estate_properties.search([("name", "=", "Big Villa")])
        if property_ids.exists():
            jason += "true"
        else:
            jason += "false"
        jason += "}"
        json.dumps(jason)
        _logger.info(jason)
        return jason

    # create new property
    @http.route("/my_url/create_property", type="http")
    def create_property(self):
        jason = '{"create" : '
        estate_properties = http.request.env["estate.properties"]
        property_ids = estate_properties.search([("name", "=", "Small Villa")])
        if property_ids.exists():
            jason += "false"
        else:
            estate_properties.create(
                {
                    "name": "Small Villa",
                    "expected_price": "15000",
                    "property_type_id": "2",
                }
            )
            jason += "true"
        jason += "}"
        json.dumps(jason)
        _logger.info(jason)
        return jason

    # update property
    @http.route("/my_url/update_property", type="http")
    def update_property(self):
        jason = '{"update" : '
        estate_properties = http.request.env["estate.properties"]
        property_ids = estate_properties.search([("name", "=", "Small Villa")])
        if property_ids.exists():
            property_ids.write({"expected_price": "20000"})
            jason += "true"
        else:
            jason += "false"
        jason += "}"
        json.dumps(jason)
        _logger.info(jason)
        return jason

    # delete property
    @http.route("/my_url/delete_property", type="http")
    def delete_property(self):
        jason = '{"delete" : '
        estate_properties = http.request.env["estate.properties"]
        property_ids = estate_properties.search([("name", "=", "Small Villa")])
        if property_ids.exists():
            property_ids.unlink()
            jason += "true"
        else:
            jason += "false"
        jason += "}"
        json.dumps(jason)
        _logger.info(jason)
        return jason

    # duplicate property
    @http.route("/my_url/duplicate_property", type="http")
    def duplicate_property(self):
        jason = '{"duplicate" : '
        estate_properties = http.request.env["estate.properties"]
        property_ids = estate_properties.search([("name", "=", "Small Villa")])
        if property_ids.exists():
            property_ids.copy()
            jason += "true"
        else:
            jason += "false"
        jason += "}"
        json.dumps(jason)
        _logger.info(jason)
        return jason

    # post request reciever
    @http.route("/my_url/post_request", type="json", auth="public", methods=["POST"])
    def post_request(self, **kwargs):
        _logger.info(http.request.params)
        return {"success": True, "status": "OK", "code": 200}

    @http.route("/my_url/some_json", type="json")
    def some_json(self):
        jason = json.dumps({"sample_dictionary": "This is a sample JSON dictionary"})
        return jason
