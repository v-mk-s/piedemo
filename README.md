# piedemo

Set up rclone tool for better experience:  

```commandline
curl https://rclone.org/install.sh | sudo bash
rclone config
```

After that use Google Drive hosting and verify your account.
If you use remote connection, verify your account via port forwarding. 
```ssh -L localhost:53682:localhost:53682 ...```

You can simply host your file in Google Drive and use it everywhere you want:
```commandline
python -m piedemo host 1.txt
Host model option
Transferred:              0 B / 0 B, -, 0 B/s, ETA -
Checks:                 1 / 1, 100%
Elapsed time:         1.7s
Url: 
https://drive.google.com/open?id=1nN64iU6EY490YMjI3GHfNQhbN4tVmhtu
Filename: 
1.txt
Code:
PretrainedCheckpoint(gdrive='1nN64iU6EY490YMjI3GHfNQhbN4tVmhtu',
                     filename='1.txt')
```

