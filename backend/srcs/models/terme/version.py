from imports.services import *
from difflib import unified_diff

class Version(Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String())
    # genre = db.Column(db.String())
    type = db.Column(db.String())
    language = db.Column(db.String())

    content = db.Column(db.Text, nullable=False)
    version = db.Column(db.Integer, nullable=False)

    terme = db.relationship('Terme', backref=db.backref('versions', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    

    @classmethod
    def new(cls, terme):

        last_version = Version.query.filter_by(terme_id=terme.id).order_by(Version.version.desc()).first()
        version = 1 if not last_version else last_version.version + 1

        # Optional: store as diff
        if last_version:
            diff = "\n".join(unified_diff(
                last_version.content.splitlines(),
                terme.content.splitlines(),
                lineterm=""
            ))
            content_to_store = diff
        else:
            content_to_store = terme.content

        new_version = Version(
            name=terme.name,
            # genre=terme.genre,
            type=terme.type,
            language=terme.language,
            content=content_to_store,
            version=version,
            terme_id=terme.id
        )
        db.session.add(new_version)
        db.session.commit()



# class ContentType(enum.Enum):
#     definitions = "definitions"
#     exemples = "exemples"
#     note = "note"
#     origine = "origine"
