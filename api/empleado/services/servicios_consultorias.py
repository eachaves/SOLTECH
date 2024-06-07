from api.consultoria.services.servicios_consultoria import update_fecha_fin

def mark_as_done(id):
    try:
        update_fecha_fin(id)
    except Exception as e:
        raise Exception(e.args[0], e.args[1])