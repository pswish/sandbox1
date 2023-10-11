### Written by Paul Swisher, (c) 2023, all rights reserved
# =========== run this in the location you put your keys like your OpenSSL/ directory ==========
# Version 1.0 : This version only tested on MacOS and creates RSA keys

from subprocess import Popen, PIPE

class Encoder:

    try:
        def __init__(self) -> None: 
            self.username = input('Please input your user name : \n')
            self.message = input('Please input your message:\n')

        @classmethod
        def writeMessageToFile(self):  
            # mkdir OpenSSL in home or user
            command = 'cd ~; mkdir OpenSSL; cd OpenSSL; touch unencryptedMessage.txt'
            self.run_command(command)
            self.filePath = '/Users/' + self.username + '/OpenSSL/unencryptedMessage.txt'
            with open(self.filePath, "w") as f:
                f.write(str(self.message + ": " + self.username))
                f.close() 

        @staticmethod
        def generate_RSA_keys():
            # Generate RSA key:
            generateRSA1 = 'openssl genrsa -out key.pem 1024'
            generateRSA2 = 'openssl rsa -in key.pem -text -noout'

            # Save public key in pub.pem file:
            savepublickey1 = 'openssl rsa -in key.pem -pubout -out pub.pem'
            savepublickey2 = 'openssl rsa -in pub.pem -pubin -text -noout'

        @classmethod
        def encrptyMessage(self):
            # openssl command to encrypt
            command = 'openssl rsautl -encrypt -inkey pub.pem -pubin -in ' + self.filePath + ' -out encyptedMessage.bin'
            p = self.run_command(command)
            print(p)

        # @classmethod
        # def decryptMessage(self):
        #     # openssl or openssh command to decrypt
        #     decrypt_Command = 'openssl rsautl -decrypt -inkey key.pem -in encyptedMessage.bin'
        #     self.run_command(decrypt_Command)
        # next version

        # def printMessage(self):
        #     self.run_command('cat messageDecrypted')
        #     # Output message decrypted to user
        # next version

    except Exception as e:
         print(e)


    @staticmethod
    def run_command(commands_with_args):
        # This function controls the running of shell commands
        # Returns output and err to the calling function
        p = Popen(commands_with_args, shell=True, bufsize=8 * 1024, stdout=PIPE, stderr=PIPE)
        (output, err) = p.communicate()
        return output, err
    
def main():
    code = Encoder()
    code.writeMessageToFile()
    code.encrptyMessage()
    # code.generate_RSA_keys()  next version (if needed)
    # code.decryptMessage()  next version

main()
