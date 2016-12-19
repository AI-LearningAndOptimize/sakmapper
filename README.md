sakmapper
=======

Implementation of Mapper Algorithm

**Background**

Mapper is an algorithm in the sub-genre of exploratory data analysis known as topological data analysis (TDA). Competing open-source implementations include Python Mapper, TDAmapper, and KeplerMapper, while Ayasdi offers a commercial solution.

**Python Dependencies**

sakmapper has been developed for python 2.7.x

- numpy
- scipy
- pandas
- scikit-learn
- networkx

**Usage**

The core functions of sakmapper are meant to be imported from the module into your python namespace, e.g.

```
from sakmapper import apply_lens, mapper_graph
```

A data set of dimension N rows x F features will first be passed through a lens function to yield an N x 2 projection. Next, a mapper graph can be constructed by specifying the set covering of the lensed data, as well as the clustering approach. Because calculating the projection of the initial data set under the lens function is expensive, we encourage this computation upfront and invoking the mapper_graph routine with the lens_data keyword argument. Other keyword arguments of the mapper_graph routine pertain to the set covering (equalize, resolution, gain) or the clustering approach (clust, maxK, stat).

The default optimal clustering heuristic (stat='db') is the Davies-Bouldin index, an easily computed quantity. Switching to the gap statistic (stat='gap') of Tibshirani, Walther, and Hastie incurs greater computational overhead, but in our limited experience can produce better resolved mapper graphs.

**Notes**

Status: Active Development
