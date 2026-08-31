# You just need to run this code to install the voice model 
# If the two files are not in the same folder as main.py then add the path of the respective file in the main code 

import urllib.request

url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx"
config_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx.json"

urllib.request.urlretrieve(url, "en_US-amy-medium.onnx")
urllib.request.urlretrieve(config_url, "en_US-amy-medium.onnx.json")

print("Amy voice downloaded successfully.")