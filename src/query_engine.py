from src.semantic_layer import get_metric, get_dimension

def find_metric(metric_name):
    return get_metric(metric_name)

def find_dimension(dimension_name):
    return get_dimension(dimension_name)