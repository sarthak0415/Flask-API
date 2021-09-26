from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature


def verify_location(point, polygon):

    point = Point(point)
    polygon = Polygon(polygon['coordinates'])

    point = Feature(geometry=point)
    polygon = Feature(geometry=polygon)

    return boolean_point_in_polygon(point, polygon)
