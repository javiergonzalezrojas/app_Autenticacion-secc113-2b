from usuario import Usuario


class Autenticacion:
    """
    Administra el registro, el inicio de sesión y el cambio
    de contraseña de los usuarios.
    """

    MAX_INTENTOS = 3

    def __init__(self):
        # En este ejercicio los usuarios se mantienen en memoria.
        self.usuarios = []

        # Guarda los intentos fallidos por correo.
        self.intentos_fallidos = {}

    def registrar_usuario(self, nombre, correo, password):
        """Registra un usuario si cumple las validaciones básicas."""

        # Validación sencilla de longitud.
        if len(password) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            return False

        # Evita registrar dos veces el mismo correo.
        for usuario in self.usuarios:
            if usuario.correo.lower() == correo.lower():
                print("El correo ya se encuentra registrado.")
                return False

        # El objeto Usuario se encarga de generar su Salt y hash.
        nuevo_usuario = Usuario(nombre, correo, password)
        self.usuarios.append(nuevo_usuario)

        print("Usuario registrado correctamente.")
        return True

    def iniciar_sesion(self, correo, password):
        """Devuelve el objeto Usuario si las credenciales son válidas."""

        for usuario in self.usuarios:
            if usuario.correo.lower() == correo.lower():

                intentos = self.intentos_fallidos.get(correo.lower(), 0)

                # Bloqueo didáctico en memoria tras tres fallos.
                if intentos >= self.MAX_INTENTOS:
                    print("Cuenta bloqueada por intentos fallidos.")
                    return None

                if usuario.verificar_password(password):
                    self.intentos_fallidos[correo.lower()] = 0
                    print("Inicio de sesión exitoso.")
                    print("Bienvenido:", usuario.nombre)
                    return usuario

                # Contraseña incorrecta: aumenta el contador.
                intentos += 1
                self.intentos_fallidos[correo.lower()] = intentos

                print("Contraseña incorrecta.")
                print("Intentos restantes:", self.MAX_INTENTOS - intentos)

                if intentos >= self.MAX_INTENTOS:
                    print("Se alcanzó el máximo de intentos. Cuenta bloqueada.")

                return None

        print("Usuario no encontrado.")
        return None

    def cambiar_password(self, usuario, password_actual, nueva_password):
        """Permite cambiar la contraseña del usuario autenticado."""

        if usuario is None:
            print("Debe iniciar sesión primero.")
            return False

        if not usuario.verificar_password(password_actual):
            print("La contraseña actual es incorrecta.")
            return False

        if len(nueva_password) < 8:
            print("La nueva contraseña debe tener al menos 8 caracteres.")
            return False

        # Usuario genera un Salt nuevo y recalcula el hash.
        usuario.cambiar_password(nueva_password)

        # Reinicia los intentos fallidos del usuario.
        self.intentos_fallidos[usuario.correo.lower()] = 0

        print("Contraseña actualizada correctamente.")
        return True