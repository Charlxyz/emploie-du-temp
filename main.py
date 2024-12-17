from flask import Flask, render_template, redirect, url_for, request
from Class import Professeur, Classe, Etudiant, Salle, Horaire, createBDD

# Initialisation de la base de données et création d'une session
Session = createBDD()
db_session = Session

app = Flask(__name__, template_folder="./templates")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if "add-student" in request.form:
            # Récupérer les données du formulaire
            nom = request.form['nom']
            prenom = request.form['prenom']
            age = int(request.form['age'])
            classe_id = int(request.form['classe'])

            # Créer un nouvel étudiant
            student = Etudiant(
                nom=nom,
                prenom=prenom,
                age=age,
                classe_id=classe_id
            )
            # Ajouter l'étudiant à la session et sauvegarder
            db_session.add(student)
            db_session.commit()

            # Rediriger vers la page principale
            return redirect(url_for('index'))

    # Charger les données nécessaires pour afficher dans le template
    classes = db_session.query(Etudiant).all()
    return render_template("index.html", classes=classes)

if __name__ == '__main__':
    app.run(debug=True)
