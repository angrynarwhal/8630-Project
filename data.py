import requests

def download_dropbox_file(url, save_path):
    """
    Download a file from a Dropbox URL and save it to a specified path.
    
    :param url: str - The Dropbox URL of the file to download.
    :param save_path: str - The local path to save the downloaded file.
    """
    try:
        # Modify Dropbox URL for direct download
        if "www.dropbox.com" in url:
            url = url.replace("www.dropbox.com", "dl.dropboxusercontent.com")
        elif "?dl=0" in url:
            url = url.replace("?dl=0", "?dl=1")
        
        # Send a GET request to the modified URL
        response = requests.get(url, stream=True)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Write the content to a file
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"File downloaded successfully and saved to: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")

# Example usage
if __name__ == "__main__":
    # Original Dropbox URL
    url = "https://www.dropbox.com/scl/fi/953otkig0m2eqrno0mnic/oss-cncf-networks.zip?rlkey=rm13irhmtamv7othi24tftgp5&st=zgbce3nb&dl=0"
    
    # Local path to save the downloaded file
    save_path = "data.zip"
    
    download_dropbox_file(url, save_path)


