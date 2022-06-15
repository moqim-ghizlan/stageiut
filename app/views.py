from calendar import c
import json
from typing import final
from flask import Flask, render_template, flash, redirect, request, url_for, session, jsonify
from flask_login import UserMixin, login_user, current_user, logout_user, login_required
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import urllib.request
from .models import *
from .app import app ,db
from .static.python.info_validertor import *
from .static.python.firebase import firebase_upload_file, firebase_get_image_url, firebase_delete_image, firebase_edit_image
from .static.python.py_os import *
from os.path import join, dirname, realpath
import tempfile


###################################################
#                       auth
###################################################

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    # if current_user.is_authenticated(): return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Admin.query.filter_by(email=email).one_or_none()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Vienvenu !')
                return redirect(url_for('index'))
        return render_template("login.html", contactes = Contactes.query.first())
    return render_template("login.html", contactes = Contactes.query.first())



@app.route('/admin/logout')
@login_required
def logout():
    logout_user()
    flash('Au revoir !')
    return redirect(url_for('index'))


###################################################
#                       main
###################################################




@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template(
        "index.html",
        cars = Voiture.query.all(),
        contactes = Contactes.query.first()
        )


@app.route('/car/<int:id>/details', methods=['GET', 'POST'])
def plus_details(id):
    if Voiture.query.get(id) is None: return redirect(url_for('index'))
    return render_template(
        "plus_details.html",
        car = Voiture.query.filter_by(id = id).first(),
        contactes = Contactes.query.first())

@app.route('/admin/add/<string:gole>', methods=['GET', 'POST'])
@login_required
def add__(gole):
    return_data = dict()
    if gole == 'admin':
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            password2 = request.form.get('password_confirm')
            return_data['email'] = email
            if password != password2:
                return render_template("admin__.html", gole = gole, error = "Les mots de passe ne sont pas identiques", contactes = Contactes.query.first(), return_data = return_data)
            elif Admin.query.filter_by(email = email).one_or_none():
                return render_template("admin__.html", gole = gole, error = "L'administrateur est déjà enregistré(e) ", contactes = Contactes.query.first(), return_data = return_data)
            elif len(password) < 6:
                return render_template("admin__.html", gole = gole, error = "Le mot de passe doit contenir au moins 6 caractères", contactes = Contactes.query.first(), return_data = return_data)
            else:
                new_admin(email, generate_password_hash(password, method='sha256'))
                flash('Administrateur ajouté !')
                return redirect(url_for('index'), contactes = Contactes.query.first())
    elif gole == 'article':
        if request.method == 'POST':
            select_marques = request.form.get('select_marques')
            select_modeles = request.form.get('select_modeles')
            year = request.form.get('annee')
            kilometrage = request.form.get('Kilometrage')
            puissance = request.form.get('puissance')
            puissance_fiscale = request.form.get('puissance_fascals')
            select_nbportes = request.form.get('select_nbportes')
            select_nbplaces = request.form.get('select_nbplaces')
            select_carburants = request.form.get('select_carburants')
            select_boitesvitesse = request.form.get('select_boite-de-vitesse')
            description = request.form.get('description')
            prix = request.form.get('prix')
            # images = request.form.get('imagesToUpload')
            images = request.files.getlist('imagesToUpload')
            if not all([select_marques, select_modeles, year, kilometrage, puissance, puissance_fiscale, select_nbportes, select_nbplaces, select_carburants, select_boitesvitesse, description, prix, images]):
                flash(f"{select_marques} {select_modeles} {year} {kilometrage} {puissance} {puissance_fiscale} {select_nbportes} {select_nbplaces} {select_carburants} {select_boitesvitesse} {description} {prix} {images}")
                return render_template("admin__.html", gole = gole, contactes = Contactes.query.first(), return_data = return_data)
            car = Voiture(
                modele = select_modeles,
                annee = year,
                marque = select_marques,
                kilometrage = kilometrage,
                puissance = puissance,
                puissance_fiscale = puissance_fiscale,
                nb_portes = select_nbportes,
                couleur = "red",
                nb_places = select_nbplaces,
                carburant = select_carburants,
                boite_vitesse = select_boitesvitesse,
                description = description,
                prix = prix,
                images = [],
                marque_id = get_marque_id_by_name(select_marques)
                )
            db.session.add(car)
            db.session.commit()
            # os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], str(car.id)))
            files = request.files.getlist('imagesToUpload')
            for file in files:
                cpt = 1
                filename = secure_filename(file.filename)
                #file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(car.id), filename))
                # file.save(os.path.join(dirname(realpath(__file__)) + "/static/images/cars/"+str(car.id), filename))
                # file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(car.id), filename))
                print("file : ")
                print(file)
                print("file.filename : ")
                print(file.filename)
                temp = tempfile.NamedTemporaryFile(delete=False)
                file.save(temp.name)
                firebase_upload_file(car.id, temp.name, cpt)
                car.images.append(Voiture_images(url = firebase_get_image_url(car.id, cpt), voiture_id= car.id))
                os.remove(temp.name)
                cpt += 1
            db.session.commit()
            flash('Voiture ajoutée !')
            return redirect(url_for('index'))
    return render_template("admin__.html", contactes = Contactes.query.first(), gole = gole, return_data = return_data)



