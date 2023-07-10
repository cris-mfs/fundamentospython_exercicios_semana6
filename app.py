from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RespostaForm, MensagemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo' # chave que tem que existir para ele poder utilizar formulários

respostas = ['laranja', 'lisboa', 'benfica']
mensagens = []

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/desafios", methods=['GET', 'POST'])
def desafios():
    if request.method == "POST":
        respostas_dadas=[
        request.form.get("resposta1"),
        request.form.get("resposta2"),
        request.form.get("resposta3")
        ]
        if respostas_dadas == respostas:
                return redirect(url_for('end'))
        else:
            flash('Erraste pelo menos uma das perguntas. Tenta novamente.', 'error') 
    return render_template('desafios.html')

@app.route("/end", methods=['GET', 'POST'])
def end():
    form = MensagemForm()
    if form.validate_on_submit():
        mensagem = form.mensagem.data
        mensagens.append(mensagem)
        print(f'Mensagem recebida: {mensagem}') # Print da mensagem no terminal
        flash(f'Mensagem enviada com sucesso! Já existem {len(mensagens)} mensagem(s).', 'success') # Print de mensagem na página
    return render_template('end.html', form=form)

@app.route("/mensagens")
def ver_mensagens():
    return render_template('mensagens.html', mensagens=mensagens)

if __name__ == "__main__":
    app.run()