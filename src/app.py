import os
from flask import Flask, render_template, request, flash, redirect, url_for
from spellcheck import SpellChecker

app = Flask(__name__)
# Tarvitaan flash-viestien käyttöön
app.secret_key = 'salainen'
spell_checker = SpellChecker()
# SpellChecker-luokkaan ladataan sanoja tarkistusta varten
spell_checker.load_dictionary(
    ['testi', 'testit', 'sana', 'kissa', 'kissan', 'kissat', 'koira'])
spell_checker.load_dictionary_from_file(
    # Lataa sanalista tiedostosta
    os.path.join(os.path.dirname(__file__), 'sanakirja', 'kaikkisanat.txt'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spellcheck', methods=["POST"])
def spellcheck():
    # Sanoja vertaillaan pienillä kirjaimilla helppottakseen vertailua
    submitted_text = request.form.get('text').strip()
    text = submitted_text.lower()
    # Tallennetaan alkuperäinen teksti flash-viestejä varten
    original_text = submitted_text
    # Jaetaan teksti sanoiksi
    text = text.split()
    if not text:
        flash('Anna tarkistettava sana tai lause.')
        return redirect(url_for('index'))

    flash(f'Tarkistetaan teksti: "{original_text}"')

    for word in text:
        if not spell_checker.is_correct(word):
            flash(f'Sana "{word}" on mahdollisesti väärin kirjoitettu.')
            suggestions = spell_checker.suggest(word)
            if suggestions:
                flash(
                    f'Ehdotuksia sanalle "{word}": ' + ', '.join(suggestions))
        else:
            flash(f'Sana "{word}" on oikein kirjoitettu.')
    return redirect(url_for('index'))
