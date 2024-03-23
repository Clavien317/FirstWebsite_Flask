from flask import Flask,render_template,request
import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tp"
)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/inscription")
def inscrir():
    return render_template("inscription.html")


@app.route("/traitement/inscription",methods=["POST"])
def traitement():
    data = request.form
    nom = data.get("nom")
    email = data.get("email")
    password = data.get("password")
    stm = mydb.cursor()
    sql=("INSERT INTO user (nom,email,password) VALUES (%s,%s,%s)")
    val = (nom,email,password)
    stm.execute(sql,val)
    if stm.rowcount > 0:
        stm = mydb.cursor()
        stm.execute("SELECT * FROM user")
        result = stm.fetchall()
        return render_template("liste.html",resultat = result)
    else:
        return "Aucune donnée insérée, erreur d'insertion de données..."
mydb.commit()



@app.route("/liste")
def liste():
    stm = mydb.cursor()
    stm.execute("SELECT * FROM user")
    result = stm.fetchall()
    print(result)
    return render_template("liste.html",resultat = result)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)