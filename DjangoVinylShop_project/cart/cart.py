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
        
      
        
    def add(self, product, product_qty):
        
        product_id = str(product.id)
        
        if product_id in self.cart:
            
            self.cart[product_id]['qty'] = product_qty
            
        else:
            
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
         
            
        self.session.modified = True