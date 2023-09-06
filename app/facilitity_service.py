from connect import Session
from models import Facility


class FacilityService:
    @classmethod
    def get_all_facilities(cls):
        session = Session()
        all_facilities = session.query(Facility).all()
        session.close
        return all_facilities
