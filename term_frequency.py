import math
tf = [['체첸', [2, 3]],
      ['공화국', [2, 2], [28, 2], [34, 1], [45, 2], [58, 1], [73, 2], [80, 2]],
      ['또는', [2, 1], [28, 1], [65, 1], [80, 1]],
      ['줄여서', [2, 1], [30, 1], [73, 1]],
      ['러시아', [2, 1], [23, 1], [32, 1], [92, 2], [93, 2], [96, 1]],
      ['사용되', [2, 1], [38, 1], [71, 1]],
      ['언어', [2, 1], [51, 2]],
      ['체첸어', [2, 2]],
      ['러시아어', [2, 1]],
      ['캅카스제어', [2, 2]],
      ['중', [2, 1], [5, 1], [10, 1], [13, 1], [22, 1], [32, 2], [33, 1], [35, 1], [67, 1], [71, 1], [92, 1]],
      ['북동', [2, 1]],
      ['불리', [2, 1], [77, 1]],
      ['그룹', [2, 1], [6, 1]],
      ['속하는데', [2, 1]],
      ['인구시어', [2, 1]],
      ['매우', [2, 1]],
      ['밀접한', [2, 1]],
      ['관계', [2, 1]],
      ['있다', [2, 1], [3, 1], [4, 1], [24, 3], [28, 1], [30, 2], [32, 1], [38, 2], [43, 1], [47, 1], [50, 1], [54, 1], [57, 2], [63, 1], [64, 2], [65, 1], [66, 1], [71, 1], [73, 2], [74, 3], [78, 1], [80, 1], [81, 2], [82, 1], [83, 1], [90, 1], [98, 1]]]


def term_frequency():
    # tf : total term index
    # tf[i] : one term index
    # tf[i][0] : term
    # tf[i][1] : [docID, frequency]
    # tf[i][1][0] : docID
    # tf[i][1][1] : frequency
    # len(tf[i] - 1) :

    for i in range(len(tf)) :
      for j in range(len(tf[i]) - 1):
            tf[i][j+1][1] = 1 + math.log10(tf[i][j+1][1])

term_frequency()