from system.core.model import Model

class Poke(Model):
    def __init__(self):
        super(Poke, self).__init__()

    def register(self, user):

        hashed_pw = self.bcrypt.generate_password_hash(user['password'])
        query = "INSERT INTO users(name, alias, email, password) VALUES (:name, :alias, :email, :pw_hash)"
        data = {
            'name' : user['name'],
            'alias' : user['alias'],
            'email' : user['email'],
            'pw_hash' : hashed_pw
        }
        return self.db.query_db(query, data)

    def login(self, user):

        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {
            "email" : user['email'],
            'password' : user['password']
        }
        result = self.db.query_db(query, data)

        if len(result) == 0:
            return {"status": False}

        if self.bcrypt.check_password_hash(result[0]['password'], user['password']):
            return {"status": True, "user_id": result[0]['id']}
        return {"status": False}

    def show(self):
        query = "SELECT * FROM users"
        return self.db.query_db(query)

    def get_poke_by_id(self, id):

        query = "SELECT * FROM pokes WHERE user_id = :user_id"
        data = {
            'user_id' : id
        }

    # def addpoke(self):
    #     query = "INSERT INTO pokes(poker, poked) VALUES (:session['user['alias']']', :user['alias'])"
    #     data = {
    #         'poker' : session['user['alias']'],
    #         'poked' : user['alias']
    #     }


