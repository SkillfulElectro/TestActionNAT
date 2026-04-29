#!/usr/bin/env python3
"""Check NAT type using a public STUN server (Google). Requires pystun3."""
import stun

def main():
    nat_type, external_ip, external_port = stun.get_nat_type(
        stun_host='stun.l.google.com',
        stun_port=19302
    )
    print(f"NAT Type: {nat_type}")
    print(f"External IP: {external_ip}")
    print(f"External Port: {external_port}")

if __name__ == "__main__":
    main()
