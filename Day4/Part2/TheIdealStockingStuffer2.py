import hashlib

def mine_advent_coin(secret_key):
    num_zeroes = 6
    num_once = 0

    while True:
        data = f"{secret_key}{num_once}".encode("ascii")
        md5_hash = hashlib.md5(data).hexdigest()
        if md5_hash.startswith("0" * num_zeroes):
            return num_once
        num_once += 1


secret_key = "ckczppom"
print(
    "The lowest positive number to produce an MD5 hash with leading zeroes is:",
    mine_advent_coin(secret_key),
)
