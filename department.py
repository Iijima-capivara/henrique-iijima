from datetime               import datetime
from src.model.name         import name
from src.model.admin        import admin
from src.model.roles        import Role 
from src.model.company      import Company

class Department:
    def __init__(self):
        self._id = None
        self._name = name
        self._admin = admin
        self._roles = [roles]
        self._company = company
        self._created_at = datetime.now()
        self._updated_at = datetime.now()

    def get_id(self):
        return self._id

    def set_id(self, value: int):
        self._id = value

    def get_number(self):
        return self._name

    def set_number(self, value: str):
        self._name = value

    def get_type(self):
        return self._admin

    def set_type(self, value: str):
        self._admin = value

    def get_main(self):
        return self._roles

    def set_main(self, value: bool):
        self._roles = value

    def get_main(self):
        return self._company

    def set_main(self, value: bool):
        self._company = value

    def get_createdAt(self):
        return self._createdAt

    def set_createdAt(self, value: datetime):
        self._createdAt = value

    def get_updatedAt(self):
        return self._updatedAt

    def set_updatedAt(self, value: datetime):
        self._updatedAt = value

    def __hash__(self):
        return hash((self._id, self._name, self._admin, self._roles, self._company))

    def __eq__(self, other):
        if not isinstance(other, Department):
            return False
        return self._id == other._id and self._name == other._name and self._admin == other._admin and self._role == other._role and self._company == other._company

    def __str__(self):
        return (f"Phone(id={self._id}, name={self._name}, admin={self._admin}, "
                f"role={self._role}, company={self._company} created_at={self._created_at}, updated_at={self._updated_at})")
    
    @classmethod
    def builder(cls):
        return cls.DepartmentBuilder()

    class DepartmentBuilder:
        def __init__(self):
            self._department = Department()

        def id(self, value):
            self._department.id = value
            return self

        def build(self):
            return self._department