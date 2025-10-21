from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class NovaSupportTicket(models.Model):
    _name = "nova.support.ticket"
    _description = "Nova Support Ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"

    name = fields.Char(string="Ticket", required=True, copy=False, readonly=True, default="New")
    partner_id = fields.Many2one("res.partner", string="Customer", required=True, index=True, tracking=True)
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company)

    email = fields.Char(string="Email", help="Contact email of the reporter")
    phone = fields.Char(string="Phone")

    subject = fields.Char(string="Subject", required=True, tracking=True)
    description = fields.Text(string="Description", tracking=True)

    priority = fields.Selection(
        [
            ("0", "Low"),
            ("1", "Normal"),
            ("2", "High"),
            ("3", "Urgent"),
        ],
        string="Priority",
        default="1",
        tracking=True,
    )

    state = fields.Selection(
        [
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("waiting", "Waiting"),
            ("done", "Solved"),
            ("cancel", "Cancelled"),
        ],
        default="new",
        tracking=True,
    )

    attachment_ids = fields.Many2many("ir.attachment", string="Attachments")

    @api.model
    def create(self, vals):
        if vals.get("name") in (False, "New"):
            vals["name"] = self.env["ir.sequence"].next_by_code("nova.support.ticket") or "New"
        rec = super().create(vals)
        template = self.env.ref("nova_support.mail_template_ticket_created", raise_if_not_found=False)
        if template:
            template.send_mail(rec.id, force_send=True)
        return rec
