from flask import request, jsonify, make_response
from app import app, db
from sqlalchemy.exc import IntegrityError
from app.models.modelos import Membros, Atas, Lideranca,Contato

from datetime import datetime

# Listar todos os membros
@app.route('/membros', methods=['GET'])
def get_membros():
    membros = Membros.query.all()

    lista_membros = []
    for membro in membros:
        lista_membros.append({
            'id': membro.id,
            'nome': membro.nome,
            'idade': membro.idade,
            'sexo': membro.sexo,
            'nascimento': membro.nascimento.strftime('%d/%m/%Y'),
            'cpf': membro.cpf,
            'rg': membro.rg,
            'e_civil': membro.e_civil,
            'cidade_estado': membro.cidade_estado
        })
    return jsonify(lista_membros)

# Obter membro pelo ID
@app.route('/membros/<int:membro_id>', methods=['GET'])
def get_membro(membro_id):
    membro = Membros.query.get(membro_id)
    if membro is None:
       return jsonify({'Error': 'Membro não encontrado'}), 404
    return jsonify({
        'id': membro.id,
        'nome': membro.nome,
        'idade': membro.idade,
        'sexo': membro.sexo,
        'nascimento': membro.nascimento.strftime('%d/%m/%Y'),
        'cpf': membro.cpf,
        'rg': membro.rg,
        'e_civil': membro.e_civil,
        'cidade_estado': membro.cidade_estado
    })

# Criar um novo membro
@app.route('/membros', methods=['POST'])
def create_membro():
    data = request.json
    nascimento_str = data['nascimento']
    nascimento = datetime.strptime(nascimento_str, '%d/%m/%Y').date()

    novo_membro = Membros(nome=data['nome'],
                         idade=data['idade'],
                         sexo=data['sexo'],
                         nascimento=nascimento,
                         cpf=data['cpf'],
                         rg=data['rg'],
                         e_civil=data['e_civil'],
                         cidade_estado=data['cidade_estado'])
    db.session.add(novo_membro)
    db.session.commit()
    return jsonify({'message': 'Membro criado com sucesso'}), 201

# Atualizar um membro
@app.route('/membros/<int:membro_id>', methods=['PUT'])
def update_membro(membro_id):
    membro = Membros.query.get(membro_id)
    if membro is None:
        return jsonify({'Error': 'Membro não encontrado'}), 404

    data = request.json
    nascimento_str = data['nascimento']
    nascimento = datetime.strptime(nascimento_str, '%d/%m/%Y').date()

    membro.nome = data['nome']
    membro.idade = data['idade']
    membro.sexo = data['sexo']
    membro.nascimento = nascimento
    membro.cpf = data['cpf']
    membro.rg = data['rg']
    membro.e_civil = data['e_civil']
    membro.cidade_estado = data['cidade_estado']

    db.session.commit()
    return jsonify({'message': 'Atualização feita com sucesso'})

# Excluir um membro
@app.route('/membros/<int:membro_id>', methods=['DELETE'])
def delete_membro(membro_id):
    membro = Membros.query.get(membro_id)
    if membro is None:
        return jsonify({'Error': 'Membro não encontrado'}), 404

    db.session.delete(membro)
    db.session.commit()
    return jsonify({'message': 'Membro excluído com sucesso'})
# end membros

# rotas para Atas

# listar todas as atas
@app.route('/atas', methods=['GET'])
def get_atas():
    atas = Atas.query.all()

    listar_atas = []
    for ata in atas:
        listar_atas.append({
            'id': ata.id,
            'numero': ata.numero,
            'tipo': ata.tipo,
            'presidente_secao': ata.presidente_secao,
            'data': ata.data.strftime('%d/%m/%Y'),
            'membros_presentes': ata.membros_presentes,
            'texto': ata.texto
        })
    return jsonify(listar_atas)

