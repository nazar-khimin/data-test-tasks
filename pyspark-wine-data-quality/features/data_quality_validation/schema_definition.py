WINE_QUALITY_TYPE_SCHEMA: dict[str, str] = {
    "fixed acidity": "float",
    "volatile acidity": "float",
    "citric acid": "float",
    "residual sugar": "float",
    "chlorides": "float",
    "free sulfur dioxide": "float",
    "total sulfur dioxide": "float",
    "density": "float",
    "pH": "float",
    "sulphates": "float",
    "alcohol": "float",
    "quality": "float",
    "Id": "float"
}

WINE_QUALITY_RANGE_SCHEMA: dict[str, tuple[float, float]] = {
    "fixed acidity": (3.0, 15.0),
    "volatile acidity": (0.1, 1.6),
    "citric acid": (0.0, 1.5),
    "residual sugar": (0.6, 65.8),
    "chlorides": (0.01, 0.2),
    "free sulfur dioxide": (1, 289),
    "total sulfur dioxide": (6, 440),
    "density": (0.98, 1.005),
    "pH": (2.7, 4.0),
    "sulphates": (0.3, 2.0),
    "alcohol": (8.0, 15.5),
    "quality": (3, 9)
}
