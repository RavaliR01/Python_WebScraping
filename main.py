from flask import *
import pandas as pd


app = Flask("myapp")

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/Menus")
def menus():
    pex_df = pd.read_csv("/Users/ns/CFG_Project/pex_menu_sheet1.csv")
    pex_df_red = pex_df[['Item', 'kcal', 'kJ', 'Fat g', 'Carbs g', 'Sugars g', 'Fibre g', 'Protein g', 'Salt g']]
    zi_df = pd.read_csv("/Users/ns/CFG_Project/zizzi_menu.csv")
    zi_df_final = zi_df.dropna()
    return render_template('tables.html',tables=[pex_df_red.to_html(index=False), zi_df_final.to_html(index=False)],
    titles = ['na','Pizza Express', 'Zizzi'])


@app.route("/Calculator")
def calc():
    pex_df_c = pd.read_csv("/Users/ns/CFG_Project/pex_menu_sheet1.csv")
    pex_df_red_c = pex_df_c[['Item']]
    zi_df_c = pd.read_csv("/Users/ns/CFG_Project/zizzi_menu.csv")
    zi_df_final_c = zi_df_c[['MENU ITEM']].dropna()
    pex_df_red_ca = pex_df_red_c.to_html(index=False)
    zi_df_final_ca = zi_df_final_c.to_html(index=False)
    return pex_df_red_ca, zi_df_final_ca

app.run(debug=True)








# import foursquareapi
# from flask import Flask, render_template, request, json
# app = Flask("foursquareapi")
# url = 'https://api.foursquare.com/v2/venues/explore'
# params = dict(
# client_id='CLIENT_ID',
# client_secret='CLIENT_SECRET',
# v='20180323',
# ll='40.7243,-74.0018',
# query='zizzi',
# limit=1
# )
# resp = requests.get(url=url, params=params)
# data = json.loads(resp.text)
# app.run(debug=True)
