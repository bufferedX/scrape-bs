# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:02:52 2021

@author: basus
"""
from flask import Flask,make_response,Response
from io import StringIO
import .webScraper
app = Flask(__name__)

legend = '''Currently this app is under development.<br/> Releasing beta version 0.0.1 of this
application for public use.<br/> Will keep updating it iterations, with better UI and ease of
access, and more customizeable data to download. <br/><br/> 
THIS IS JUST THE BEGINNING. 
<br/><br/><br/>
HOW TO USE:<br/>
    1. If you want the PASSING statistics of Premier League clubs (overall) the just add
    /passing at the end of the url to get it.<br/>
    2.The data avilable to download currently is at the squad level and of the following aspects of the game <br/><br/>
    -STANDARD STATS<br/><br/>
    -SHOOTING STATS<br/><br/>
    -PASSING STATS<br/><br/>
    -POSSESSION STATS<br/><br/>
    -DEFENSE STATS<br/><br/>
    -SHOT CREATING ACTIONS/GOAL CREATING ACTIONS(use /gca to retrieve)<br/><br/>
    -KEEPER STATS<br/><br/>

I currently have the player and team level data scraped and available. <br/>
Need to make changes to this web app to make it available to you all.<br/><br/><br/>

Since this is the beta version, you all might face issues, please write to me at basu.sandipani@gmail.com for any bugs or issues you see.
<br/><br/>

Thank you :)
    
    '''

@app.route("/")
def index():
    return legend

@app.route("/<stat>")
def getCsv(stat):
    output = StringIO()
    webScraper.pl_all(stat).to_csv(output,index=False)
    return Response(output.getvalue(), mimetype="text/csv",headers={"Content-disposition":
                 "attachment; filename="+stat+".csv"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
