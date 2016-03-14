def davies_bouldin(dist_mu, sigma):
    DB = 0
    K = len(sigma)
    for i in range(K):
        D_i = 0
        for j in range(K):
            if j == i:
                continue
            R_ij = (sigma[i] + sigma[j]) / dist_mu[i,j]
            if R_ij > D_i:
                D_i = R_ij
        DB += D_i
    return DB / K


def optimal_kmeans_clustering(df, points_highlighted):
    clustering = {}
    db_index = []
    X = df.ix[points_highlighted,:]
    for k in range(1, 6):
        kmeans = cluster.KMeans(n_clusters=k).fit(X)
        clustering[k] = pd.DataFrame(kmeans.predict(X), index=points_highlighted)
        dist_mu = squareform(pdist(kmeans.cluster_centers_))
        sigma = []
        for i in range(k):
            points_in_cluster = clustering[k][clustering[k][0] == i].index
            sigma.append(sqrt(X.ix[points_in_cluster,:].var(axis=0).sum()))
        db_index.append(davies_bouldin(dist_mu, np.array(sigma)))
    db_index = np.array(db_index[1:])
    k_optimal = np.argmin(db_index) + 2
    return [list(clustering[k_optimal][clustering[k_optimal][0] == i].index) for i in range(k_optimal)]

