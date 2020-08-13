users = [
    {
        'id' : 1,
        'username': 'Ethan',
        'password': 1234
    }
]

username_mapping = { 'Ethan': {
        'id' : 1,
        'username': 'Ethan',
        'password': 1234
    }
}

userid_mapping = { 1: {
        'id' : 1,
        'username': 'Ethan',
        'password': 1234
    }
}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return userid_mapping

def identity(payload):
    user_id = payload['identity']
    return user