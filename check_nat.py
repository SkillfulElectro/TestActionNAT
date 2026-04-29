#!/usr/bin/env python3
"""Check NAT type using a public STUN server (Google). Requires pystun3."""
import socket
import stun

def main():
    # Create a UDP socket for the STUN request
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)  # 3 seconds timeout

    try:
        # Bind to any available local address and port
        local_ip = "0.0.0.0"
        local_port = 0  # Let the OS pick a free port
        sock.bind((local_ip, local_port))

        # Call the library with the socket, local IP, and a preferred port (0 = automatic)
        nat_type, external_ip, external_port = stun.get_nat_type(
            sock,
            local_ip,
            local_port,
            stun_host="stun.l.google.com",
            stun_port=19302,
        )
        print(f"NAT Type: {nat_type}")
        print(f"External IP: {external_ip}")
        print(f"External Port: {external_port}")

    except Exception as e:
        print(f"❌ STUN request failed: {e}")
        raise SystemExit(1)
    finally:
        sock.close()

if __name__ == "__main__":
    main()
