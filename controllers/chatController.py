#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtenemos configuracion del archivo __init__.py
from . import *


class UserStatus(Resource):
    # Ruta para cambiar tu estado de conexion
    def put(self, username):
        # Declaramos la lista de valores posibles
        status_list = config['STATUS_OPTIONS']

        # Capturamos la peticion
        data = request.get_json()
        # Capturamos el nuevo status
        new_status = data["status"]
        # Creamos el query para el nuevo status
        newValue = {"$set": data}
        # Obtenemos el usuario a modificar
        current_user = connection.showItem(username)

        # Validamos que la opcion este dentro de lo permitido
        if new_status in status_list:
            # Si el status es conectado, se actualiza,
            # pero sin responder ultima conexion
            if new_status == 'Conectado':
                connection.updateItem(current_user, newValue)
                return {
                    'status': new_status,
                    "success": "true"}, 200
            # Si es otro tipo, respondera con la hora
            # de la ultima conexion
            else:
                # Actualizamos status
                connection.updateItem(current_user, newValue)

                # Creamos nuevo query de ultima vez conectado
                lastConnection = {"lastConnection": f'{last_connection}'}
                newValue = {"$set": lastConnection}

                # Actualizamos lastConnection
                connection.updateItem(current_user, newValue)
                return {
                    'status': new_status,
                    'connection': f'Última conexión: {last_connection}',
                    "success": "true"}, 200
        else:
            return {
                'message': 'Elija una opción correcta',
                'success': 'false'}, 400