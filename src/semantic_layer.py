import yaml

def load_semantic_layer():
    with open("semantic/metrics.yaml", "r") as file:
        return yaml.safe_load(file)

def get_metric(metric_name):
    semantic_layer = load_semantic_layer()
    return semantic_layer["metrics"].get(metric_name) 

def get_dimension(dimension_name):
    semantic_layer = load_semantic_layer()
    return semantic_layer["metrics"]["dimensions"].get(dimension_name)