import subprocess
import plistlib

def scan_networks():
    try:
        result = subprocess.run(
            ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s", "-x"],
            capture_output=True,
            text=True
        )

        networks = plistlib.loads(result.stdout.encode())

        print("Redes Wi-Fi encontradas:\n")
        for net in networks:
            ssid = net.get("SSID_STR", "N/A")
            bssid = net.get("BSSID", "N/A")
            rssi = net.get("RSSI", "N/A")
            channel = net.get("CHANNEL", "N/A")

            # Obtener información de seguridad
            security = "N/A"
            if "RSN_IE" in net:
                rsn_ie = net["RSN_IE"]
                auth_sels = rsn_ie.get("IE_KEY_RSN_AUTHSELS", "N/A")
                security = f"WPA/WPA2 (Auth: {auth_sels})"
            elif "CAPABILITIES" in net:
                capabilities = int(net["CAPABILITIES"])
                if (capabilities & 0x10): # Verificar bit de WEP
                    security = "WEP"
                elif (capabilities & 0x2000): # Verificar bit de WPA
                    security = "WPA"
                elif (capabilities & 0x2010): # Verificar bits de WPA2
                    security = "WPA2"

            print(f"SSID: {ssid}")
            print(f"BSSID: {bssid}")
            print(f"RSSI: {rssi}")
            print(f"CHANNEL: {channel}")
            print(f"SECURITY: {security}")
            print("-" * 30)

    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    scan_networks()

# ////////////////////////////////////////////////////////////////////////////////////////

# import subprocess
# import xml.etree.ElementTree as ET

# def scan_networks_xml():
#     """Escanea redes WiFi en macOS utilizando 'airport -s -x' y parsea la salida XML."""
#     cmd = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s", "-x"]
    
#     try:
#         result = subprocess.run(cmd, capture_output=True, text=True, check=True)
#         xml_data = result.stdout

#         # Parsear el XML
#         root = ET.fromstring(xml_data)
#         networks = root.find("array")

#         if networks is None:
#             print("No se encontraron redes.")
#             return

#         for dict_node in networks.findall("dict"):
#             # Crear un diccionario con claves y valores alternos
#             keys = dict_node.findall("key")
#             values = dict_node.findall("*")[1::2]  # Tomar cada segundo nodo después de los <key>

#             info = {k.text: v.text for k, v in zip(keys, values)}

#             ssid = info.get("SSID_STR", "N/A")
#             bssid = info.get("BSSID", "N/A")
#             rssi = info.get("RSSI", "N/A")
#             channel = info.get("CHANNEL", "N/A")

#             # Obtener información de seguridad
#             security = "N/A"
#             if "RSN_IE" in info:
#                 rsn_ie = {}
#                 # Crear un diccionario para RSN_IE
#                 rsn_ie_node = dict_node.find("dict[key='RSN_IE']")
#                 if rsn_ie_node is not None:
#                   rsn_keys = rsn_ie_node.findall("dict/key")
#                   rsn_values = rsn_ie_node.findall("dict/*")[1::2]
#                   rsn_ie = {k.text: v.text for k, v in zip(rsn_keys, rsn_values)}
                
#                 auth_sels = rsn_ie.get("IE_KEY_RSN_AUTHSELS", "N/A")
#                 security = f"WPA/WPA2 (Auth: {auth_sels})"
#             elif "CAPABILITIES" in info:  # Si no hay RSN_IE, verificar capabilities
#                 capabilities = int(info["CAPABILITIES"])
#                 if (capabilities & 0x10): # Verificar bit de WEP
#                     security = "WEP"
#                 elif (capabilities & 0x2000): # Verificar bit de WPA
#                     security = "WPA"
#                 elif (capabilities & 0x2010): # Verificar bits de WPA2
#                     security = "WPA2"    

#             print(f"SSID: {ssid}")
#             print(f"BSSID: {bssid}")
#             print(f"RSSI: {rssi}")
#             print(f"CHANNEL: {channel}")
#             print(f"SECURITY: {security}")
#             print("-" * 30)

#     except subprocess.CalledProcessError as e:
#         print(f"Error al ejecutar el comando airport: {e}")
#     except ET.ParseError as e:
#         print(f"Error al parsear XML: {e}")
#     except Exception as e:
#         print(f"Ocurrió un error inesperado: {e}")


# if __name__ == "__main__":
#     scan_networks_xml()


# ////////////////////////////////////////////////////////////////////////////////////////


# import subprocess
# import xml.etree.ElementTree as ET

# def scan_networks_xml():
#     """Escanea redes WiFi en macOS utilizando 'airport -s -x' y parsea la salida XML."""
#     cmd = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s", "-x"]
    
#     try:
#         result = subprocess.run(cmd, capture_output=True, text=True, check=True)
#         xml_data = result.stdout

#         # Parsear el XML
#         root = ET.fromstring(xml_data)
#         networks = root.find("array")

#         if networks is None:
#             print("No se encontraron redes.")
#             return

#         for dict_node in networks.findall("dict"):
#             # Crear un diccionario con claves y valores alternos
#             keys = dict_node.findall("key")
#             values = dict_node.findall("*")[1::2]  # Tomar cada segundo nodo después de los <key>

#             info = {k.text: v.text for k, v in zip(keys, values)}

#             ssid = info.get("SSID_STR", "N/A")
#             bssid = info.get("BSSID", "N/A")
#             rssi = info.get("RSSI", "N/A")
#             channel = info.get("CHANNEL", "N/A")
#             security = info.get("SECURITY", "N/A")

#             print(f"SSID: {ssid}")
#             print(f"BSSID: {bssid}")
#             print(f"RSSI: {rssi}")
#             print(f"CHANNEL: {channel}")
#             print(f"SECURITY: {security}")
#             print("-" * 30)

#     except subprocess.CalledProcessError as e:
#         print(f"Error al ejecutar el comando airport: {e}")
#     except ET.ParseError as e:
#         print(f"Error al parsear XML: {e}")
#     except Exception as e:
#         print(f"Ocurrió un error inesperado: {e}")


# if __name__ == "__main__":
#     scan_networks_xml()
