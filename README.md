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

## Example: Histograms of most frequent diseases in a cluster
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_0_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_1_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_2_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_3_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_4_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_5_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_6_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_7_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_8_histogram.png)
!["Cluster 0"](https://github.com/gulraizchoudhary/k-medoid/blob/main/k-medoids/visuals/toydata_mlcss_9_histogram.png)
