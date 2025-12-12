from imports.extern import *

class RelationshipTypes(enum.Enum):
    blocked = "blocked"
    unfollow = "unfollow"
    follow = "follow"
    