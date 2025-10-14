from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home ():
    pide_datos = ["Nombre:","Apellido:","Edad:"]
    
    #Traemos datos Ingresados
    name_info = ""
    lastname_info = ""
    age_info = ""
    
    if request.method == "POST":
        name_info = request.form.get("nombre")
        lastname_info = request.form.get("apellido")
        age_info = request.form.get("edad")
        
    email_generado = f"{lastname_info.capitalize()}{name_info.lower()}{age_info}@gmail.com"
        
    return render_template("index.html",dat_pedi=pide_datos, email_re=email_generado)
    
    


if __name__ == "__main__":
    app.run(debug=True)