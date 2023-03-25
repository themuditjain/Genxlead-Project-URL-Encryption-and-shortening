from flask import Flask, request, render_template
import pyshorteners
import hashlib
# Flask constructor
app = Flask(__name__)  

def get_short_url(url):
    # Use SHA256 to hash the URL
    hash_object = hashlib.sha256(url.encode())
    hash_value = hash_object.hexdigest()
    # Take the first 8 characters of the hash value as the shortened URL
    short_url = hash_value[:8]
    return short_url

@app.route('/', methods =["GET", "POST"])
def shorten_url():
    if request.method == "POST":
       url = request.form.get("url")
       url = get_short_url(url)
    #    type_tiny = pyshorteners.Shortener()
    #    short_url = type_tiny.tinyurl.short(url)
       return "Shortened URL is "+url
    return render_template("form.html")

if __name__=='__main__':
   app.debug = True
   app.run()