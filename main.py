import re
def parse(query: str) -> dict:
    pattern = r'\?([^#]*)'
    match = re.search(pattern, query)
    print(match)

    if match:
        query_string = match.group(1)
        params = re.findall(r'([^&]+)=([^&]+)', query_string)
        print(params)
        return {param[0]: param[1] for param in params}

    else:
        return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima')


def parse_cookie(query: str) -> dict:
    # Используем регулярное выражение для разбора cookie-строки
    pattern = r'([^=;]+)=([^;]+);'
    print(pattern)
    cookies = re.findall(pattern, query)
    print(cookies)

    cookie_dict = {key.strip(): value.strip() for key, value in cookies}
    print(cookie_dict)

    return cookie_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}