import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .app import db
import click
import yaml
import os.path
from flask import jsonify
from os.path import join, dirname, realpath
from .static.python.data_marque_modele import get_data
from .static.python.firebase import firebase_upload_file




class Admin(UserMixin, db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))
    password = db.Column(db.String(256))
    role = db.Column(db.String(256))
    def __repr__(self):
        return f"Admin ({self.id}, {self.email}, {self.role})"


class Voiture(db.Model):
    __tablename__ = 'voitures'
    id = db.Column(db.Integer, primary_key=True)
    marque = db.Column(db.String(256))
    modele = db.Column(db.String(256))
    annee = db.Column(db.Integer)
    prix = db.Column(db.Integer)
    kilometrage = db.Column(db.Integer)
    nb_places = db.Column(db.Integer)
    nb_portes = db.Column(db.Integer)
    couleur = db.Column(db.String(256))
    carburant = db.Column(db.String(256))
    puissance = db.Column(db.Integer)
    puissance_fiscale = db.Column(db.Integer)
    boite_vitesse = db.Column(db.String(256))
    description = db.Column(db.String(256))
    images = db.relationship('Voiture_images', backref='images', lazy=True, uselist=True)
    marque_id = db.Column(db.Integer,db.ForeignKey("marque.id"), nullable=False)

    def __repr__(self):
        # return (f"Voiture (id :{self.id}, modele : {self.modele}, annee :{self.annee}, prix : {self.prix}, kilometrage : {self.kilometrage}, nb_blace : {self.nb_places}, nb_portes : {self.nb_portes}, couleur : {self.couleur}, carburant : {self.carburant}, puissance : {self.puissance}, puissance_fiscale : {self.puissance_fiscale}, boite_vitesse : {self.boite_vitesse}, description: {self.description}, marque_id : {self.marque_id}, images :\n {self.images})")
        # return (f"Voiture (id :{self.id}, modele : {self.modele}, annee :{self.annee}, prix : {self.prix}, kilometrage : {self.kilometrage}, nb_blace : {self.nb_places}, nb_portes : {self.nb_portes}, couleur : {self.couleur}, carburant : {self.carburant}, puissance : {self.puissance}, puissance_fiscale : {self.puissance_fiscale}, boite_vitesse : {self.boite_vitesse}, description: {self.description}, marque_id : {self.marque_id}")
        return (f"Voiture (id :{self.id}, modele : {self.modele}, marque_id : {self.marque_id}")



class Marque(db.Model):
    __tablename__ = 'marque'
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(50))
    voitures = db.relationship('Voiture', backref='author', lazy=True)
    modeles = db.relationship('Modele', backref='modeles', lazy=True, uselist=True)
    
    def __repr__(self):
        return (f"Marque ({self.id}, {self.nom}, {self.modeles})")





class Modele(db.Model):
    __tablename__ = 'modele'
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(50))
    marque_id = db.Column(db.Integer,db.ForeignKey("marque.id"))

    def __repr__(self):
        return (f"Modele ({self.id}, {self.nom}, {self.marque_id})")
    
    


class Voiture_images(db.Model):
    __tablename__ = 'voiture_images'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(256), nullable=False)
    voiture_id = db.Column(db.Integer, db.ForeignKey("voitures.id"))

    def __repr__(self):
        return (f"Voiture_images ({self.id}, {self.url}, {self.voiture_id})")




class Contactes(db.Model):
    __tablename__ = 'Contactes'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(256), nullable=False)
    telephone = db.Column(db.String(256), nullable=False)
    adresse = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return (f"Contactes ({self.email}, {self.telephone}, {self.adresse})")





def loaddb():
    db.drop_all()
    db.create_all()
    #__init__marques_modele()
    __init_app__()
    
    


# def fount_errer():

images = [
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F1.png?alt=media&token=f4851063-e1ed-46b2-8745-9d1beb6264ec",
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F2.png?alt=media&token=39c963b7-df5b-424c-b18d-5480819402e2",
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F3.png?alt=media&token=6323dbf0-c45e-409e-b95c-199bf5088547",
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F4.png?alt=media&token=f0658b80-aee2-4b41-b8e1-bdbe05aeb918",
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F5.png?alt=media&token=d5714912-1a71-40d9-b0e6-b78683820acb",
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F6.png?alt=media&token=4a7d20cd-5cbf-4e2a-9ea7-7a9a33a4ec73",
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F6.png?alt=media&token=4a7d20cd-5cbf-4e2a-9ea7-7a9a33a4ec73",
    "https://firebasestorage.googleapis.com/v0/b/stageiut-e1349.appspot.com/o/images%2Fcars%2F1%2F6.png?alt=media&token=4a7d20cd-5cbf-4e2a-9ea7-7a9a33a4ec73"
]
    


def __init_app__():
    db.drop_all()
    db.create_all()
    __init__marques_modele()
    __init__contactes_info()
    new_admin("moqim@gmail.com", generate_password_hash('moqim', method='sha256'))
    new_car("80", "Audi", "2015", "11000", "11000", "2", "3", "rouge", "essence", "100", "100", "manuelle", "This is the test number 1", images, 1)
    new_car("200", "Audi", "2016", "12000", "12000", "4", "5", "rouge", "gpl", "200", "200", "manuelle", "This is the test number 2", images, 1)
    new_car("80","Audi", "2016", "12000", "12000", "7", "3", "rouge", "disel", "200", "200", "manuelle", "This is the test number 2", images, 1)
    new_car("316", "BMW", "2017", "13000", "13000", "5", "5", "red", "hybride", "300", "300", "automatique", "This is the test number 3", images, 2)
    # for i in range(20):
    #     new_car("Clio4", "Audi", "2018", "14000", "14000", "6", "2", "bleu", "disel", "400", "400", "automatique", "This is the test number x", images, 1)

