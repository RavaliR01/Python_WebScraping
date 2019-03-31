from flask import Flask, render_template, request
import pandas as pd


app = Flask("__name__")

@app.route("/")
def index():
    df = pd.read_csv("/Users/ns/CGF_Project/pex_menu_sheet1.csv")
    pex_kcal = df[['Item', 'kcal']]
    pex_kcal_sorted = pex_kcal.sort_values(by=['kcal'])
    pex = pex_kcal_sorted.to_html(index=False)
    return(pex)

app.run(debug=True)
