from imports.extern import *
    
class TermeTypes(enum.Enum):
    nom_commun = "nom_commun"
    nom_commun_masculin = "nom_commun_masculin"
    nom_commun_feminin = "nom_commun_feminin"
    nom_propre = "nom_propre"
    nom_propre_masculin = "nom_propre_masculin"
    nom_propre_feminin = "nom_propre_feminin"
    groupe_de_mot = "groupe_de_mot"
    adjectif = "adjectif"
    verbe = "verbe"
    adverbe = "adverbe"
    maxime = "maxime"
    poesie = "poesie"
    nouvelle = "nouvelle"
    roman = "roman"
    discution = "discution"
    
class TermeGenre(enum.Enum):
    masculin = "masculin"
    feminin = "feminin"
    invariable = "invariable"

class TermeContext(enum.Enum):
    grossier = "grossier"
    familier = "familier"
    neutre = "neutre"
    soutenue = "soutenue"
    ancien = "ancien"
    