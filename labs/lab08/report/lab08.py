P1="НаВашисходящийот1204".encode("cp1251")
P2="ВСеверныйфилиалБанка".encode("cp1251")

K=bytes.fromhex(
	"05 0C 17 7F 0E 4E 37 D2"
	"94 10 09 2E 22 57 FF C8"
	"0B B2 70 54"
)

def xor_bytes(a,b):
	return bytes(x^y for x,y in zip(a,b))
C1=xor_bytes(P1,K)
C2=xor_bytes(P2,K)
print("Шифротекст C1:")
print(C1.hex())

print()

P1_dec=xor_bytes(C1,K)
P2_dec=xor_bytes(C2,K)

print()

print("Расшифрованный P1:")
print(P1_dec.decode("cp1251"))
print()

print("Расшифрованный P2:")
print(P2_dec.decode("cp1251"))
print()
X=xor_bytes(C1,C2)
P2_hacked=xor_bytes(X,P1)
print("Восстановленный P2 без знания ключа:")
print(P2_hacked.decode("cp1251"))
print()
P1_hacked=xor_bytes(X,P2)
print("Восстановленный P1 без знания ключа:")
print(P1_hacked.decode("cp1251"))
