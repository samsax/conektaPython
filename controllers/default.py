# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import conekta
import jsonpickle

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    conekta.api_key = "key_SRxjoEZ3jbjv5FiPh3HHxQ"
    conekta.api_version = "2.0.0"
    order = conekta.Order.create({
          "line_items": [{
              "name": "Tacos",
              "unit_price": 1000,
              "quantity": 12,
              'antifraud_info' : {
			          'trip_id'        : '12345',
			          'driver_id'      : 'driv_1231',
			          'ticket_class'   : 'economic',
			          'pickup_latlon'  : '23.4323456,-123.1234567',
			          'dropoff_latlon' : '23.4323456,-123.1234567'
			      			},
          },
          ],
          "currency": "MXN",
          "customer_info": {
            "name": "Fulanito Pérez",
            "email": "fulanito@conekta.com",
            "phone": "+5218181818181",
            "antifraud_info":{
		        "account_created_at":1484040996,
		        "first_paid_at": 1485151007, 
		        "paid_transactions": 4
		    }
          },
          "charges":[{
            "payment_method": {
              "type": "oxxo_cash"
            }
          }]
        })
    print("ID: " + order.id)
    #print(order.line_items.data[0].quantity + " - "+ order.line_items.data[0].name + " - "+ (order.line_items.data.unit_price/100))
    response.flash = T(order.id)
    return jsonpickle.encode(order)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


