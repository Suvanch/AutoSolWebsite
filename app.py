from contextlib import _RedirectStream
from flask import Flask, render_template, request, send_file,redirect,url_for, send_from_directory
import json
import autoSol as c

app = Flask(__name__, static_folder="c:\\Users\\suvan\\VSCode\\HTMLWebsite\\static")
@app.route("/")
def home():
    return render_template("home.html")



#def generateToken():
#   text1=""
#   if request.method == 'POST':
#       # check if the post request has the file part
##      
#       tname = request.form['tname']
#       tsymbol = request.form["tsymbol"]
#       tsupply = request.form["tsupply"]
#       terms = request.form.get("terms")
#       #make contract
#       print(tname)
##       print(tsymbol)
  #     print(tsupply)
  #     print(terms)
  #     contract = c.contractData(tname,tsymbol,tsupply)
  #     c.basicContract(contract)
  # return render_template("home.html")
  
#listnes from js and waits till person buys
@app.route('/postmethod', methods = ['GET','POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    jsddata = request.form['soulMetaData']
    with open('solMeta.json', 'w') as outfile:
        outfile.write(jsddata)
    contract = c.readJson()
    c.createContract(contract)
    return render_template("home.html")
    #return "redirect(url_for('templates',filename='downloadPage.html'))"

    
@app.route('/back', methods = ['POST'])
def back():
    return send_from_directory('reports', "c:\\Users\\suvan\\VSCode\\HTMLWebsite\\templates\\home.html")
    #return "redirect(url_for('templates',filename='downloadPage.html'))"

@app.route('/download')
def download_file():
    file = open('solMeta.json')
    data = json.load(file)
    print("hi")
    path = "contracts\\"+data['symbol']+".sol"
    #path  = "contracts\\lk.sol"
    return send_file(path, as_attachment=True)
    

@app.route('/downloadPage', methods = ['GET','POST'])
def downloadPage():
    print("hi")
    return redirect(url_for('static',filename='downloadPage.html'))
    #return render_template("downloadPage.html")
    #return redirect('downloadPage.html')

#@app.route('/')
#def returnData():
    #data = c:\Users\suvan\VSCode\HTMLWebsite\contracts\hi2.sol
    #return render_template('settings.html', data=data)

def changeJson(tname):
    print(tname)
    with open("solMeta.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["name"] = tname

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()
    