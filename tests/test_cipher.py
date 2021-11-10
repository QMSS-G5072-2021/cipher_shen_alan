#!/usr/bin/env python
# coding: utf-8

# In[ ]:
def cipher(text, shift, encrypt = True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index + 1]
    return new_text

def test_cipher(): 
    example = 'Apple'
    expected = 'Dssoh'
    actual = cipher(example, 3)
    assert actual == expected
    
test_cipher()


# In[ ]:


def test_cipher_negative():
    example = 'Tea'
    expected = 'RcY'
    actual = cipher(example, -2)
    assert actual == expected
    
test_cipher_negative()


# In[ ]:


def test_cipher_symbol(): 
    example = '@pple'
    expected = '@ssoh'
    actual = cipher(example, 3)
    assert actual == expected
    
test_cipher_symbol()


# In[ ]:


import pytest

def cipher_assert(text, shift, encrypt=True):
    assert type(shift)!=str ,'Shift parameter should be an integer'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:         # not exist in the alphabet
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


# In[ ]:


def test_cipher_string():
    with pytest.raises(AssertionError):
        cipher_assert('Apple',"two")

test_cipher_string()

