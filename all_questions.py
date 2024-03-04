def question1():
    answers = {}
    # a) Agglomerative hierarchical clustering procedures are better able to handle outliers than k-means.
    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In Agglomerative clustering, outliers are less problematic and do not merge with any other clusters."
    "K-means has problems when data contain outliers."

    # For any given data set, different runs of k-means can produce different clusterings, but agglomerative hierarchical clustering procedures will always produce the same clustering.
    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means has a number of limitations with finding different types of clusters."
    "Agglomonerative clustering merges the closest pair but does not randomize the data points in each cluster."
    
    # K-means take less time and memory than agglomerative hierarchical clustering and is the most efficient clustering algorithm possible.
    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Aggolmerative clustering takes long time but produce efficent result than K-means."
    "K-means approach is computationally infeasible and find solutions that are not guaranteed."
    
    # During a post-processing step for K-means, a cluster is split by
    # picking one of the points of the cluster as a new centroid and 
    # then reassigning the points in the cluster either to the original centroid or the new centroid.
    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "In K-means, the splitting decrease the SSE and clusters are combined within the same points which reduce distance to the nearby centroid."
    
    # When clustering a dataset using K-means, whenever SSE decreases, cohesion increases.
    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In K-means, SSE has a measure of the cohesion in clusters."
    
    # When clustering a dataset using K-means, whenever SSB (the between sum of squares) increases, separation increases.
    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "Higher the total SSB of a clustering, more separated the clusters are from one another."

    #Cohesion and separation are independent for K-Means, i.e., improving cohesion (smaller SSE) doesnt necessarily improve separation (larger between sum of squares (SSB)).
    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "The importance of minimizing SSE cohesion is the same to maximizng SSB separation."

    # When clustering a dataset using K-means, SSE + BSS is a constant.
    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The sum of the total SSE and the total SSB is a constant, SSE + SSB"
    
    #When clustering a dataset using K-means, whenever cohesion increases, separation increases.
    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "The result is that minimizing SSE (cohesion) is equivalent to maximizing SSB (separation)"

    return answers

# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In Figure A, clusters have a centriod that has a distance."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The shaded regions are near to each other and not of circular shape or size."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "In Figure C, 12.5 seems to have point that is farthest away from any current cluster."

    return answers


# -----------------------------------------------------------
def question3():
    answers = {}
    # Compute the total SSE of the data points to the centroid, C.
    # type: a string that evaluates to a float
    answers["(a) SSE"] = "R^2 + R^2 + R^2 + R^2 = 4R^2"
    
    # Compute the total SSE of the data points to the origin, O.
    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4(a^2 + b^2 + R^2)"
    
    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10R^2"

    return answers

# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Assigned all three centroid"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Assigned all three centroid"

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Assigned points in rightmost centroid"

    return answers

# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A', 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Group A and Group B will be the smallest single link distance."

    # type: set
    answers["(b)"] = {'Group A', 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Group A and Group C will be the complete link distance."

    return answers


# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set(['B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'])

    # type: set
    answers["(a) boundary"] = set(['D', 'G'])

    # type: set
    answers["(a) noise"] = set(['A', 'H'])

    # type: set
    answers["(b) cluster 1"] = set(['B', 'C', 'D', 'E', 'F', 'G'])
    #Since point A is the farthest I would consider the closest points in the first cluster.
    #This cluster has more data points.

    # type: set
    answers["(b) cluster 2"] = set(['I', 'J', 'L', 'M'])
    #Since point H is the farthest I would consider the closest points in the second cluster.

    # type: set
    answers["(b) cluster 3"] = set()
    #There is no third cluster in figure 5.
    # type: set
    answers["(b) cluster 4"] = set()
    #There is no fourth cluster in figure 5.

    # type: set
    answers["(c)-a core"] = set(['B', 'C', 'E', 'F', 'I', 'J', 'L', 'M', 'D', 'G'])

    # type: set
    answers["(c)-a boundary"] = set(['A', 'H'])

    # type: set
    answers["(c)-a noise"] = set()
    # There's no point that is neither a core point nor a border point.

    # type: set
    answers["(c)-b cluster 1"] = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    # All points are clustered in this figure.

    # type: set
    answers["(c)-b cluster 2"] = set()
    # There's no second cluster in figure 5
    
    # type: set
    answers["(c)-b cluster 3"] = set()
    # There's no third cluster in figure 5

    # type: set
    answers["(c)-b cluster 4"] = set()
    # There's no fourth cluster in figure 5

    return answers


# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The cluster 4 has less distinct values."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The cluster 1 has distinct values."

    return answers


# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Has one diagonal entry that's blue."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "It shows different colors in the non diagonal entries."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal entries are more blue and light blue compared to others."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows that are not light blue has different colors with non diagonal entries."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Has a blue diagonal entries that's compared to the previous two."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Most rows are similar but one different color are non diagonal. "

    # type: string
    answers["(b) Row 1"] = "1-100 cluster"

    # type: string
    answers["(b) Row 2"] = "101-200 cluster"

    # type: string
    answers["(b) Row 3"] = "201-300 cluster"

    # type: string
    answers["(b) Row 4"] = "301-400 cluster"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Cluster is less cohesive in diagonal entry, clusters have different distances."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Cluster is more cohesive, entries have the same color which the cluster are near each other."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Cluster is more cohesive, entries have the same color which the cluster are near each other."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Cluster is less cohesive in diagonal entry, clusters have different distances."

    return answers


# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Overlapping', 'Partial']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'Fuzzy', 'Complete']

    # type: list
    answers["(d)"] = ['Hierarchical', 'Overlapping', 'Partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Can't be grouped with some student didn't get in the data mining class."

    return answers


# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "The noise is much denser than the interest patterns so noise, eyes, and mouth will be out."

    # type: string
    answers["(a) Figure (b)"] = "The points in nose, eyes, and mouth are much closer together and DBSCAN can work for this task."

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN can be use for every figure to identify the clusters."

    # type: string
    answers["(b) Figure (a)"] = "In this figure, K-means does not work for figure a."

    # type: string
    answers["(b) Figure (b)"] = "In this figure, K-means does work for figure b."

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "You can't use K-mean for every figure with the placement in certain data point to the cluster."

    # type: string
    answers["(c)"] = "The reciprocal of the density being use in DBSCAN."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
