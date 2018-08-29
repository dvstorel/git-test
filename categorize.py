# Lighting baseline categorization algorithm
# David Storelli
# 28 August 2018

def categorize_bulb_type(*args):
    """ **function description here**

    accepted arguments:
    - app:
    - base_type:
    - bulb_shape:
    - length:
    - cct:
    - voltage:
    - subtype:
    - subtype1:
    - subtype2:

    doctest
    >>> categorize_bulb_type('app: outdoor')
    'outdoor'
    >>> categorize_bulb_type('app: three way')
    'three way'
    >>> categorize_bulb_type('base_type: cand')
    'd-c-exempt'

    """
    bulb_type = None
    application = None
    base_type = None
# argument handler
    for arg in args:
        if arg[:4] == 'app:':
            application = arg[5:]
        if arg[:10] == 'base_type:':
            base_type = arg[11:]
            #print(base_type)
        if arg[:11] == 'bulb_shape:':
            bulb_shape = arg[12:]
            #print(bulb_shape)
        if arg[:6] == 'watts:':
            watts = arg[7:]
            #print(watts)
        if arg[:7] == 'length:':
            length = arg[8:]
            #print(length)
        if arg[:4] == 'cct:':
            cct = arg[5:]
            #print(cct)
        if arg [:8] == 'voltage:':
            voltage = arg[9:]
            #print(voltage)
        if arg[:8] == 'subtype:':
            subtype1 = arg[9:]
            #print(subtype1)
        if arg[:9] == 'subtype1:':
            subtype1 = arg[10:]
            #print(subtype1)
        if arg[:9] == 'subtype2:':
            subtype2 = arg[10:]
            #print(subtype2)

# decision tree
    if application:
        if application is not 'general':
            bulb_type = application

    if base_type:
        if base_type is 'cand' or 'int':
            bulb_type = 'd-c-exempt'


    return bulb_type


if __name__ == "__main__":
    out = categorize_bulb_type('app: outdoor')
    print(out)