@app.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def car_edit(id):
    car = Voiture.query.filter_by(id = id).first()
    data = {'seleceted_modele': car.modele, 'seleceted_marque' : car.marque}
    if request.method == 'POST':
        select_marques = request.form.get('select_marques')
        select_modeles = request.form.get('select_modeles')
        year = request.form.get('annee')
        kilometrage = request.form.get('Kilometrage')
        puissance = request.form.get('puissance')
        puissance_fiscale = request.form.get('puissance_fiscale')
        select_nbportes = request.form.get('select_nbportes')
        select_nbplaces = request.form.get('select_nbplaces')
        select_carburants = request.form.get('select_carburants')
        select_boitesvitesse = request.form.get('select_boite-de-vitesse')
        description = request.form.get('description')
        prix = request.form.get('prix')  
        car = Voiture.query.filter_by(id = id).first()
        car.kilometrage = kilometrage
        car.nb_places = year
        car.nb_portes = select_nbportes
        car.nb_places = select_nbplaces
        car.carburant = select_carburants
        car.puissance = puissance
        car.puissance_fiscale = puissance_fiscale
        car.boite_vitesse = select_boitesvitesse
        car.description = description
        car.prix = prix
        car.modele = select_modeles
        car.marque = select_marques
        db.session.commit()
        files = request.files.getlist('imagesToUpload')
        for file in files:
            try:
                filename = secure_filename(file.filename)
                # file.save(os.path.join(dirname(realpath(__file__)) + "/static/images/cars/"+str(car.id), filename))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(car.id), filename))
                car.images.append(Voiture_images(url = filename, voiture_id= car.id))
            except:
                pass
        db.session.commit()
        flash('Votre voiture a bien été modifiée !')
        return redirect(url_for('index'))

    return render_template(
        "admin_edit.html",
        contactes = Contactes.query.first(),
        car = Voiture.query.filter_by(id = id).first(),
        data = data
        )







