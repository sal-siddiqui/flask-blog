import hashlib


def get_gravatar(email, size=200):
    email = email.strip().lower()
    email_hash = hashlib.md5(email.encode("utf-8")).hexdigest()

    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=mp"
