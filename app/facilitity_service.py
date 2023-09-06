from connect import Session
from models import Facility


class FacilityService:
    @classmethod
    def get_facility_by_id(cls, id):
        session = Session()
        facility = session.query(Facility).filter_by(id=id).first()
        session.close()
        return facility

    @classmethod
    def get_all_facilities(cls):
        session = Session()
        all_facilities = session.query(Facility).all()
        session.close
        return all_facilities

    @classmethod
    def create_facility(cls, name):
        facility = Facility(name=name)
        session = Session()
        session.add(facility)
        session.commit()
        session.close

    @classmethod
    def update_facility(cls, id, new_name):
        session = Session()
        facility = session.query(Facility).filter_by(id=id).first()
        facility.name = new_name
        session.commit()
        session.close

    @classmethod
    def delete_facility(cls, id):
        session = Session()
        facility = session.query(Facility).filter_by(id=id).first()
        session.delete(facility)
        session.commit()
        session.close

    @classmethod
    def get_all_facility_dogs(cls, id):
        session = Session()
        facility = session.query(Facility).filter_by(id=id).first()
        dogs = facility.get_facility_dogs()
        return dogs

    @classmethod
    def get_facility_adopters(cls, id):
        session = Session()
        facility = session.query(Facility).filter_by(id=id).first()
        adopters = facility.get_adopters()
        return adopters
