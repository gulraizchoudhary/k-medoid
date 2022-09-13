"""
implementation of K-Medoids with pre-compute pairwise distance
"""
import numpy as np

def cluster(data, number_of_cluster, pair_wise_distances, initial_medoids_idx):
    data_size = data.shape[0]
    
    if number_of_cluster > data_size:
        raise Exception('Number of medoids is more than data size')

    if initial_medoids_idx.shape[0] == 0:
        # Select ramdom indices for initial representation object == number_of_medoids
        medoids_row_index_init = np.random.choice(data_size, number_of_cluster, replace=False)
    else:
        medoids_row_index_init = initial_medoids_idx
    
    labels = _get_labels(data, data_size, number_of_cluster, medoids_row_index_init, pair_wise_distances)

    # Find new medoids from the clusters until medoids do not change any more
    medoids_row_index_prev = medoids_row_index_init
    medoids_row_index_current = np.full(number_of_cluster, -1)

    while not np.array_equal(medoids_row_index_prev, medoids_row_index_current):
        # If they are not the same CURRENT becomes PREV
        medoids_row_index_prev = np.copy(medoids_row_index_current)

        # Find new current
        for i in range(number_of_cluster):
            # Get index where value is equal to i
            # .where returns tuple so we need [0] here
            indices = np.where(labels == i)[0]
            
            if len(indices) == 0:
                # empty cluster
                medoids_row_index_current[i] = np.random.randint(0, data_size)
            else:
                # Find new medoids
                # Get pair distance for the indices
                clusters_pair_distance_arr = pair_wise_distances[np.ix_(indices, indices)]
    
                # find the index of minimum mean row
                min_mean_index = np.argmin(np.mean(clusters_pair_distance_arr,axis=1))
                medoids_row_index_current[i] = indices[min_mean_index]

        # We have new medoids
        # Get new clusters
        labels = _get_labels(data, data_size, number_of_cluster, medoids_row_index_current, pair_wise_distances)
     
    return (labels, medoids_row_index_current)

def _get_labels(input_arr, data_size, medoids_number, medoids_row_idx, pair_wise_distances):
    # Get distance to medoids
    distance_arr = np.zeros((data_size, medoids_number))

    for i in range(data_size):
        for j in range(medoids_number):
            distance_arr[i, j] = pair_wise_distances[i, medoids_row_idx[j]]

    # argmin return the minimum on each row
    # we can see it as cluster the node is allocated in
    return np.argmin(distance_arr, axis=1)