@app.route('/outpui_searchbar', methods = ['GET', 'POST'])
def outpui_searchbar():
    if request.method == 'POST':
        select_marques = request.form.get('select_marques')
        select_modeles = request.form.get('select_modeles')
        year_min = request.form.get('year-min')
        year_max = request.form.get('year-max')
        kilometrage_min = request.form.get('kilometrage-min')
        kilometrage_max = request.form.get('kilometrage-max')
        puissance_min = request.form.get('puissance-min')
        puissance_max = request.form.get('puissance-max')
        select_nbportes = request.form.get('select_nbportes')
        select_nbplaces = request.form.get('select_nbplaces')
        select_carburants = request.form.get('select_carburants')
        select_boitesvitesse = request.form.get('select_boitesvitesse')
        form__input = request.form.get('form__input')
        # query to get the search result
        with_marque = list()
        if select_marques != "all":
            with_marque = Voiture.query.filter_by(marque_id = Marque.query.filter_by(nom = select_marques).first().id).all()
        else: 
            with_marque = Voiture.query.all()

        cars = with_marque
        with_modele = list()
        if select_modeles.lower() != "all":
            with_modele = Voiture.query.filter_by(modele = str(select_modeles)).all()
        else:
            with_modele = Voiture.query.all()




        with_portes = list()
        if select_nbportes != "all":
            with_portes = Voiture.query.filter_by(nb_portes = int(select_nbportes)).all()
        else:
            with_portes = Voiture.query.all()
        
        with_places = list()
        if select_nbplaces != "all":
            with_places = Voiture.query.filter_by(nb_places = int(select_nbplaces)).all()
        else:
            with_places = Voiture.query.all()
        
        with_carburants = list()
        if select_carburants != "all":
            with_carburants = Voiture.query.filter_by(carburant = str(select_carburants)).all()
        else:
            with_carburants = Voiture.query.all()
        
        with_vitesse = list()
        if select_boitesvitesse != "all":
            with_vitesse = Voiture.query.filter_by(boite_vitesse = str(select_carburants)).all()
        else:
            with_vitesse = Voiture.query.all()
        
        with_years = Voiture.query.filter(Voiture.annee.between(int(year_min), int(year_max))).all()
        with_kilometrage = Voiture.query.filter(Voiture.kilometrage.between(int(kilometrage_min), int(kilometrage_max))).all()
        with_puissance = Voiture.query.filter(Voiture.puissance.between(int(puissance_min), int(puissance_max))).all()
        
        
        






        if len(with_modele) ==  0:
            cars = with_modele
        else:
            for car in cars:
                if car not in with_modele:
                    if car in cars:
                        cars.remove(car)
                    else: pass
                if car not in with_portes:
                    if car in cars:
                        cars.remove(car)
                    else: pass
                if car not in with_places:
                    if car in cars:
                        cars.remove(car)
                    else: pass
                if car not in with_carburants:
                    if car in cars:
                        cars.remove(car)
                    else: pass
                if car not in with_vitesse:
                    if car in cars:
                        cars.remove(car)
                    else: pass
                if car not in with_years:
                    if car in cars:
                        cars.remove(car)
                    else: pass
                if car not in with_kilometrage:
                    if car in cars:
                        cars.remove(car)
                    else: pass
                if car not in with_puissance:
                    if car in cars:
                        cars.remove(car)
                    else: pass

        

        
        

        


            

        





        return render_template(
            "index.html",
            contactes = Contactes.query.first(),
            cars = cars
            )
        
        
    return redirect(url_for('index'))



@app.route('/admin/contact/edit', methods = ['GET', 'POST'])
def edit_contact():
    if request.method == 'POST':
        new_email = request.form.get('email')
        new_number = request.form.get('number')
        con = Contactes.query.first()
        con.email = new_email
        con.number = new_number
        db.session.commit()
        flash('Les contactes ont été modifier avec succès')
    return redirect(url_for('index'))

@app.route('/cars/marque-name=<string:marque>', methods = ['GET', 'POST'])
def get_marques_list(marque):
    marque = Marque.query.filter_by(nom = marque).one_or_none()
    if marque == None:
        return redirect(url_for('index'))
    else:
        cars = Voiture.query.filter_by(marque_id = marque.id).all()
        return render_template(
            "index.html",
            cars = cars,
            contactes = Contactes.query.first()
            )

@app.route('/cars/marque-id=<int:id>', methods = ['GET', 'POST'])
def get_cars_list_by_marque_id(id):
    cars = Voiture.query.filter_by(marque_id =id).all()
    return render_template(
        "index.html",
        cars = cars,
        contactes = Contactes.query.first()
        )

@app.route('/marques/list', methods = ['GET', 'POST'])
def get_list_marques():
    marques = Marque.query.all()
    return render_template(
        "marques.html",
        marques = marques,
        contactes = Contactes.query.first()
        )


def make_first_leter_up(world):
    if type(world) is not str:
        return world
    return str(world[0].upper() + world[1:])

def set_format_tele(n):
    cpt = 0
    res = ""
    for i in n:
        if cpt == 2:
            res += " "
            cpt = 0
        res += i
        cpt += 1
    return res



