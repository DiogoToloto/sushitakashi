from flask import Flask, render_template, url_for

meu_site = Flask(__name__)

# primeira pagina do site

# route -> é o caminho que vem depois do dominio Ex: SushiTakashi.com.br/""home""

#função -> o que voce quer exibir naquela pagina
@meu_site.route("/")
def homepage():
    return render_template("home.html")

@meu_site.route("/contatos")
def contactspage():
    return render_template("contatos.html")

@meu_site.route("/menu")
def menupage():
    return render_template("menu.html")

@meu_site.route("/galeria")
def gallerypage():
    return render_template("galeria.html")

@meu_site.route("/blog")
def blogpage():
    return render_template("blog.html")

@meu_site.route("/reservas")
def reservationspage():
    return render_template("reservas.html")
 

# colocar site no ar
if __name__ == "__main__":
    meu_site.run(debug= True)