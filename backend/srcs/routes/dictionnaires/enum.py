from imports.extern import *

class OwnerShipRights(enum.Enum):
    blocked = "blocked"
    read = "read"
    view = "view"
    write = "write"
    all = "all"

rights_level = {
    "blocked": 0,
    "view": 1,
    "read": 2,
    "write": 3,
    "all": 4,
}
