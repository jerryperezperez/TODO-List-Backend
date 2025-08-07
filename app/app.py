from flask import Flask, jsonify, request
from models import db, Task
from flask_cors import CORS  # Importa Flask-CORS

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    CORS(app)  # Configura CORS en tu aplicación
    # Configura la aplicación para usar SQLAlchemy
    db.init_app(app)

    # Crea las tablas en la base de datos
    with app.app_context():
        db.create_all()

    #Rutas

    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({'status': 'Server is running'}), 200

    @app.route('/tasks', methods=['GET'])
    def get_all_tasks():
        # Consulta todas las tareas en la base de datos
        tasks = Task.query.all()  # Asegúrate de que Task tenga un modelo SQLAlchemy.

        # Convierte las tareas en un formato JSON y responde
        task_list = [{'id': task.id, 'name': task.name, 'description': task.description,'category': task.category, 'completed': task.completed} for task in tasks]
        return task_list

    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        new_task = Task(name=data['name'], description=data['description'], category=data['category'])
        db.session.add(new_task)  # Asegúrate de que db esté definido y configurado para SQLAlchemy.
        db.session.commit()
        return jsonify({'message': 'Task created successfully'})

    @app.route('/tasks', methods=['POST'])
    def delete(self, task_id):
        task = Task.query.get(task_id)  # Busca la tarea por su ID en la base de datos
        if not task:
            return {'message': 'Tarea no encontrada'}, 404  # 404 significa Not Found
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Tarea eliminada exitosamente'}

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        print("entra en delete")
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'message': 'Tarea no encontrada'}), 404
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Tarea eliminada exitosamente'})

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        # Busca la tarea por su ID en la base de datos
        print("entra en update")
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'message': 'Tarea no encontrada'}), 404  # 404 significa Not Found

        # Obtiene los datos actualizados de la solicitud JSON
        data = request.get_json()
        print(data)
        # Actualiza los atributos de la tarea con los datos recibidos
        task.name = data.get('name', task.name)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)

        # Guarda los cambios en la base de datos
        db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
