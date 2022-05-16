def translate(message):
    #string characters to unicode values
    charcodes = [ord(c) for c in message]
    #unicode values to 8-bit strings (removed binary indicator)
    bytes = []
    for char in charcodes:
        bytes.append(bin(char)[2:].zfill(8))
    #8-bit strings to list of bits as integers
    bits = []
    for byte in bytes:
        for bit in byte:
            bits.append(int(bit))
    return bits

print(translate("Hola a todos"))