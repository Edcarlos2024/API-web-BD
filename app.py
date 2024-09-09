from flask import Flask, request, jsonify
from bd import Pessoa

app = Flask(__name__)

@app.route('/pessoa', methods=['POST'])
def criar_usuario():
    dados = request.json
    cpf = dados.get('cpf')
    
    for usuario in Pessoa:
        if usuario['cpf'] == cpf :
            return jsonify(mensagem = 'Esse usuário já existe!')
    
    usuario = {
        'cpf': cpf,
        'nome': dados.get('nome'),
        'data_nascimento': dados.get('data_nascimento')
    }

    Pessoa.append(usuario)

    return jsonify(mensagem = 'Usuário criado com sucesso!')

@app.route('/pessoa/<int:cpf>', methods=['GET'])
def get_pessoa(cpf):
    for usuario in Pessoa:
        if usuario['cpf'] == cpf:
            return jsonify(usuario)
    
    return jsonify(mensagem = 'Usuário não encontrado!')

if __name__ == '__main__':
    app.run(debug=True)

