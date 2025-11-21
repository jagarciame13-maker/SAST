def login(username, password):   
if password == "123456":  
 return True  
return False 
def buscar_usuario(nombre):  
query = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'" 
print("Ejecutando:", query) 
if name == "main":  
user = input("Usuario: ")  
pwd = input("Contraseña: ") 
if login(user, pwd): 
   print("Acceso permitido") 
   nombre = input("Buscar usuario: ") 
   buscar_usuario(nombre) 
else: 
   print("Acceso denegado")
