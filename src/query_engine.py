from src.semantic_layer import get_metric, get_dimension


def find_metric(metric_name):
    return get_metric(metric_name)


def find_dimension(dimension_name):
    return get_dimension(dimension_name)


def list_metrics():
    from src.semantic_layer import load_semantic_layer
    semantic_layer = load_semantic_layer()
    return list(semantic_layer["metrics"].keys())


def list_dimensions():
    from src.semantic_layer import load_semantic_layer
    semantic_layer = load_semantic_layer()
    return list(semantic_layer["dimensions"].keys())