
def kntrl(email):
    adt = 0
    for a in email:
        if a == '@':
            adt = adt + 1

    if adt == 1:
        return True
    else:
        return False


email = input('Email Adresi: ')
if (kntrl(email) == True):
    print(email+'\nemail adresiniz doğru')
else:
    print(email+'\nemail adresiniz yanlış')