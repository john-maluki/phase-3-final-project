from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, backref
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Facility(Base):
    __tablename__ = "facilities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    dogs = relationship("Dog", backref=backref("facility"))

    def __repr__(self):
        return "Facility<{0}>".format(self.name)


class Adopter(Base):
    __tablename__ = "adopters"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    dogs = relationship("Dog", backref=backref("adopter"))

    def __repr__(self):
        return "Facility<{0} {1}>".format(self.first_name, self.last_name)


class Dog(Base):
    __tablename__ = "dogs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    facility_id: Mapped[int] = mapped_column(ForeignKey(Facility.id), nullable=False)
    adopter_id: Mapped[int] = mapped_column(ForeignKey(Adopter.id))
