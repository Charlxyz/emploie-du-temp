from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Salle(Base):
    __tablename__ = 'salles'
    id = Column(Integer, primary_key=True)
    nom = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Salle(id={self.id}, nom='{self.nom}')>"

class Professeur(Base):
    __tablename__ = 'professeurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    matiere = Column(String, nullable=False)

    def __repr__(self):
        return f"<Professeur(id={self.id}, nom='{self.nom}', prenom='{self.prenom}', matiere='{self.matiere}')>"

class Classe(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    nom = Column(String, unique=True, nullable=False)
    niveau = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Classe(id={self.id}, nom='{self.nom}', niveau={self.niveau})>"

class Etudiant(Base):
    __tablename__ = 'etudiants'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    classe_id = Column(Integer, ForeignKey('classes.id'), nullable=False)

    classe = relationship("Classe", back_populates="etudiants")

    def __repr__(self):
        return f"<Etudiant(id={self.id}, nom='{self.nom}', prenom='{self.prenom}', age={self.age}, classe_id={self.classe_id})>"

Classe.etudiants = relationship("Etudiant", order_by=Etudiant.id, back_populates="classe", cascade="all, delete-orphan")

class Horaire(Base):
    __tablename__ = 'horaires'
    id = Column(Integer, primary_key=True)
    professeur_id = Column(Integer, ForeignKey('professeurs.id'), nullable=False)
    classe_id = Column(Integer, ForeignKey('classes.id'), nullable=False)
    salle_id = Column(Integer, ForeignKey('salles.id'), nullable=False)
    horaire = Column(String, nullable=False)

    professeur = relationship("Professeur")
    classe = relationship("Classe")
    salle = relationship("Salle")

    def __repr__(self):
        return (f"<Horaire(id={self.id}, professeur_id={self.professeur_id}, classe_id={self.classe_id}, "
                f"salle_id={self.salle_id}, horaire='{self.horaire}')>")

def createBDD():
    engine = create_engine('sqlite:///database/planning.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
