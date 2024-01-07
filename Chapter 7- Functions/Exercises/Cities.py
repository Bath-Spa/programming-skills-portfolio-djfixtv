def describe_city(city, country='France'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Paris')
describe_city('Tokyo', 'Japan')
describe_city('Versailles')