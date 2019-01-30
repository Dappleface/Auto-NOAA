#Yikes this is not going to be goo*d to begin with
#insatlling and updating packages
echo "this script requires root"
echo "testing for sudo"
timeout 2 sudo id && echo "Sudo Detected, Continuing" || echo "please try again with sudo"
echo "Updating and Installing required packages"

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install pip python3 
echo "done"
