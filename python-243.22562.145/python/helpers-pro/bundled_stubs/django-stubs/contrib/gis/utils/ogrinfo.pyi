from django.contrib.gis.gdal import DataSource

def ogrinfo(data_source: str | DataSource, num_features: int = ...) -> None: ...
