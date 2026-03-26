from flask import Flask, render_template, request, flash, redirect, url_for
from spellcheck import SpellChecker

app = Flask(__name__)
app.secret_key = 'salainen'                                               # Tarvitaan flash-viestien käyttöön
spell_checker = SpellChecker()
spell_checker.load_dictionary(['testi', 'sana', 'kissa', 'koira'])        # SpellChecker-luokkaan ladataan sanoja tarkistusta varten 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spellcheck', methods=["POST"])
def spellcheck():
    text = request.form['text'].strip().lower()
    if spell_checker.is_correct(text):
        flash('Sana on oikein kirjoitettu.')
        return redirect(url_for('index'))
    else:
        flash('Sana on väärin kirjoitettu.')
        suggestions = spell_checker.suggest(text)
        if suggestions:
            flash('Ehdotuksia: ' + ', '.join(suggestions))
        return redirect(url_for('index'))