@app.route('/get-marques')
def get_marques():
    return jsonify(set_marques_modeles())

# def get_marques_list():
#     liste = list()
#     for m in Marque.query.all():
#         liste.append(m.nom)
#     return liste

def get_nb_car_by_marque_id(id):
    return Voiture.query.filter_by(marque_id = id).count()

app.jinja_env.globals.update(
    get_marque_by_id = get_marque_nom_by_car_id,
    make_first_leter_up = make_first_leter_up,
    set_format_tele = set_format_tele,
    get_marques_list = get_marques_list,
    get_nb_car_by_marque_id = get_nb_car_by_marque_id
    )



@app.route("/admin/delete/car-id=<int:car_id>/img-id=<int:img_id>", methods = ['GET', 'POST'])
@login_required
def delete_car_image(car_id, img_id):
    car = Voiture.query.filter_by(id = car_id).one_or_none()
    for image in car.images:
        if image.id == img_id:
            db.session.delete(image)
            db.session.commit()
            try:
                # os.remove(dirname(realpath(__file__)) + "/static/images/cars/" +str(car_id) + "/" + image.url) #=> 100%                
                firebase_delete_image(car_id, image.id)
                flash('l\'image a été supprimée avec succès')
                return render_template(
                    "admin_edit.html",
                    contactes = Contactes.query.first(),
                    car = Voiture.query.filter_by(id = id).first())
            except:
                pass
    return redirect(url_for('car_edit', id=car_id))



@app.route("/admin/delete/car-id=<int:car_id>", methods = ['GET', 'POST'])
@login_required
def delete_car(car_id):
    car = Voiture.query.filter_by(id = car_id).one_or_none()
    if car == None: return redirect(url_for('car_delete', id=car_id))
    for image in car.images:
        db.session.delete(image)
        try:
            os.remove(os.remove(dirname(realpath(__file__)) + "/static/images/cars/" +str(car_id) + "/" + image.url)) #=> 100% 
        except:
            pass
    db.session.delete(car)
    db.session.commit()
    flash('La voiture a été supprimée avec succès')
    return redirect(url_for('index'))



# @app.errorhandler(404)
# def page_not_found(error):
#         return render_template('404.html',contactes = Contactes.query.first())

@app.errorhandler(404)
def page_not_found(error):
        return redirect(url_for('index'))
    
    
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



"""
if select_marques.lower() == "all":
            final_results.append(v for v in Voiture.query.all())
        else:
            final_results.append(v for v in (Voiture.query.filter_by(marque_id = Marque.query.filter_by(nom = select_marques).first().id).all()))
        
        if select_modeles.lower() == "all": pass
        else:
            for v in final_results:
                if v.modele != select_modeles:
                    final_results.pop(final_results.index(v))
                else: pass
                if v.annee < year_min or v.annee > year_max:
                    final_results.pop(final_results.index(v))
                else: pass
                if v.kilometrage < kilometrage_min or v.kilometrage > kilometrage_max:
                    final_results.pop(final_results.index(v))
                else: pass
                if v.puissance < puissance_min or v.puissance > puissance_max:
                    final_results.pop(final_results.index(v))
                else: pass
                if select_nbportes != "all":
                    if v.nb_portes != int(select_nbportes):
                        final_results.pop(final_results.index(v))
                    else: pass
                else: pass
                if select_nbplaces != "all":
                    if v.nb_places != int(select_nbplaces):
                        final_results.pop(final_results.index(v))
                    else: pass
                else: pass
                if select_carburants != "all":
                    if v.carburant.lower() != select_carburants.lower():
                        final_results.pop(final_results.index(v))
                    else: pass
                else: pass
                if select_boitesvitesse != "all":
                    if v.boite_vitesse.lower() != select_boitesvitesse.lower():
                        final_results.pop(final_results.index(v))
                    else: pass
                else: pass
                if form__input != "":
                    if v.description.lower().find(form__input.lower()) == -1:
                        final_results.pop(final_results.index(v))
                    else: pass
                else: pass
        return render_template("index.html", cars=final_results, contactes = Contactes.query.first())



"""