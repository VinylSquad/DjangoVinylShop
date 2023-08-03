class Cart():
    
    def __init__(self, request):
        
        self.session = request.session
        # Zwracanie użytkownikowi istniejącej sesji 
        
        cart = self.session.get('session_key')
        
        
        # Nowy użytkownik generuje nową sesję
        if 'session_key' not in request.session:
            
            cart = self.session['session_key'] = {}
            
        self.cart = cart
        # nalezy dodac do settings/templates/context_processor