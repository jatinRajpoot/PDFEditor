from flask import Flask, render_template, request, send_from_directory, send_file
from werkzeug.utils import secure_filename
import os
import time
import pdftoolsmain


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/pdf", methods=["post"])
def pdf():
    # Reciving files from the user
    if request.method == "POST":
        # making a list 
        files = request.files.getlist('pdf')
        instance = str(time.time_ns())
        listofpath = []
        for file in files:
            timeinnanosec = time.time_ns()
            secure_name = secure_filename(file.filename)
            path = os.path.join("D:\\Projects\\pdftools\\uploads\\", str(
                timeinnanosec)+secure_name)
            listofpath.append(path)
            file.save(path)
        pdftoolsmain.mergerpdf(listofpath, instance)
        return send_from_directory("D:\\Projects\\pdftools\\static", instance+".pdf")

    os.remove("D:\\Projects\\pdftools\\static"+instance+".pdf")




if __name__ == "__main__":
    app.run(debug=True)
