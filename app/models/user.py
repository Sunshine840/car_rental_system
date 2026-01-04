from enum import Enum


class Role(Enum):  # Enums can be extended further
    USER = "User"
    ADMIN = "Admin"
    SUPERADMIN = "SuperAdmin"


class User:  # Parent class
    def __init__(
        self,
        id,
        fname,
        lname,
        email_id,
        password,
        phone_number,
        created_at,
        updated_at,
        role: Role = Role.USER,
        is_active=True,
    ):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email_id = email_id
        self.password = password
        self.phone_number = phone_number
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
