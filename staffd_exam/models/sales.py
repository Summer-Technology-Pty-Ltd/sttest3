from odoo import models, fields, api, exceptions


class Sales(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def check_customer_action(self):
        if self.partner_id.action == 'warn':
            return {
                'warning': {

                    'title': 'Warning!',
                    'message': 'Warning this customer exceeded his credit limit'}
            }
        elif self.partner_id.action == 'put_on_hold':
            raise exceptions.ValidationError("This customer is on hold!")