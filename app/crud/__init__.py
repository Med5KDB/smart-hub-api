from .client import create, deleteOne, findOne, updateOne, findAll
from .employee import create as createEmployee, deleteOne as deleteEmployee, findOne as findEmployee, updateOne as updateEmployee, findAll as findAllEmployee

__all__ = ["create", "deleteOne", "findOne", "updateOne", "findAll", "createEmployee", "deleteEmployee", "findEmployee", "updateEmployee", "findAllEmployee"]