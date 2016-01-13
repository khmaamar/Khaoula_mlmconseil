# -*- coding: utf-8 -*-
################################################################################
#                                                                              
#                        Module [Total en lettres]                         
#                    ----------------------------------                        
#                      permet d'ajouter une convertion                         
#                        du total en lettres (Devis et Facture)                           
#                    ----------------------------------                        
#                                                                              
#                       langage : Python 2.7                                   
#                       date creation : 01/01/2016                            
#                       date modification : 04/01/2016                         
#                       version : 0.1                                          
#                       auteur  : MLMConseil                              
#                                                                              
################################################################################
from openerp.osv import fields, osv
import conversion

class sale_order(osv.Model):
    _inherit = 'sale.order'
    _name = 'sale.order'
    _description = "le modele ajoute le total d'un devis en lettres"


    def _amount_all_text(self, cr, uid, ids, field_name, arg, context=None):
        return self._amount_all(cr, uid, ids, field_name, arg, context=context)

    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = {
                'amount_untaxed': 0.0,
                'amount_tax': 0.0,
                'amount_total': 0.0,
                'amount_total_text':'arrete le devis a la somme de zero dinars'
            }
            val = val1 = 0.0
            cur = order.pricelist_id.currency_id
            for line in order.order_line:
                val1 += line.price_subtotal
                val += self._amount_line_tax(cr, uid, line, context=context)
            res[order.id]['amount_tax'] = cur_obj.round(cr, uid, cur, val)
            res[order.id]['amount_untaxed'] = cur_obj.round(cr, uid, cur, val1)
            res[order.id]['amount_total'] = res[order.id]['amount_untaxed'] + res[order.id]['amount_tax']
            res[order.id]['amount_total_text'] = conversion.convertir_dev(res[order.id]['amount_total'])
        return res

    _columns = {

        'amount_total_text': fields.function(_amount_all_text, string='total en lettres', type='text',store={
            'sale.order': (lambda self, cr, uid, ids, c={}: ids, ['order_line'], 10),
            },
            multi='sums', help="Total en lettres"),

    }