# DataLink

A simple class to monitor a remote directory via SSH and transfer any newly created files to the local server

Usage is simple, create DataLink object and open connection

```
dev = Data_link()
    
dev.open_ssh()
dev.open_sftp()
```

Specific a remote directory to monitor and transfer and newly created files

```
dev.wait_new_file(remote_directory = 'Desktop/test')

dev.transfer_data(local_directory = 'transfered_data')
```

Close connection

```
dev.close_sftp()
dev.close_ssh()
```
