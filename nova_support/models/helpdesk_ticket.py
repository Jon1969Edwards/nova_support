from odoo import api, fields, models

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    phone = fields.Char(string="Phone")
    company_name = fields.Char(string="Company Name")
    cc_emails = fields.Char(string="CC Emails",
                            help="Comma-separated emails to follow the ticket.")

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if rec.cc_emails:
                emails = [e.strip() for e in rec.cc_emails.split(",") if e.strip()]
                for em in emails:
                    partner = self.env["res.partner"].sudo().search([("email","=",em)], limit=1)
                    if not partner:
                        partner = self.env["res.partner"].sudo().create({"name": em.split("@")[0], "email": em})
                    rec.message_subscribe(partner_ids=[partner.id])
        return records
