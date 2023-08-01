from flask import Flask,render_template,request,send_file
from hybrid_crypto import *
import os
import shutil

app=Flask(__name__)

app.config["UPLOAD_PATH"] = "uploads"

key1=''

def encrypt(txt,key):
    text=hybrid_enc(txt,key)
    return text

def decrypt(txt,key):
    text=hybrid_dec(txt,key)
    return text

    
@app.route("/")
def home():
    return render_template("index.html")

    
@app.route("/upload_file",methods=["POST","GET"])
def upload_file():
    if request.method=="POST":
        f=request.files['file_name']
        key=request.form['password']
        f.save(os.path.join(app.config["UPLOAD_PATH"],f.filename))

        f1=open("C:/isaa project final/uploads/"+f.filename,"r")
        txt=""
        for text in f1.read():
            txt+=text
        f1.close()

        txt=encrypt(txt,key)

        f1=open("C:/isaa project final/uploads/"+f.filename,"w")
        f1.write(txt)
        f1.close()

        return render_template("index.html")
    return render_template("upload_file.html",msg="please choose a file")



@app.route("/download",methods=["POST","GET"])
def download_file():
    if len(os.listdir("temp"))!=0:
        for file in os.listdir("temp"):
            os.remove("C:/isaa project final/temp/"+file)

    if request.method=="POST":
        file=request.form["file"]
        key=request.form["passwd"]
        l=os.listdir("C:/isaa project final/uploads")
        
        
        if file in l:
            shutil.copy("C:/isaa project final/uploads/"+file,"temp")
            
            f1=open("C:/isaa project final/temp/"+file,"r")
            txt=""
            for text in f1.read():
                txt+=text
            f1.close()
            
            txt=decrypt(txt, key)

            f1=open("C:/isaa project final/temp/"+file,"w")
            f1.write(txt)
            f1.close()

            return send_file("C:/isaa project final/temp/"+file,as_attachment=True)
    l=os.listdir("uploads")
    return render_template("download.html",List=l)

if __name__=="__main__":
    app.run(debug=True)
    


    