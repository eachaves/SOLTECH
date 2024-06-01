import hashlib


def create_hash(id_compra: str, monto: int, divisa: str) -> Hash:
    try:
        hash = hashlib.sha256()
        concat= id_compra + str(monto) + divisa
        hash.update(concat.encode())
        return hash.hexdigest()
    except Exception as e:
        raise Exception(e.args[0], 500)