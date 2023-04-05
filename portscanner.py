import socket, sys
import asyncio

banner = """Author : Gameye98
Date   : Thu Apr  6 00:26:45 2023
Purpose: Scanning port with async
Team   :
  - BlackHole Security
	    (https://github.com/BlackHoleSecurity)
  - Schadenfreude
	    (https://t.me/schdenfreude)
"""

async def connect(ip: str, port) -> bool:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((ip,port))
	if status == 0:
		print(f"Port {port} is open!")
		return True
	return False

async def main():
	funcs: list[bool] = [connect(sys.argv[1],port) for port in range(1,65536)]
	await asyncio.gather(*funcs)
	print("Done!")

if __name__ == "__main__":
	print(banner)
	if len(sys.argv) != 2:
		print("Usage: portscanner <ip-address>")
	else:
		asyncio.run(main())