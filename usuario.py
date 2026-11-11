# Genera los hash
import hashlib
#Genera el Salt
import secrets
#Realiza la comparacion de contraseñas
import hmac

class Usuario:
    
    ITERACIONES = 600_000
    
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.__salt = secrets.token_bytes(16)
        self.__password_hash = self.generar_hash(password)

    def generar_hash(self, password):
        
        # la contraseña se convierte a bytes antes del calculo
        password_bytes = password.encode("utf-8")
        
        return hashlib.pbkdf2_hmac(
            "sha256",
            password_bytes,
            self.__salt,
            self.ITERACIONES
        )
        
    def verificar_password(self, password):
        
        nuevo_hash = self.generar_hash(password)
        
        return hmac.compare_digest(
            self.__password_hash,
            nuevo_hash
        )
        
    def cambiar_password(self, nueva_password):
        
        self.__salt = secrets.token_bytes(16)
        self.__password_hash = self.generar_hash(nueva_password)
        
    def mostrar_datos(self):
        print("\n --Datos del Usuario--")
        print("Nombre: ", self.nombre)
        print("Correo: ", self.correo)
        print("Contraseña: ********")