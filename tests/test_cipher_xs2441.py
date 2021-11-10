from cipher_xs2441 import cipher_xs2441

def test_cipher(): 
    example = 'Apple'
    expected = 'Dssoh'
    actual = cipher_xs2441.cipher(example, 3)
    assert actual == expected
    
