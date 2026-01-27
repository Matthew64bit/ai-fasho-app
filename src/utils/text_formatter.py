def format_counter(counter: int = 0) -> str:
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


def format_time(time: int = 0) -> str:
    if time < 10:
        return "0" + str(time)
    elif time < 60:
        return str(time)
    else:
        raise ValueError("Invalid time value")

# filters has a 'range' field for specifying price range with values ['min', 'max', 'between']
# if min => price smaller or eq to price, if max => price bigger or eq to price, if between => price between filters['price'][0] and filters['price'][1]
# NEED TO MAKE SURE 'range' FIELD IS BEFORE 'price' FILED

def format_query(filters: dict) -> str:
    base_query = "SELECT * FROM clothes WHERE "
    opt = []
    p = False
    for key, value in filters.items():
        if key == 'range':
            if value == 'min':
                opt.append(f'price <= {filters['price']}')
            elif value == 'max':
                opt.append(f'price >= {filters['price']}')
            elif value == 'between':
                opt.append(f'price BETWEEN {filters['price'][0]} AND {filters['price'][1]}')
            p = True
        elif key == 'style' or key == 'colours':
            opt.append(f'{key} && ARRAY{value}')
        elif key == 'price' and p == True:
            continue
        else:
            opt.append(f"{key} = '{value}'")


    query = base_query +  " AND ".join(opt)
    return query
