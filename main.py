from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    uusi_nimi = request.args["nimi"]
    uusi_nimi = uusi_nimi 
    
    lempinimi = request.args["lempinimi"]
    
    loppuliitteet = ["-ski", "-ster", "-y", "-o", "-man"]
    
    liite = random.choice(loppuliitteet)
    
    uusi_lempinimi = uusi_nimi + liite
    
    #with open("kaikki_nimet.txt", "a") as nimitiedosto:
    #    nimitiedosto.write(uusi_nimi + "\n")
    
    #kaikki_nimet = open("kaikki_nimet.txt").read()
    #return render_template('vastaus.html', nimi=kaikki_nimet)
    #return render_template('vastaus.html', nimi=request.args['nimi'])
    return render_template('vastaus.html', nimi=uusi_nimi, lempinimi=uusi_lempinimi)

if __name__ == '__main__':
    app.run()
    
    