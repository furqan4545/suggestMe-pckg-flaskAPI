from flask import Flask, render_template, url_for, request, jsonify, make_response, flash, redirect
import requests
import json
import os
import numpy as np
import math


app = Flask(__name__)

def calculate(nbot, prices = 0, pieces = 11):
    # pieces = 11
    qbox1 = pieces * 24

    if nbot >= pieces and nbot < qbox1:
        boxes = 0

        j = nbot / pieces
        packs = math.floor(j)
        j = j % 1
        j = str(j)
        kk = int(j[2:4])
        if kk == 00:
            ll = 0
        else:
            s = int(j[2:3])
            ll = s + 1

        result = [ll, packs, boxes]
        return result


    elif nbot >= qbox1:
        j = nbot / qbox1
        bpacks = math.floor(j)
        
        kl = bpacks * qbox1
        llp = nbot - kl
        if llp >= pieces:
            jj = llp / pieces
            packs = math.floor(jj)
            jj = jj % 1
            jj = str(jj)
            kk = int(jj[2:4])
            if kk == 00:
                ll = 0
            else:
                s = int(jj[2:3])
                ll = s + 1

        result = [ll, packs, bpacks]
        return result

    else:
        boxes = 0
        packs = 0
        result = [nbot, packs, boxes]
        return result


@app.route('/', methods=['GET', 'POST'])
def index():
    dicti = data()
    return render_template('app.html',predic=dicti)


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        try:
            nbot = int(request.form.get('nbot'))
            choc = int(request.form.get('choc'))
            bis = int(request.form.get('bis'))
            
            response = {"bottles" : nbot, "choclates" : choc, "Biscuits" : bis}
            print(response)

            rs = calculate(nbot, pieces=11)
            rs2 = calculate(choc, pieces=11)
            rs3 = calculate(bis, pieces=11)
            
            return jsonify({
                "n_bottles" : rs[0],
                "n_packs" : rs[1],
                "n_boxes" : rs[2],
                "n_choclates" : rs2[0],
                "n_cpacks" : rs2[1],
                "n_cboxes" : rs2[2],
                "n_biscuits" : rs3[0],
                "n_bpacks" : rs3[1],
                "n_bboxes" : rs3[2]
            })

            
        except:
            return "Please check if the values are entered correctly"


if __name__ == "__main__":
    app.run(debug=True)
    

