def generate_repr(fields=None):
    def decorator(cls):
        def __repr__(self):
            repr_str = f'{cls.__name__}('
            attributes = []
            for attr, value in self.__dict__.items():
                if fields and attr in fields:
                    field_name = fields[attr]
                    if isinstance(value, list) and value and hasattr(value[0], field_name):
                        value = [getattr(item, field_name) for item in value]
                    elif hasattr(value, field_name):
                        value = getattr(value, field_name)

                attributes.append(f'{attr}={value!r}')
            repr_str += ", ".join(attributes)
            repr_str += ")"
            return repr_str

        cls.__repr__ = __repr__
        return cls

    return decorator