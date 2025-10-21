import base64
from odoo import http
from odoo.http import request

class NovaSupportPortal(http.Controller):

    @http.route(['/my/support/tickets', '/my/support/tickets/page/<int:page>'], type='http', auth='user', website=True)
    def my_tickets(self, page=1, **kw):
        partner = request.env.user.partner_id.commercial_partner_id
        Ticket = request.env['nova.support.ticket'].sudo()
        domain = [('partner_id', 'child_of', [partner.id])]
        tickets = Ticket.search(domain, order='id desc')
        values = {'tickets': tickets}
        return request.render('nova_support.portal_my_tickets', values)

    @http.route(['/my/support/tickets/<int:ticket_id>'], type='http', auth='user', website=True)
    def my_ticket_detail(self, ticket_id, **kw):
        ticket = request.env['nova.support.ticket'].sudo().browse(ticket_id)
        return request.render('nova_support.portal_ticket_detail', {'ticket': ticket})

    @http.route(['/my/support/tickets/new'], type='http', auth='public', website=True, csrf=True)
    def new_ticket(self, **post):
        if request.httprequest.method == 'POST':
            user = request.env.user
            partner = user.partner_id if user and user.has_group('base.group_portal') else request.env.ref('base.public_partner')

            vals = {
                'partner_id': partner.id,
                'email': post.get('email') or (partner and partner.email),
                'phone': post.get('phone') or (partner and partner.phone),
                'subject': post.get('subject'),
                'description': post.get('description'),
                'priority': post.get('priority', '1'),
            }
            ticket = request.env['nova.support.ticket'].sudo().create(vals)

            files = request.httprequest.files.getlist('attachments')
            for f in files:
                data = f.read()
                request.env['ir.attachment'].sudo().create({
                    'name': f.filename,
                    'datas': base64.b64encode(data),
                    'res_model': 'nova.support.ticket',
                    'res_id': ticket.id,
                    'mimetype': getattr(f, 'mimetype', False),
                    'type': 'binary',
                })

            return request.redirect(f"/my/support/tickets/{ticket.id}")

        return request.render('nova_support.portal_ticket_create', {})
