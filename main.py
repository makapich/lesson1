def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=+380502924354&color=2+2') == {'name': '380502924354', 'color': '2 2'}
    assert parse('https://example.com/path/to/page?name=&&color=&&exempe==name=') == {'name': '', 'color': '', 'exemple': '=name='}
    assert parse('https://example.com/path/to/page?name=&&color=&&exempe=?name?') == {'name': '', 'color': '', 'exemple': '?name?'}
    assert parse('https://example.com/path/to/page?name=?/&color=/&&exempe=?name=/') == {'name': '?/', 'color': '/', 'exemple': '?name=/'}
    assert parse('https://example.com/path/to/page?name=?/&color=/p&exempe=?name=/&&main=1000') == {'name': '?/', 'color': '/p', 'exemple': '?name=/', 'main': '1000'}
    assert parse('https://example.com/path/to/page?name=https://example.com/') == {'name': 'https://example.com/'}
    assert parse('https://example.com/path/to/page?name=діма&color=червоний') == {'name': 'діма', 'color': 'червоний'}
    assert parse('https://example.com/path/to/page?name=/&color=/') == {'name': '/', 'color': '/'}
    assert parse('https://example.com/path/to/page?name:/&/=dima') == {'name': '', '/': 'dima'}
    assert parse('https://example.com/path/to/page?name:/?/= ?dima?') == {'name:/?/': '?dima?'}

def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
