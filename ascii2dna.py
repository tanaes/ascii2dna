### frm, to, and convert are from https://www.quora.com/How-do-I-write-a-program-in-Python-that-can-convert-an-integer-from-one-base-to-another/answer/Nayan-Shah

def frm(x, b):
    """
    Converts given number x, from base 10 to base b 
    x -- the number in base 10
    b -- base to convert
    """
    assert(x >= 0)
    assert(1< b < 37)
    r = ''
    import string
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r
def to(s, b):
    """
    Converts given number s, from base b to base 10
    s -- string representation of number
    b -- base of given number
    """
    assert(1 < b < 37)
    return int(s, b)
def convert(s, a, b):
    """
    Converts s from base a to base b
    """
    return frm(to(s, a), b)

def asciiToDNA(chars, trans_table=None):

    if trans_table is None:
        trans_table = ['T','A','G','C']

    dna = ''

    for x in chars:
        x_4 = str(convert(str(ord(x)), 10, 4))

        while len(x_4) < 4:
            x_4 = '0' + x_4

        codon = ''
        for y in x_4:
            codon += trans_table[int(y)]

        dna += codon

    return(dna)

exp_char = '2Be'
exp_DNA = 'TCTGATTGAGAA'

assert(asciiToDNA(exp_char) == exp_DNA)

def dnaToASCII(dna, trans_table=None):

    if trans_table is None:
        trans_table = ['T','A','G','C']

    trans_dict = {x: str(i) for i,x in enumerate(trans_table)}

    chars  = ''

    try:
        assert(len(dna) % 4 == 0)
    except AssertionError:
        raise('DNA sequence not evenly divisible by 4!')

    codon = ''

    for i,x in enumerate(dna):
        if (i + 1) % 4 == 0:
            codon += x
            x_4 = ''.join([trans_dict[y] for y in codon])
            chars += chr(int(convert(x_4,4,10)))
            codon = ''
        else:
            codon += x

    return(chars)

assert(dnaToASCII(exp_DNA) == exp_char)     
