from .client import create, deleteOne, findOne, updateOne
from .employee import create as createEmployee, deleteOne as deleteEmployee, findOne as findEmployee, updateOne as updateEmployee

__all__ = ["create", "deleteOne", "findOne", "updateOne", "createEmployee", "deleteEmployee", "findEmployee", "updateEmployee"]