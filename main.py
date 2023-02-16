def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=+380502924354;age=2+2') == {'name': '380502924354', 'age': '2 2'}
    assert parse_cookie('name=&;color=&;exempe==name=') == {'name': '', 'color': '', 'exemple': '=name='}
    assert parse_cookie('name=&;color=&;exempe=?name?') == {'name': '', 'color': '', 'exemple': '?name?'}
    assert parse_cookie('name=?/;color=/&;exempe=?name=/') == {'name': '?/', 'color': '/', 'exemple': '?name=/'}
    assert parse_cookie('name=?/;color=/p;exempe=?name=/&;main=1000') == {'name': '?/', 'color': '/p', 'exemple': '?name=/', 'main': '1000'}
    assert parse_cookie('name=https://example.com/') == {'name': 'https://example.com/'}
    assert parse_cookie('name=діма;color=червоний') == {'name': 'діма', 'color': 'червоний'}
    assert parse_cookie('name=/&color=/') == {'name': '/', 'color': '/'}
    assert parse_cookie('name:/;/=dima') == {'name': '', '/': 'dima'}
    assert parse_cookie('name:/?/= ?dima?') == {'name:/?/': '?dima?'}
