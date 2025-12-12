from faker import Faker
from imports.all import *
from hashlib import sha256
import random


fake = Faker()


def faux_dictionnaire(dic_id, n=50):
    termes = []
    for i in range(n):
        t = Terme(name=fake.word(),
                content="fake$@@@$" + fake.sentence(),
                type=random.choice([e.value for e in TermeTypes]),
                language=fake.language_name(),
                context=random.choice([e.value for e in TermeContext]),
              )
        db.session.add(t)    
        termes.append(t)
        db.session.commit()
    for t in termes:
        auth = Author(
            terme_id=t.id,
            user_id=1,
              )
        dict = DictionnaireTerme(
            terme_id=t.id,
            dictionnaire_id=dic_id,
              )
        db.session.add(auth)  
        db.session.add(dict)    
        db.session.commit()


def fake_db():
   
    d = Dictionnaire.query.filter_by(name="fake dictionnaire").first()
    if d:
        return
    d = Dictionnaire(
        name="fake dictionnaire",
        description="this is just a fake dictionnaire",
        visibility="public",
        suggestions=True,
    )
    db.session.add(d)
    db.session.commit()
    
    owner = Ownership(
        user_id=1,
        dictionnaire_id=d.id,
        rights="all"
    )
    db.session.add(owner)
    db.session.commit()
    
    faux_dictionnaire(d.id, 100)
    
from imports.all import *

def fake_users():
    fake_user = User.get_or_create(username="fake_user", password="123")
    fake_friend = User.get_or_create(username="fake_friend", password="123")
    fake_follower = User.get_or_create(username="fake_follower", password="123")
    fake_following = User.get_or_create(username="fake_following", password="123")
    fake_blocked = User.get_or_create(username="fake_blocked", password="123")
    fake_blocked_by = User.get_or_create(username="fake_blocked_by", password="123")
    
    Relationship.get_or_create(user_id=fake_user.id, target_id=fake_friend.id, type="follow")
    Relationship.get_or_create(user_id=fake_friend.id, target_id=fake_user.id, type="follow")
    Relationship.get_or_create(user_id=fake_follower.id, target_id=fake_user.id, type="follow")
    Relationship.get_or_create(user_id=fake_user.id, target_id=fake_following.id, type="follow")
    Relationship.get_or_create(user_id=fake_user.id, target_id=fake_blocked.id, type="blocked")
    Relationship.get_or_create(user_id=fake_blocked_by.id, target_id=fake_user.id, type="blocked")
    
    fake_view_dictionnaire = Dictionnaire.get_or_create(name="fake_view_dictionnaire", description="this is a fake view dictionnaire", visibility="public")
    fake_read_dictionnaire = Dictionnaire.get_or_create(name="fake_read_dictionnaire", description="this is a fake reading dictionnaire", visibility="public")
    fake_write_dictionnaire = Dictionnaire.get_or_create(name="fake_write_dictionnaire", description="this is a fake writing dictionnaire", visibility="public")
    fake_all_dictionnaire = Dictionnaire.get_or_create(name="fake_all_dictionnaire", description="this is a fake all rights dictionnaire", visibility="public")

    Ownership.get_or_create(dictionnaire_id=fake_view_dictionnaire.id, rights="view", user_id=fake_user.id)
    Ownership.get_or_create(dictionnaire_id=fake_read_dictionnaire.id, rights="read", user_id=fake_user.id)
    Ownership.get_or_create(dictionnaire_id=fake_write_dictionnaire.id, rights="write", user_id=fake_user.id)
    Ownership.get_or_create(dictionnaire_id=fake_all_dictionnaire.id, rights="all", user_id=fake_user.id)
    
def delete_fake_termes():
    termes = Terme.query.filter(Terme.content.startswith("fake$@@@$")).all()
    print(len(termes))
    for t in termes:
        Author.query.filter_by(terme_id=t.id).delete()
        DictionnaireTerme.query.filter_by(terme_id=t.id).delete()
        db.session.delete(t)
    db.session.commit()

def erase_links_dic8():
    for i in range(2, 10):
        DictionnaireTerme.query.filter_by(dictionnaire_id=8).delete()
        Author.query.filter_by(dictionnaire_id=8).delete()
    db.session.commit()

def erase_fake_db():
    d = Dictionnaire.query.filter_by(name="fake dictionnaire").first()
    delete_fake_termes()
    if not d:
        return

    # Delete all related terme links, authors, and terms
    links = DictionnaireTerme.query.filter_by(dictionnaire_id=d.id).all()
    for link in links:
        terme = Terme.query.get(link.terme_id)

        Author.query.filter_by(terme_id=terme.id).delete()
        DictionnaireTerme.query.filter_by(terme_id=terme.id).delete()
        db.session.delete(terme)
    
    termes = Terme.query.filter_by()

    # Delete ownership
    Ownership.query.filter_by(dictionnaire_id=d.id).delete()

    # Delete the dictionnaire
    db.session.delete(d)
    db.session.commit()
