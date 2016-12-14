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

A data set of dimension N rows x F features will first be passed through a lens function to yield an N x 2 projection. Next, a mapper graph can be constructed by specifying the set covering of the lensed data, as well as the clustering approach.

**Notes**

Status: Active Development
