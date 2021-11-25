import paramiko
import os

class DataLink():
    
    
    def __init__(self):
        
        """
        Detect new files using SSH and transfer to server using SFTP
        
        Server, IPv4 connection properties: 'Shared to other computers'

        Server address: 10.42.0.1

        Device address: 10.42.0.91
        
        requirements:
            sudo apt-get install inotify-tools
            
        """
        # SFTP
        self.transport = paramiko.Transport(('10.42.0.91'))
        
        # SSH
        self.ssh_client = paramiko.SSHClient()

        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    
    def open_sftp(self):
        
        self.transport.connect(username='danie', password='1926')

        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        
    
    def open_ssh(self):
        self.ssh_client.connect(hostname='10.42.0.91', username='danie', password='1926')

    
    def close_sftp(self):
        self.sftp.close()
        

    def close_ssh(self):
        self.ssh_client.close()


    def wait_new_file(self):

        (stdin, stdout, stderr) = self.ssh_client.exec_command(
        '''    
        inotifywait Downloads/Hiya -e create|
            while read dir action file; do
                #echo "'$file'"
                echo $file
            done
        ''')
        self.new_file = stdout.readlines()[0].replace('\n', '')
        return self.new_file
        
        
    def transfer_data(self):
        self.sftp.get('Downloads/Hiya/' + self.new_file, 'transfered/' + self.new_file)
        

if __name__ == "__main__":
    
    dev = Data_link()
    
    dev.open_ssh()
    dev.open_sftp()
    
    # Wait for file to be created in monitored remote directory
    dev.wait_new_file()
    # Transfer newly created file into local directory
    dev.transfer_data()
    
    dev.close_sftp()
    dev.close_ssh()
