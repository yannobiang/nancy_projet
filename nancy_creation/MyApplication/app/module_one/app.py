import os
import sqlite3
import ast
import json
import requests
import json2html
from .formatting_data import extract_data_db
import requests
from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix

import werkzeug
from flask import (
    Flask,
    request,
    render_template,
    url_for,
    redirect
)

import stripe



template_dir = '/home/princeobiang/nancy_creation/MyApplication/app/templates/'
static_dir = '/home/princeobiang/nancy_creation/MyApplication/app/static/'
images = '/home/princeobiang/nancy_creation/MyApplication/app/images/'

app = Flask(__name__, template_folder = template_dir,  static_folder=static_dir
                        )
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51ML83GGkR2DegpH1QL2mvNrUnTXdjKPTKagEgGMyI81TwUFs3n9LkmGSuk63BOiMr87HxKVPtZqdqtwhr5UwSEwC00BODG8H5b'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51ML83GGkR2DegpH1WfxUl9WIatZ1dvnQjNveZlzJwViZQeWXWsC3px5RVyVdPlHBgGZMmXpouklAayDr9pZ5WYHd009XNdKVUi'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/', methods=['GET', 'POST'])

def home():

    """the home page of our site"""
    
    url_image =  'new_logo.jpg' #static_dir
    url = request.url
    text, montant = request.args.get('country'), request.args.get('montant')
    title = "Gabontransmoney"
    print(' ')
    print(montant)
    print(text)
    print('')
    if request.method == "POST":
        data = request.form
        
        print(data)
        print("popo je suis donc dans home")

    return render_template('module_one/index.html',  
                            url_image = url_image
                            )


@app.route('/gabontransmoney/', methods=['GET', 'POST'])
def gabontransmoney():
    
    print(request.args)
    if request.method == "POST":
        data = request.form
        
        print(data)
        print("popo je suis donc dans home")

    return redirect(url_for('home'))



@app.route('/nancyservices/', methods=['GET', 'POST'])
def nancyservices():

    
    title = "La révédélice"
    if request.method == "POST":
        data = request.form
        print(data)
        
    return render_template('module_two/index.html', title = title)


@app.route('/tarifs en Euro/', methods=['GET', 'POST'])
def grille_euro():

    
    # Opening JSON file
    file = os.path.join(static_dir,'myJSON2.json') 
    url_image =  'new_logo.jpg'
    f = open(file)
    
    # returns JSON object as 
    # a dictionary
    data_table1 = json.load(f)
    print(type(data_table1))
    table1 = json2html.json2html.convert(data_table1)
    
    return render_template('module_four/tarif_eur.html', 
                            table1 = table1,
                            url_image =  url_image)




@app.route('/tarifs en Franc/', methods=['GET', 'POST'])
def grille_cfa():


    file = os.path.join(static_dir,'myJSON1.json')
    url_image =  'new_logo.jpg' 

    f = open(file)
    
    # returns JSON object as 
    # a dictionary
    data_table2 = json.load(f)
    
    table2 = json2html.json2html.convert(data_table2)

    return render_template('module_four/tarif_cfa.html', table2 = table2,
                            url_image = url_image
                            )

@app.route('/support/', methods=['GET', 'POST'])
def support():

    if request.method == "POST":
        data = request.form
        print(data)

    return render_template('module_three/index.html')


@app.route('/stripe_pay', methods=['POST'])
def stripe_pay():
    url = request.url    
    if request.method == "POST":
        url = request.base_url
        format = request.args
        data = request.form
        print(format)
        #session = stripe.checkout.Session.create(
        #payment_method_types=['card'],
        #line_items=[{
            #'price': 400,
        #    'quantity': 1,
       # }],
       # mode='payment',
       # success_url=url_for('succes', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        #cancel_url=url_for('home', _external=True),
    #)
    return '''<h2> Bonjour comment vas tu . </h2>''' #{
        #'checkout_session_id': session['id'], 
        #'checkout_public_key': app.config['STRIPE_PUBLIC_KEY']
    #}


@app.route('/transfert/succes')
def succes():
    return render_template('payements/succes.html')


@app.route('/transfert/cancel')
def echec():
    return render_template('payements/echec.html')

