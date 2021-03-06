from openerp.osv import osv, fields

class res_partner(osv.Model):
    _inherit = "res.partner"
    
    def _opportunity_meeting_phonecall_count(self, cr, uid, ids, field_name, arg, context=None):
        res = super (res_partner, self)._opportunity_meeting_phonecall_count (cr, uid, ids, field_name, arg, context=None)
        try:
            for partner in self.browse(cr, uid, ids, context):
                if partner.is_company:
                    operator = 'child_of'
                else:
                    operator = '='
                opp_ids = self.pool['crm.lead'].search(cr, uid, [('partner_id', operator, partner.id), ('type', '=', 'opportunity'), ('probability', '<', '100')], context=context)
                res[partner.id] = {
                    'opportunity_count': len(opp_ids),
                    'sd_meeting_count': len(partner.meeting_ids) + len (partner.mapped ('child_ids.meeting_ids')),
                }
        except:
            pass
        return res
    
    _columns = {
        'sd_meeting_count': fields.function(_opportunity_meeting_phonecall_count, string="# Meetings", type='integer', multi='opp_meet'),
    }
    
    def schedule_meeting (self, cr, uid, ids, context=None):
        res = super (res_partner, self).schedule_meeting (cr, uid, ids, context=None)
        ides = list (ids)
        for child in self.pool.get ('res.partner').browse (cr, uid, ids):
            for i in child.child_ids:
                ides.append (i.id)
        res['context']['search_default_partner_ids'] = ides
        return res