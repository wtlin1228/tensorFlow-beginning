import math
def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    batches = []

    for i in range(0, len(features), batch_size):
        end_pos = i + batch_size
        batch = features[i:end_pos], labels[i:end_pos]
        batches.append(batch)
        
    return batches