# obter uma ata pelo ID
@app.route('/atas/<int:ata_id>',methods=['GET'])
def get_ata(ata_id):
    ata = Atas.query.get(ata_id)

    if ata is None:
        return jsonify({'error':'Ata não encontrada!'}), 404
    return jsonify({
        'id': ata.id,
        'numero': ata.numero,
        'tipo': ata.tipo,
        'presidente_secao': ata.presidente_secao,
        'data': ata.data.strftime('%d/%m/%Y'),
        'membros_presentes': ata.membros_presentes,
        'texto': ata.texto
    })

# criar uma nova ata
@app.route('/atas', methods=['POST'])
def create_ata():
    ata = request.json
    data_ata_str = ata['data']

    nova_ata = Atas(numero=ata['numero'],
                    tipo=ata['tipo'],
                    presidente_secao=ata['presidente_secao'],
                    data=datetime.strptime(data_ata_str,'%d/%m/%Y').date(),
                    membros_presentes=ata['membros_presentes'],texto=ata['texto'])
    db.session.add(nova_ata)
    db.session.commit()
    return jsonify({'message':'Ata criada com sucesso!'}), 201

# atualizar uma ata
@app.route('/atas/<int:ata_id>', methods=['PUT'])
def update_ata(ata_id):
    ata = Atas.query.get(ata_id)

    if ata is None:
        return jsonify({'error':'Ata não encontrada!'}), 404
    
    data = request.json
    ata.numero = data.get('numero', ata.numero)
    ata.tipo = data.get('tipo', ata.tipo)
    ata.presidente_secao = data.get('presidente_secao', ata.presidente_secao)
    ata.data = datetime.strptime(data['data'], '%d/%m/%Y').date()
    ata.membros_presentes = data.get('membros_presentes', ata.membros_presentes)
    ata.texto = data.get('texto', ata.texto)

    db.session.commit()
    return jsonify({'message': 'Atualização feita com sucesso'}), 200

# excluir uma ata
@app.route('/atas/<int:ata_id>', methods=['DELETE'])
def delete_ata(ata_id):
    ata = Atas.query.get(ata_id)

    if ata is None:
        return jsonify({'error':'Ata não encontrada!'}), 404
    db.session.delete(ata)
    db.session.commit()
    return jsonify({'message':'Ata excluída com sucesso!'}), 200

# end Atas

# rotas para liderança

# listar toda a liderança
@app.route('/lideranca', methods=['GET'])
def get_lideranca():
    liderancas = Lideranca.query.all()

    listar_lideranca =[]
    for lideranca in liderancas:
        listar_lideranca.append({
            'id': lideranca.id,
            'presidente': lideranca.presidente,
            'vice_presidente': lideranca.vice_presidente,
            'secretario': lideranca.secretario,
            'vice_secretario': lideranca.vice_secretario,
            'tesoureiro': lideranca.tesoureiro,
            'vice_tesoureiro': lideranca.vice_tesoureiro,
            'membros_id': lideranca.membros_id 
        })
    return jsonify(listar_lideranca)  

# obter um lider pelo ID
@app.route('/lideranca/<int:lideranca_id>', methods=['GET'])
def get_lideranca_by_id(lideranca_id):
    lideranca = Lideranca.query.get(lideranca_id)

    if lideranca is None:
        return jsonify({'error':'Liderança não encontrada!'}), 404
    return jsonify({
        'id': lideranca.id,
        'presidente': lideranca.presidente,
        'vice_presidente': lideranca.vice_presidente,
        'secretario': lideranca.secretario,
        'vice_secretario': lideranca.vice_secretario,
        'tesoureiro': lideranca.tesoureiro,
        'vice_tesoureiro': lideranca.vice_tesoureiro,
        'membros_id': lideranca.membros_id     
    })

