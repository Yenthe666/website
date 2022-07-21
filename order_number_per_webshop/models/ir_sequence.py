from odoo import api, models


class IrSequence(models.Model):
    _inherit = "ir.sequence"

    def next_by_code(self, sequence_code, sequence_date=None):
        """
        Check if a certain sequence is present in the context and use that one if set.
        """
        sequence = self.env.context.get("sequence_id", False)
        if sequence:
            return sequence.sudo().next_by_id(sequence_date=sequence_date)
        return super(IrSequence, self).next_by_code(sequence_code, sequence_date)
