from datetime                   import datetime
from src.model.street           import street
from src.model.city             import city
from src.model.neighborhood     import neighborhood
from src.model._state_province  import _state_province
from src.model.country          import country


class Adress:
  _id: int
  _street: str
  _city: str
  _neighborhood: str
  _state_province: str
  _country: str
  _createdAt: datetime
  _updatedAt: datetime 

  def __init__(self):
    self._id = None
    self._street: str = street
    self._city: str = city
    self._neighborhood: str = neighborhood
    self._state_province: str = state_province
    self.country: str = country
    self._createdAt = datetime.now()
    self._updatedAt = datetime.now()

  def get_id(self):
    return self._id

  def set_id(self, value: int):
    self._id = value

  def get_street(self):
    return self._street

  def set_street(self, value: str):
    self._street = value

  def get_city(self):
    return self._city

  def set_city(self, value: str):
    self._city = value

  def get_neighborhood(self):
    return self._neighborhood

  def set_neighborhood(self, value: str):
    self._neighborhood = value

  def get_state_province(self):
    return self._state_province

  def set_state_province(self, value: str):
    self._state_province = value

  def get_country(self):
    return self._country

  def set_country(self, value: str):
    self._country = value

  def set_updatedAt(self, value: datetime):
    self._updatedAt = value

  def get_updatedAt(self):
    return self._updatedAt

  def get_createdAt(self):
    return self._createdAt

  def set_createdAt(self, value: datetime):
    self._createdAt = value

  def __hash__(self):
    return hash((self._id, self._street, self._city, self._neighborhood, self._state_province, self._country))

  def __eq__(self, other):
    if not isinstance(other, Adress):
      return False
    return (self._id == other.get_id() and self._street == other.get_street() and self._city == other.get_city() and 
            self._neighborhood == other.get_neighborhood() and self._state_province == other.get_state_province() and 
            self._country == other.get_country())

  def __str__(self):
    return (f"Contact(id={self._id}, street={self._street}, city={self._city}, neighborhood={self._neighborhood}, state_province={self._state_province}, country={self._country} "
            f"createdAt={self._createdAt}, updatedAt={self._updatedAt})")

  @classmethod
  def addressBuilder(cls):  
    return cls.AdressBuilder() 

class ContactBuilder:
  def __init__(self):
    self._user = Adress() 

  def id(self, value: int):
    self._user.set_id(value)
    return self
