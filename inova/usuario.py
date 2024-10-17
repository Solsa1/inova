from abc import ABC, abstractmethod

class Usuario(ABC):
  def __init__(self, Nome = None, NumeroMatricula = None, CPF = None, Tipo = None, EmailInstitucional = None):
    self.__Nome = Nome
    self.__NumeroMatricula = NumeroMatricula
    self.__CPF = CPF
    self.__Tipo = Tipo
    self.__EmailInstitucional = EmailInstitucional

  def setNome(self, Nome):
    self.__Nome = Nome


  def getNome(self):
    return self.__Nome


  def setNumeroMatricula(self, NumeroMatricula):
    self.__NumeroMatricula = NumeroMatricula


  def getNumeroMatricula(self):
    return self.__NumeroMatricula


  def setCPF(self, CPF):
    self.__CPF = CPF


  def getCPF(self):
    return self.__CPF


  def setTipo(self, Tipo):
    self.__Tipo = Tipo


  def getTipo(self):
    return self.__Tipo


  def setEmailInstitucional(self, EmailInstitucional):
    self.__EmailInstitucional = EmailInstitucional


  def getEmailInstitucional(self):
    return self.__EmailInstitucional


class Aluno(Usuario):
  def __init__(self,Nome = None, NumeroMatricula = None, CPF = None, Tipo = None, EmailInstitucional = None, Periodo=None, Curso=None, Coordenador=None):
    super().__init__(Nome=None, NumeroMatricula=None, CPF=None, Tipo=None, EmailInstitucional=None)
    self.__Periodo = Periodo
    self.__Curso = Curso
    self.__Coordenador = Coordenador
  def getCoordenador(self):
    return self.__Coordenador
  def setCoordenador(self, coordenador):
    self.__Coordenador = coordenador
  def getPeriodo(self):
    return self.__Periodo
  def getCurso(self):
    return self.__Curso
  def setPeriodo(self,Periodo):
    self.__Periodo = Periodo
  def setCurso(self,Curso):
    self.__Curso = Curso

     