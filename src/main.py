from .entities.entity import Session, engine, Base
from .entities.exam import Exam

# Generamos el esquema de base de datos

Base.metadata.create_all(engine)


# Iniciar sesion

session = Session()


# Verificamos si hay algun dato en la tabla que especifiquemos

exams = session.query(Exam).all()


if len(exams) == 0:
    record =  Exam('Titulo de prueba', 'Descripcion de prueba', 'Creado por la funcion inicial creada por Adrian')
    
    session.add(record)
    session.commit()
    session.close()
    
    exams = session.query(Exam).all()
    
print('## Datos de Exams')

for exam in exams:
    print(f'({exam.id}) - {exam.title} - {exam.description}')