from odoo import http
from odoo.http import request
import json


class MyController(http.Controller):
    @http.route("/my_url/some_html", type="http")
    def some_html(self):
        jason = json.dumps ({"template" : """<div><button t-on-click="changeText">Click Me! [uh-oh]</button><strong><t t-esc="state.value" /></strong><h1> YOOOOOOOOOOOOOOOOOOOOOOOO </h1></div>"""})
        return jason

    @http.route("/my_url/some_json", type="json")
    def some_json(self):
        jason = json.dumps ({"sample_dictionary" : "This is a sample JSON dictionary"})
        return jason
