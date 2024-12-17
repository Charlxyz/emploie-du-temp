from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Création de la base de données
Base = declarative_base()

# Modèle pour les salles
class Salle(Base):
    __tablename__ = 'salles'
    id = Column(Integer, primary_key=True)
    nom = Column(String, unique=True, nullable=False)

# Modèle pour les professeurs
class Professeur(Base):
    __tablename__ = 'professeurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    matiere = Column(String, nullable=False)

# Modèle pour les classes
class Classe(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    nom = Column(String, unique=True, nullable=False)
    niveau = Column(Integer, nullable=False)

# Modèle pour les étudiants
class Etudiant(Base):
    __tablename__ = 'etudiants'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    classe_id = Column(Integer, ForeignKey('classes.id'), nullable=False)
    classe = relationship("Classe", back_populates="etudiants")

# Ajout de la relation dans Classe
Classe.etudiants = relationship("Etudiant", back_populates="classe", cascade="all, delete-orphan")

# Modèle pour les horaires
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

# Création de la base de données
engine = create_engine('sqlite:///database//planning.db', echo=True)
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()