# adicionar novo lider
@app.route('/lideranca', methods=['POST'])
def create_lideranca():
    lideranca = request.json

    novo_lider = Lideranca(presidente=lideranca['presidente'],
                           vice_presidente=lideranca['vice_presidente'],
                           secretario=lideranca['secretario'],
                           vice_secretario=lideranca['vice_secretario'],
                           tesoureiro=lideranca['tesoureiro'],
                           vice_tesoureiro=lideranca['vice_tesoureiro'],
                           membros_id=lideranca['membros_id'])
    db.session.add(novo_lider)
    db.session.commit()
    return jsonify({'message':'Liderança criada com sucesso!'}), 201

# editar liderança
@app.route('/lideranca/<int:lideranca_id>', methods=['PUT'])
def update_lideranca(lideranca_id):
    lideranca = Lideranca.query.get(lideranca_id)

    if lideranca is None:
        return jsonify({'error': 'Liderança não encontrada!'}), 404

    data = request.json
    lideranca.presidente = data.get('presidente', lideranca.presidente)
    lideranca.vice_presidente = data.get('vice_presidente', lideranca.vice_presidente)
    lideranca.secretario = data.get('secretario', lideranca.secretario)
    lideranca.vice_secretario = data.get('vice_secretario', lideranca.vice_secretario)
    lideranca.tesoureiro = data.get('tesoureiro', lideranca.tesoureiro)
    lideranca.vice_tesoureiro = data.get('vice_tesoureiro', lideranca.vice_tesoureiro)
    lideranca.membros_id = data.get('membros_id', lideranca.membros_id)

    db.session.commit()
    return jsonify({'message':'Liderança atualizada com sucesso!'}), 201

#deletar liderança
@app.route('/lideranca/<int:lideranca_id>', methods=['DELETE'])
def delete_lideranca(lideranca_id):
    lideranca = Lideranca.query.get(lideranca_id)

    if lideranca is None:
        return jsonify({'error':'liderança não encontrada!'}),404
    db.session.delete(lideranca)
    db.session.commit()
    return jsonify({'message':'Liderança excluida com sucesso!'})

#rota para listar contato
@app.route('/contato', methods=['GET'])
def get_cooontato():
    contatos = Contato.query.all()

    listar_contatos = []
    for contato in contatos:
        listar_contatos.append({
            'id': contato.id,
            'nome': contato.nome,
            'email': contato.email,
            'mensagem': contato.mensagem
        })
    return jsonify(listar_contatos)  

#Obter contato pelo ID
@app.route('/contato/<int:contato_id>', methods=['GET'])
def get_contato(contato_id):
    contato = Contato.query.get(contato_id)

    if contato is None:
        return jsonify({'error':'Contato não encontrado.'}),404
    return jsonify({
        'id': contato.id,
        'nome': contato.nome,
        'email': contato.email,
        'mensagem': contato.mensagem
    })

#Criar novo contato
@app.route('/contato', methods=['POST'])
def create_contato():
    contato = request.json

    novo_contato = Contato(nome=contato['nome'],email=contato['email'],mensagem=contato['mensagem'])
    db.session.add(novo_contato)
    db.session.commit()
    return jsonify({'message':'Contato criado com sucesso!'}),201

#Editar contato
@app.route('/contato/<int:contato_id>', methods=['PUT'])
def update_contato(contato_id):
    contato = Contato.query.get(contato_id)

    if contato is None:
        return jsonify({'error':'Contato não encontrado.'}),404
    
    data = request.json
    contato.nome = data.get('nome', contato.nome)
    contato.email = data.get('email', contato.email)
    contato.mensagem = data.get('mensagem', contato.mensagem)
    db.session.commit()
    
    return jsonify({'message':'Contato atualizado com sucesso!'}), 201


#Deletar um contato
@app.route('/contato/<int:contato_id>', methods=['DELETE'])
def delete_contato(contato_id):
    contato = Contato.query.get(contato_id)

    if contato is None:
        return jsonify({'error':'Contato não encontrado'}),404
    db.session.delete(contato)
    db.session.commit()
    return jsonify({'message':'Contato deletado com sucesso!'}),201   

