import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("api/firebaseApi.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_all_list():
    docs = db.collection(u'profile').stream()

    user_list = 'Список: \n\n'
    counter = 1

    for doc in docs:
        doc_arr = doc.to_dict()
        user_list += f'{counter}: /{doc_arr.get("surname")} {doc_arr.get("name")} {doc_arr.get("patronymic")} \n\n'
        counter = counter + 1
    return user_list


def get_surname(name, surname):
    users_ref = db.collection(u'profile')
    user = users_ref.stream()
