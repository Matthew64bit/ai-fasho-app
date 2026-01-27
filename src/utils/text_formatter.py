
def format_counter(counter: int = 0):
    if counter < 10:
        return "000" + str(counter)
    elif counter < 100:
        return "00" + str(counter)
    elif counter < 1000:
        return "0" + str(counter)
    elif counter >= 1000:
        return str(counter)
    else:
        raise ValueError("Invalid counter value")


def format_time(time: int = 0):
    if time < 10:
        return "0" + str(time)
    elif time < 60:
        return str(time)
    else:
        raise ValueError("Invalid time value")


def format_query(filters: dict):
    base_query = "SELECT * FROM clothes WHERE "
    opt = []
    for key, value in filters.items():
        if key == 'style' or key == 'colour':
            opt.append(f'{key} && ARRAY{value}')
        else:
            opt.append(f"{key} = '{value}'")

    query = base_query +  " AND ".join(opt)
    return query
