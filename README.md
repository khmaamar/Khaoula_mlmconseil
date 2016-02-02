
################################################################################
                                                                              
                        Module [Total en lettres]                         
                    ----------------------------------                        
                      permet d'ajouter une convertion                         
                        du total en lettres (Devis et Facture)                           
                    ----------------------------------                        
                                                                              
                       langage : Python 2.7                                   
                       date creation : 01/01/2016                            
                       date modification : 04/01/2016                         
                       version : 0.1                                          
                       auteur  : MLMConseil                              
                                                                              
################################################################################


# Total en lettres
Total des devis et factures en lettres (Dinar Algérien)

-------------------------
Le module permet d'ajouter un champ amount_total_text dans la table sale_order,
ou on sauvegarde le total en lettres (arrêté le présent  devis a la somme de ....) 
après sa conversion(conversion.py)
le module hérite de la vue  sale_order_view.xml , et le rapport views/report_saleorder.xml

-------------------------
Le module permet d'ajouter un champ amount_total_text dans la table account_invoice,
ou on sauvegarde le total en lettres (arrêtée la présente facture a la somme de ....) 
après sa conversion(conversion.py)
le module hérite de la vue  report_invoice_view.xml , et le rapport views/report_invoice.xml
