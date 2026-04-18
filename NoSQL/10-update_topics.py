#!/usr/bin/env python3
"""Update school topics."""


def update_topics(mongo_collection, name, topics):
    """
    Cambia todos los temas de un documento de escuela basado en el nombre.

    Args:
        mongo_collection: Objeto de colección de pymongo.
        name (string): El nombre de la escuela a buscar.
        topics (list of strings): La lista de temas a establecer.

    Returns:
        Nada.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )


if __name__ == "__main__":
    # El código no se ejecuta al ser importado
    pass