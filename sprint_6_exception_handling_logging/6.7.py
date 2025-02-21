def valid_email(email):
    try:
        if email.count('@') != 1:
            raise ValueError

        user_info, domain_info = email.split('@')

        if not user_info or not domain_info:
            raise ValueError

        if '.' not in domain_info:
            raise ValueError

        domain_parts = domain_info.split('.')
        if not all(part.isalpha() for part in domain_parts):
            raise ValueError

        return "Email is valid"

    except (ValueError, AttributeError):
        return "Email is not valid"

print(valid_email("trafik@ukr.tel.com"))
