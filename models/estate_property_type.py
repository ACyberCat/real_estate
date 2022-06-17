from odoo import fields, models, api


# create a new model estate.property.type
class RealEstatePropertyType(models.Model):
    # database table name
    _name = "estate.property.type"
    # description of the model
    _description = "Real Estate Property types Model"
    # order of viewing the records
    _order = "name desc"

    # fields of the model
    name = fields.Char(required=True)
    # manytoone relationship with estate.properties
    property_ids = fields.One2many('estate.properties', 'property_type_id')
    sequence = fields.Integer(string='Sequence', default=10,
                              help="Gives the sequence order when "
                              "displaying a list of property types.")
    # one2many relationship with estate.property.offer
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    # compute field to get the number of properties of a type
    offer_count = fields.Integer(string='Offers',
                                 compute='_compute_offer_count')
    sequence = fields.Integer(string='Sequence', default=10)

    @api.depends('offer_ids')
    # compute field to get the number of properties of a type
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    # does nothing
    def do_nothing(self):
        pass
