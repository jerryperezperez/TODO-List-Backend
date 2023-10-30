# from flask import request, jsonify
# from .models import Task, db  # Asegúrate de que la importación del modelo Task esté configurada correctamente.
# from flask import Blueprint
#
# # Crea un objeto Blueprint para definir las rutas
# routes_bp = Blueprint('routes', __name__)
#
# # Ruta para crear una nueva tarea
# @routes_bp.route('/tasks', methods=['POST'])
# def create_task():
#     data = request.get_json()
#     new_task = Task(name=data['name'], description=data['description'])
#     db.session.add(new_task)  # Asegúrate de que db esté definido y configurado para SQLAlchemy.
#     db.session.commit()
#     return jsonify({'message': 'Task created successfully'})
#
# # Ruta para obtener todas las tareas
# @routes_bp.route('/getTasks', methods=['GET'])
# def get_all_tasks():
#     # Consulta todas las tareas en la base de datos
#     tasks = Task.query.all()  # Asegúrate de que Task tenga un modelo SQLAlchemy.
#
#     # Convierte las tareas en un formato JSON y responde
#     task_list = [{'id': task.id, 'name': task.name, 'description': task.description, 'completed': task.completed} for task in tasks]
#     return jsonify({'tasks': task_list})

