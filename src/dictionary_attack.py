# # src/dictionary_attack.py
# import hashlib

# def calculate_pmk(password, ssid):
#     """Calcula el PMK (Pairwise Master Key) usando PBKDF2-HMAC-SHA1."""
#     password_bytes = password.encode('utf-8')
#     ssid_bytes = ssid.encode('utf-8')
#     pmk = hashlib.pbkdf2_hmac('sha1', password_bytes, ssid_bytes, 4096, 32)
#     return pmk

# def run_dictionary_attack(wordlist_path, ssid, handshake_mic):
#     """Ejecuta un ataque de diccionario contra un handshake WPA/WPA2."""
#     try:
#         with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
#             for password in f:
#                 password = password.strip()  # Eliminar espacios en blanco al principio y al final
#                 pmk = calculate_pmk(password, ssid)
#                 # Aquí iría la lógica para calcular el PTK y comparar el MIC
#                 print(f"Probando contraseña: {password}, PMK: {pmk.hex()[:16]}...") # Imprimir solo los primeros 16 caracteres del PMK
#     except FileNotFoundError:
#         print(f"Error: La wordlist '{wordlist_path}' no se encuentra.")
#     except Exception as e:
#         print(f"Ocurrió un error inesperado: {e}")

# if __name__ == "__main__":
#     wordlist_path = "wordlist/rockyou2.txt"  # Reemplaza con la ruta a tu wordlist
#     ssid = "iPhone de Jesus"  # Reemplaza con el ESSID de la red
#     handshake_mic = "mic_del_handshake"  # Simulamos el MIC del handshake
#     run_dictionary_attack(wordlist_path, ssid, handshake_mic)

# src/dictionary_attack.py
import hashlib

def calculate_pmk(password, ssid):
    """Calcula el PMK (Pairwise Master Key) usando PBKDF2-HMAC-SHA1."""
    password_bytes = password.encode('utf-8')
    ssid_bytes = ssid.encode('utf-8')
    pmk = hashlib.pbkdf2_hmac('sha1', password_bytes, ssid_bytes, 4096, 32)
    return pmk

def run_dictionary_attack(wordlist_path, ssid, handshake_mic):
    """Ejecuta un ataque de diccionario contra un handshake WPA/WPA2."""
    try:
        max_passwords = 10000  # Limitar el número de contraseñas a probar
        passwords_tested = 0
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for password in f:
                password = password.strip()  # Eliminar espacios en blanco al principio y al final
                pmk = calculate_pmk(password, ssid)
                passwords_tested += 1
                if passwords_tested % 1000 == 0:  # Imprimir mensaje cada 1000 contraseñas
                    print(f"Probadas {passwords_tested} contraseñas...")
                # Aquí iría la lógica para calcular el PTK y comparar el MIC
                print(f"Probando contraseña: {password}, PMK: {pmk.hex()[:16]}...") # Imprimir solo los primeros 16 caracteres del PMK
                if passwords_tested >= max_passwords:
                    print(f"Se alcanzó el límite de {max_passwords} contraseñas. Saliendo.")
                    break  # Salir del bucle si alcanzamos el límite
    except FileNotFoundError:
        print(f"Error: La wordlist '{wordlist_path}' no se encuentra.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    wordlist_path = "wordlist/rockyou.txt"  # Reemplaza con la ruta a tu wordlist
    ssid = "NombreDeMiRed"  # Reemplaza con el ESSID de la red
    handshake_mic = "mic_del_handshake"  # Simulamos el MIC del handshake
    run_dictionary_attack(wordlist_path, ssid, handshake_mic)