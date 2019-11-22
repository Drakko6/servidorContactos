from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'alumno',
    password = '12345',
    database = 'contactos'
)

cursor = bd.cursor()

@app.route('/contactos/', methods=["GET", "POST"])
def contactos():
    if request.method == 'GET':
        contactos = []
        query = "SELECT * FROM contacto"
        cursor.execute(query)

        for contacto in cursor.fetchall():
            d = {
                'nombre': contacto[1],
                'correo': contacto[2],
                'telefono': contacto[3],
                'facebook': contacto[4],
                'twitter':  contacto[5],
                'instagram':  contacto[6],
                'avatar': contacto[7]
            }
            contactos.append(d)
            print(contacto)

        return jsonify(contactos)
    else:
        data = request.get_json()
        print(data)

        query = "INSERT INTO contacto(nombre, correo, telefono, facebook, twitter, instagram, avatar)  VALUES "\
        "(%s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(query, (data['nombre'],
                              data['correo'],
                              data['telefono'],
                                data['facebook'],
                                data['twitter'],
                                data['instagram'],
                               data['avatar']
                               ))
        bd.commit()

        if cursor.rowcount:
            return jsonify({'data': 'Ok'})
        else:
            return jsonify({'data': 'Error'})

app.run(debug=True)