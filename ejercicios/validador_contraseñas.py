#!/usr/bin/env python
# coding: utf-8

# In[35]:


def strong_password(password):
    if len(password) < 8:
        print('La contraseña debe tener 8 caracteres mínimo')
        return False
    tiene_mayuscula = False
    for i in password:
        if i.isupper():
             tiene_mayuscula = True
             break
    if not tiene_mayuscula:
            print('La contraseña debe contener una mayúscula, al menos')
            return False
    tiene_minuscula = False
    for i in password:
        if i.islower():
            tiene_minuscula = True
            break
    if not tiene_minuscula:
            print('La contraseña debe contener una minúscula, al menos')
            return False
    tiene_numero = False
    for i in password:
        if i.isdigit():
            tiene_numero = True
            break
    if not tiene_numero:
            print('La contraseña debe contener un número, al menos')
            return False
    simbolos = "!@#$%^&*()_+-=[]{};:'\",.<>?/\\|"
    tiene_simbolos = False
    for i in password:
        if i in simbolos:
            tiene_simbolos = True
            break
    if not tiene_simbolos:
        print('La contraseña debe contener un carácter especial, al menos')
        return False
    return True

if __name__ == '__main__':
    password = input('Introduce una contraseña que incluya 8 caracteres mínimo, incluyendo, al menos, una mayúscula, una minúscula, un número y un carácter especial')
    if strong_password(password):
        print('La contraseña es segura')
    else:
        print('La contraseña NO es segura')
                                 

        
    
        
            
        
    


# In[31]:


print(strong_password("Abcdef1!"))    # Válida → True
print(strong_password("abcdef1!"))    # Sin mayúscula → False
print(strong_password("ABCDEF1!"))    # Sin minúscula → False
print(strong_password("Abcdefgh"))    # Sin número, sin símbolo → False
print(strong_password("A1!"))         # Demasiado corta → False
print(strong_password("Abcdef12"))    # Sin símbolo → False
print(strong_password("12345678!"))   # Sin letra →


# In[ ]:




