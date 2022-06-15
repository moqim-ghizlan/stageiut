import re

def valid_name(prenom, nom):
    if len(nom) <= 3 or len(nom) >= 32 or len(prenom) <= 3 or len(prenom) > 32:
        return "Vous dovez entrer votre nom et prenom correctement"
    elif nom[0] == " " or nom[len(nom)-1] == " " or prenom[0] == " " or prenom[len(prenom)-1] == " ":
        return "Vous dovez entrer votre nom et prenom correctement"
    elif nom.isalpha() == False or prenom.isalpha() == False:
        return "Vous dovez entrer votre nom et prenom correctement"
    return True

def valid_user(user):
    cpt = 0
    if len(user) < 6:
         return "Pseudo doit être composé d'au moins 6 lettre, Ex : 'Jh0n.Smith' ."
    for i in user:
        if i.isalpha():
            cpt += 1
    if cpt == 0:
        #return "Username must have at least one letter : EX : Jhon.15 ."
        return "Pseudo doit contenir au moins une lettre : EX : Jhon.15 ."
    else:
        return True


def valid_email(email):
    if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
        return True
    else:
        return "L'email n'est pas valide"


def validitor_sign_up(nom, prenom, email, password1, password2):
    if valid_name(nom, prenom) != True :
        return valid_name(nom, prenom)
    elif valid_email(email) != True:
        return valid_email(email)
    elif password_check(password1, password2) != True:
        return password_check(password1, password2)
    else:
        return True
    
def password_check(passwd1, passwd2):
    #SpecialSym =['$', '@', '#', '%']
    if passwd1 != passwd2:
        return f"Les mots de passe ne correspondent pas"
    elif len(passwd1) < 8:
        return "La longueur doit être d'au moins 8 caractères"
    elif len(passwd1) > 36:
        return "La longueur ne doit pas dépasser 36 caractères"
    elif not any(char.isdigit() for char in passwd1):
        return 'Le mot de passe doit comporter au moins un chiffre'
    elif not any(char.isupper() for char in passwd1):
        return 'Le mot de passe doit avoir au moins une lettre majuscule'
    elif not any(char.islower() for char in passwd1):
        return 'Le mot de passe doit contenir au moins une lettre minuscule'
    return True