def new_marque(nom):
    if Marque.query.filter_by(nom = nom).one_or_none() is None:
        m = Marque(nom = nom)
        db.session.add(m)
        db.session.commit()
    else: return None



def new_modele(marque_nom, modele_nom):
    if Marque.query.filter_by(nom = marque_nom).one_or_none() is None:
        m = Marque(nom = marque_nom)
        m.modeles.append(Modele(nom = modele_nom))
        db.session.add(m)
        db.session.commit()
    else:
        m = Marque.query.filter_by(nom = marque_nom).first()
        m.modeles.append(Modele(nom = modele_nom))
        db.session.commit()




def get_marque_id_by_name(name):
    m = Marque.query.filter_by(nom=name).one_or_none()
    if m: return m.id
    else: return None

def new_car(modele, marque, annee, prix, kilometrage, nb_places, nb_portes, couleur, carburant, puissance, puissance_fiscale, boite_vitesse, description, images, marque_id):
    car = Voiture(
        modele = modele,
        marque = marque,
        annee = annee,
        prix = prix,
        kilometrage = kilometrage,
        nb_places = nb_places,
        nb_portes = nb_portes,
        couleur = couleur,
        carburant = carburant,
        puissance = puissance,
        puissance_fiscale = puissance_fiscale,
        boite_vitesse = boite_vitesse,
        description = description,
        marque_id = marque_id)
    for i in images:
        car.images.append(Voiture_images(url = i))
    db.session.add(car)
    db.session.add(car)
    db.session.commit()


def get_all_cars():
    return Voiture.query.all()

def get_marque_by_id(id):
    marque = Marque.query.filter_by(id = id).first()
    if marque is None:
        return "Marque inconnue"
    return Marque.query.filter_by(id = id).first().nom


def get_marque_id_by_name(nom):
    m = Marque.query.filter_by(nom = nom).one_or_none()
    if m: return m.id
    else:
        m = Marque(nom = nom)
        db.session.add(m)
        db.session.commit()
        return m.id


def get_marque_nom_by_car_id(id):
    marque_id = Voiture.query.filter_by(id = id).one_or_none()
    if marque_id is None:
        return None
    return Marque.query.filter_by(id = marque_id.marque_id).first().nom


def get_car_images_by_id(id):
    return Voiture.query.filter_by(id = id).first().images

def get_car_by_id(id):
    return Voiture.query.filter_by(id = id).first()

def new_admin(email, password):
    ad = Admin(email = email, password = password, role = "admin")
    db.session.add(ad)
    db.session.commit()

def delete_car(id):
    car = Voiture.query.filter_by(id = id).one_or_none()
    car_images = car.images
    for image in car_images:
        db.session.delete(image)
        db.session.commit()
        try:
            #os.remove("app/static/images/cars/" +str(car_id) + "/" + image.url) => 50%
            os.remove(dirname(realpath(__file__)) + "/static/images/cars/" +str(id) + "/" + image.url) #=> 100% 
        except:
            pass
    os.rmdir(dirname(realpath(__file__)) + "/static/images/cars/" +str(id))
    db.session.delete(car)
    db.session.commit()



def __init__contactes_info():
    con = Contactes(email = "myautolivefrance@gmail.com", telephone = "0753895133", adresse = "2 allée Pierre de Coubertin 45000 Orléans")
    db.session.add(con)
    db.session.commit()

def __init__marques_modele():
    data = get_data()
    for marque, modeles in data.items():
        m = Marque(nom = marque)
        for modele in modeles:
            m.modeles.append(Modele(nom = modele, marque_id = m.id))
        db.session.add(m)
    db.session.commit()


def set_marques_modeles():
    final_data = list()
    marques = Marque.query.all()
    for marque in marques:
        data = {
            'marque': marque.nom,
            'modeles': [modele.nom for modele in marque.modeles]
        }
        final_data.append(data)
    return final_data
    

def get_searched_cars(select_marques, select_modeles, year_min, year_max, kilometrage_min, kilometrage_max, puissance_min, puissance_max, select_nbportes, select_nbplaces, select_carburants, select_boitesvitesse, form__input):
    cars = Voiture.query.all()
    final_cars = list()
    for car in cars:
        if (car.marque_id in select_marques and
            car.modele_id in select_modeles and
            car.annee >= year_min and
            car.annee <= year_max and
            car.kilometrage >= kilometrage_min and
            car.kilometrage <= kilometrage_max and
            car.puissance >= puissance_min and
            car.puissance <= puissance_max and 
            car.nb_portes == select_nbportes and 
            car.nb_places == select_nbplaces and 
            car.carburant in select_carburants and 
            car.boite_vitesse in select_boitesvitesse):
            final_cars.append(car)
    return final_cars



def delete_car_with_images(car_id):
    car = Voiture.query.filter_by(id = car_id).first()
    for image in car.images:
        try:
            db.session.delete(image)
            os.remove(dirname(realpath(__file__)) + "/static/images/cars/" +str(id) + "/" + image.url) #=> 100% 
        except:
            pass
    db.session.delete(car)
    db.session.commit()