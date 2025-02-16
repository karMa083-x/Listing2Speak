import flask
from flask import Flask, jsonify, render_template, send_file, request,url_for,flash,redirect
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import model
import webscrabing
server=Flask(__name__)
cors = CORS(server)
server.config['CORS_HEADERS'] = "Content-Type"
@server.route('/Ecommerce',methods=['POST','GET'])
def run():
    data=[0,0,0,0,['n/a','n/a']]
    if request.method == 'POST':
        url=request.form.get('url')
        type=request.form.get('type')
        Data=webscrabing.scrape(url)
        data=[Data[4],Data[5],Data[7],Data[8]]
        
        
        
        prediction=model.useModel(int(type)-1,[[int(Data[4]),int(Data[5]),int(Data[7]),int(Data[8])]])
        data.append(prediction)
       

    return render_template('index.html',data=data)
if __name__ ==  '__main__':
  server.run(debug=True)