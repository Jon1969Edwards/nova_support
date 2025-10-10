from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)
_logger.info(">>> NovaSupport controller module imported")

class NovaSupportController(http.Controller):

    @http.route('/nova/ping', type='http', auth='public', website=True)
    def nova_ping(self, **kw):
        return "OK"

    @http.route(['/support'], type='http', auth='public', website=True)
    def support_form(self, **kw):
        # First prove route works
        return "SUPPORT OK"
        # Once confirmed, swap to:
        # teams = request.env['helpdesk.team'].sudo().search([])
        # return request.render('nova_support.support_form',
        #                       {"teams": teams, "values": kw})

    @http.route('/support/create', type='http', auth='public', methods=['POST'], website=True)
    def support_create(self, **post):
        return "CREATE OK"
