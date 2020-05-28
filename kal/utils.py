def dig(obj, *keys, default=None):
    current_value = None
    index = 0
    try:
        for key in keys:
            if type(key) is str and key.isdigit():
                key = int(key)
            if index == 0:
                current_value = obj[key]
            else:
                current_value = current_value[key]
            index += 1
        return current_value
    except KeyError:
        return default
    except IndexError:
        return default
