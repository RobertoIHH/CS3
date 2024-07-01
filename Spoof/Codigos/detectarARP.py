from scapy.all import *  # Importa todas las funciones de la biblioteca Scapy
import time  # Importa la biblioteca de tiempo
import os  # Importa la biblioteca de os para ejecutar comandos del sistema

def get_mac(ip):
    # Usa el comando arp para obtener la MAC address
    try:
        output = os.popen(f"arp -n {ip}").read()
        lines = output.split('\n')
        for line in lines:
            if ip in line:
                return line.split()[2]
    except Exception as e:
        print(f"Error obteniendo la MAC para {ip}: {e}")
    return None

def get_gateway_ip():
    # Ejecuta el comando para obtener la IP del gateway
    gateway_ip = os.popen("ip route | grep default").read().strip().split()[2]
    return gateway_ip

def detect_arp_spoof(gateway_ip):
    original_mac = get_mac(gateway_ip)  # Obtiene la dirección MAC original del gateway
    if original_mac is None:
        print(f"No se puede obtener la MAC del gateway {gateway_ip}")  # Imprime un mensaje si no se puede obtener la MAC
        return

    print(f"MAC original del gateway {gateway_ip}: {original_mac}")  # Imprime la MAC original del gateway

    while True:
        current_mac = get_mac(gateway_ip)  # Obtiene la dirección MAC actual del gateway
        if current_mac != original_mac:
            print(f"¡ARP Spoofing detectado! La MAC original {original_mac} ha sido cambiada a {current_mac}")  # Imprime un mensaje de alerta si la MAC ha cambiado
        else:
            print(f"No se detectaron cambios en la MAC del gateway {gateway_ip}. La MAC sigue siendo {current_mac}")  # Confirma que no hay cambios en la MAC
        time.sleep(2)  # Espera 2 segundos antes de la siguiente verificación

if __name__ == "__main__":
    gateway_ip = get_gateway_ip()  # Obtiene la IP del gateway automáticamente
    print(f"IP del gateway detectada: {gateway_ip}")  # Imprime la IP del gateway detectada
    
    detect_arp_spoof(gateway_ip)  # Llama a la función detect_arp_spoof con la IP del gateway detectada
