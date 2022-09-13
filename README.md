# _k_-medoid
Cluster patients’ diagnosis using different set and sequence similarity measures, identify correct number of clusters, optimal clustering solution, and analyze the clustering results.
Many distance matrices are used and are listed as follows.
##Set similarity measures
```bash
Jaccard Similarity 
Overlap Similarity
Bram Similarity
Dice Similarity (2*num_intersect)/(len_x+len_y)
Monge-Elkan similarity measure
```

##Sequence similarity
```bash
LCSS
Pairwise
bram num_intersect/max(len_x, len_y)
MetricLCSS lcss.lcss(x,y)/max(len_x, len_y)
```

##Hybrid: Set+Sequence similarity
```bash
OverlappLcss (p*lcss)+(q*overlap)
S3m (p*lcss)+(q*jaccard)
smc (num_intersect/(len_x+len_y))
tss ((p*overlap) + (q*overlapLcss))
```


##Sequence similarity
```bash
Bram distance socre (1 - bram similarity)
dice distance socre (1 - dice similarity)
TfIdf (1-(Monge-Elkan similarity measure/min(x,y)))

```

