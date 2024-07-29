from flask import json


def transform_objects_to_json(objects, **kwargs):
    def transform_object(obj):
        return {key: getattr(obj, attr) for key, attr in kwargs.items()}
    
    # Aplica a transformação a cada objeto e converte para JSON
    objects_dict = [transform_object(obj) for obj in objects]
    
    return json.dumps(objects_dict, ensure_ascii=False, indent=4)