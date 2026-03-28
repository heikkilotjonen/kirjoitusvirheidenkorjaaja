from flask import Flask, render_template, request, flash, redirect, url_for
from spellcheck import SpellChecker

app = Flask(__name__)
# Tarvitaan flash-viestien käyttöön
app.secret_key = 'salainen'
spell_checker = SpellChecker()
# SpellChecker-luokkaan ladataan sanoja tarkistusta varten
spell_checker.load_dictionary(['testi', 'sana', 'kissa', 'koira', 'markka'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spellcheck', methods=["POST"])
def spellcheck():
    # Sanoja vertaillaan pienillä kirjaimilla helppottakseen vertailua
    text = request.form['text'].strip().lower()
    if spell_checker.is_correct(text):
        flash('Sana on oikein kirjoitettu.')
        return redirect(url_for('index'))
    else:
        flash('Sana on väärin kirjoitettu.')
        # Jos sana on väärin kirjoitettu, haetaan ehdotuksia korjauksiksi
        suggestions = spell_checker.suggest(text)
        if suggestions:
            flash('Ehdotuksia: ' + ', '.join(suggestions))
        return redirect(url_for('index'))
