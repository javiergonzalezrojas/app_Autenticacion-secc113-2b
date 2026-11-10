#genera los hash
import hashlib
#gemera el Salt
import secrets
#realiza la comparacion de contraseña
import hmac

class usuario:
    
    ITERACIONES = 600_000
    
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.__salt = secrets.token_bytes(16)
        self.__password_hash = self.generar_hash(password)
        
    def generar_hash(self, password):
        
        #la contraseña se convierte a bytes antes del calculo
        password_bytes = password.encode("utf-8")
        
        return hashlib.pbkdf2_hmac(
            "sha256",
            password_bytes,
            self.__salt,
            self.INTERACIONES
        )
        
    def verificar_password(self, password):
        
        return hmac.compare_digest(
            self.__password_hash;
            nuevo_hash
        )
    def cambiar_password(self, nueva_password):
        
        self.__salt = secrets.token_bytes(16)
        self.__password_hash = self.generar_hash(nueva_password)
        
    def mostrar_datos(self):
        print("\n --datos del usuario--")
        print("nombre: ", self.nombre)
        print("correo: ", self.correo)
        print("contraseña: *******")               