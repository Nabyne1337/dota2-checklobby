import pymem
import pymem.process
import time

pm = pymem.Pymem("dota2.exe")
client_module = pymem.process.module_from_name(pm.process_handle, "client.dll")
base_address = client_module.lpBaseOfDll

offset0 = 0x04E72CC8
offset1 = 0xEB0

while True:
    addr1 = base_address + offset0
    pointer1 = pm.read_ulonglong(addr1)
    
    if pointer1 != 0:
        addr2 = pointer1 + offset1
        value = pm.read_int(addr2)
        print(value)
    
    time.sleep(0.5)
