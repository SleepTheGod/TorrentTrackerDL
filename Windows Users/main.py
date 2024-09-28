import subprocess

def download_torrent(magnet_link):
    command = ["aria2c", magnet_link]
    
    try:
        subprocess.run(command, check=True)
        print("Download started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading: {e}")

if __name__ == "__main__":
    magnet_link = input("Please paste the magnet link you would like to download: ")
    
    if not magnet_link.startswith("magnet:?xt=urn:btih:"):
        print("Invalid magnet link. Please ensure it starts with 'magnet:?xt=urn:btih:'.")
    else:
        download_torrent(magnet_link)
