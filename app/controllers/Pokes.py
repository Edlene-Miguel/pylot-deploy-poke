from system.core.controller import *

class Pokes(Controller):
    def __init__(self, action):
        super(Pokes, self).__init__(action)

        self.load_model('Poke')

    def index(self):
        return self.load_view('index.html')

    def register(self):
        user = {
            'name' : request.form['name'],
            'alias' : request.form['alias'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'confirm_password' : request.form['confirm_password'],
        }
        self.models['Poke'].register(user)
        return redirect('/')

    def login(self):
        user = {
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        result = self.models['Poke'].login(user)
        if result['status'] == True:
            session['user_id'] = result['user_id']
            return redirect ('/pokes')
        return redirect('/show')

    def show(self):

        pokes = self.models['Poke'].show()
        user = self.models['Poke'].get_pokes_by_id(session['user_id'])
        return self.load_view(home.html, pokes = pokes, user = user)

    # def poke(self):
        


