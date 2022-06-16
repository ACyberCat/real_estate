from odoo import fields, models, api


class RealEstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property types Model"
    _order = "name desc"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.properties', 'property_type_id')
    sequence = fields.Integer(string='Sequence', default=10,
                              help="Gives the sequence order when "
                              "displaying a list of property types.")
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    offer_count = fields.Integer(string='Offers',
                                 compute='_compute_offer_count')
    sequence = fields.Integer(string='Sequence', default=10)

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    def do_nothing(self):
        pass
