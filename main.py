from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    uusi_nimi = request.args["nimi"]
    uusi_nimi = uusi_nimi * 2
    
    #with open("kaikki_nimet.txt", "a") as nimitiedosto:
    #    nimitiedosto.write(uusi_nimi + "\n")
    
    #kaikki_nimet = open("kaikki_nimet.txt").read()
    #return render_template('vastaus.html', nimi=kaikki_nimet)
    #return render_template('vastaus.html', nimi=request.args['nimi'])
    return render_template('vastaus.html', nimi=uusi_nimi)

if __name__ == '__main__':
    app.run()
    
    