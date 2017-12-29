import sys

def caesarEncrypt(plaintext1, numShift):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    chipertext = ""

    for  ch in plaintext1:
        idx=alphabet.find(ch)
        ciphertext1=chipertext1+key[idx+numShift]
    else:
        chipertext1=chipertext1+ch

    return ciphertext1

    
def caesarDecrypt(chipertext2, numberShift):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    
    for ch in chipertext2:
        idk=alphabet.find(ch)
        plaintext2=plaintext2-key[idx+numberShift]
    else:
        plaintext2=plaintext-ch

    return plaintext2
    

def caesarBreak(message):
    ''' FILL IN YOUR CODE HERE '''
    ''' THE LINE return None  SHOULD BE LAST LINE IN THIS FUNCTION '''

    return None



def main():

    shift = int(sys.argv[1])
    inmsg = input('Please enter the message you want to encrypt/decrypt:\n')
    print()

    encryptedmsg = caesarEncrypt(inmsg, shift)
    print("The encrypted message is: " + encryptedmsg)

    decryptedmsg = caesarDecrypt(encryptedmsg, shift)
    print("The decrypted message is: " + decryptedmsg + "\n\n")

    print("We will now try to break the msg: 'we ovugpzghugpu lylz pungwyvnyhttpungshunahnl'\n\n")

    secretmsg = 'we ovugpzghugpu lylz pungwyvnyhttpungshunahnl'
    caesarBreak(secretmsg)

main()
