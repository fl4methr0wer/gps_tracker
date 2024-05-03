from GPS.Location import Location
from typing import List
class LocationDAO:
    def create(self, location: Location) -> None:
        pass

    def read(self, location_id: int) -> Location:
        pass

    def update(self, location_id: int, new_location: Location) -> None:
        pass

    def delete(self, location_id: int) -> None:
        pass

    def read_all(self) -> List[Location]:
        pass
