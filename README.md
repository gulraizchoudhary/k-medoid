# _k_-medoid
Cluster patients’ diagnosis using different set and sequence similarity measures, identify correct number of clusters, optimal clustering solution, and analyze the clustering results.
Many distance matrices are used and are listed as follows.

## Set similarity measures
```bash
Jaccard Similarity(num_intersect / (len_x + len_y - num_intersect))
Overlap Similarity (num_intersect / min(len_x, len_y))
Bram Similarity num_intersect/max(len_x, len_y)
Dice Similarity (2*num_intersect)/(len_x+len_y)
```

## Sequence similarity
```bash
LCSS 
bram num_intersect/max(len_x, len_y)
MetricLCSS lcss.lcss(x,y)/max(len_x, len_y)
```

## Hybrid: Set+Sequence similarity
```bash
OverlappLcss (p*lcss)+(q*overlap)
S3m (p*lcss)+(q*jaccard)
smc (num_intersect/(len_x+len_y))
tss ((p*overlap) + (q*overlapLcss))
Monge-Elkan similarity measure: The Monge-Elkan similarity measure is a type of hybrid similarity measure that combines the benefits of sequence-based and set-based methods. 
```


## Distance Score
```bash
Bram distance socre (1 - bram similarity)
dice distance socre (1 - dice similarity)
TfIdf (1-(Monge-Elkan similarity measure/min(x,y)))
Overlap distance score (1-overlap similarity)
Jaccard distance score (1-jaccard similarity)
```

## Example: Histograms of most frequent diseases in a cluster (mLCSS sequence similarity measure)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_0_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_1_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_2_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_3_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_4_histogram.png)
## Example: Histograms of most frequent diseases in a cluster (Overlap similarity measure)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_in_cluster_0_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_in_cluster_1_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_in_cluster_2_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_in_cluster_3_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_in_cluster_4_histogram.png)


## Example: Diseae trajectories with cluster representatives (medoid) using mLCSS sequence similarity measure
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_0.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_1.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_2.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_3.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_4.png)

## Example: Diseae trajectories with cluster representatives (medoid) using Overlap similarity measure
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_0.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_1.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_2.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_3.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_overlap_4.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)