#!/usr/bin/env python3
from app.services.facilitity_service import FacilityService

if __name__ == "__main__":
    print(FacilityService.get_all_facilities())
