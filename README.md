# _k_-medoid
Cluster patients’ diagnosis using different set and sequence similarity measures, identify correct number of clusters, optimal clustering solution, and analyze the clustering results.
Many distance matrices are used and are listed as follows.

#Set similarity measures
```bash
Jaccard Similarity(num_intersect / (len_x + len_y - num_intersect))
Overlap Similarity (num_intersect / min(len_x, len_y))
Bram Similarity num_intersect/max(len_x, len_y)
Dice Similarity (2*num_intersect)/(len_x+len_y)
```

#Sequence similarity
```bash
LCSS 
bram num_intersect/max(len_x, len_y)
MetricLCSS lcss.lcss(x,y)/max(len_x, len_y)
```

#Hybrid: Set+Sequence similarity
```bash
OverlappLcss (p*lcss)+(q*overlap)
S3m (p*lcss)+(q*jaccard)
smc (num_intersect/(len_x+len_y))
tss ((p*overlap) + (q*overlapLcss))
Monge-Elkan similarity measure: The Monge-Elkan similarity measure is a type of hybrid similarity measure that combines the benefits of sequence-based and set-based methods. 
```


#distance Score
```bash
Bram distance socre (1 - bram similarity)
dice distance socre (1 - dice similarity)
TfIdf (1-(Monge-Elkan similarity measure/min(x,y)))

```

