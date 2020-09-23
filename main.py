class currency (object):
    "Representa una moneda"
    def _init_(self,name,symbol):
        self.name = name
        self.symbol = symbol
    
    def _repr_(self):
        return self.name
        
    
    class Money(object):
        def _init(self,amount,currency):
            self.amount = amount
            self. currency = currency
            
        
        def _repr(self):
            return'{}{}'.format(self.currency.symbol, self.amount)
    
        dolar = currency('dolar','U$S')
        pesos = currency('pesos' '$')
        
        unPeso = Money(1,pesos)
        unDolar = Money(1,dolar)
        