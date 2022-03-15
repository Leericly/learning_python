targetIP = input("Enter your IP (Default: 192.168.1.1): ")

#Internal bypass
if targetIP == "":
    targetIP = "192.168.1.1"
    
splitIP = targetIP.split(".")

def convert_to_octet(a):
    octetList = [int(a[0]), int(a[1]), int(a[2]), int(a[3])]
    newOctetList = []

    for eachOctet in octetList[:]:
        binaryForm = format(eachOctet, 'b')
        newOctetList.append(binaryForm)
        
    print(newOctetList) 

convert_to_octet(splitIP)
