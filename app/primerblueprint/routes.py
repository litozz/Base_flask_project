from flask import Flask, render_template, url_for
from . import primerblueprint
 
@primerblueprint.route('/primerblueprint')
def index():
	#return render_template('index2.html')
 	return 'Hola desde el index del blueprint 1'

@primerblueprint.route('/primerblueprint/saludo')
def saludo():
	#return render_template('saludo.html')
	return 'Hola desde la funcion saludo del blueprint 1'
 
@primerblueprint.route('/primerblueprint/user/<username>')
def user(username):
	#return render_template('user.html', username=username)
	return 'Hola desde la función user del blueprint 1, {}'.format(username)