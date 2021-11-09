def cipher(text, shift, encrypt=True):
    
    """Encypt text input using a basic (Caesar cipher) by shifting each alphabet left or right by a certain number
    Parameters
    ----------
    text : str
        Text to be encrypted
    shift : int
        Number of alphabet positions the text will be shifted
    encrypt: bool
        True by default
        
    Returns: encypted (or decrypted) string
    -------
    Examples: 
    >>> cipher(today, 1)
    upebz
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text