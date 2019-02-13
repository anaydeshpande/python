

def add_sparse_matrix(m1, m2):
    # your code here
    # Define empty directory
    m={}
    # Add key "Size" and value is "total number of rows and columns" in directory m
    m = {"Size":(len(m1),len(m2))}
    # Define empty list result
    result=[]
    # iterate throguh rows
    for i in range(len(m1)):
        #iterate through columns
        for j in range(len(m1[0])):
            # First row first column of m1 and so on
            e1 = m1[i][j]
            # First row first column of m2 and so on
            e2 = m2[i][j]
            print e1
            print e2
            result = e1 + e2
            print "result:" ,result
            # Adding to dict m as key (e1 ,e2) and value is addition of it.
            m[(e1, e2)] = result
    return m


def main():
    # your test code here
    m1 = [[1,2],
          [2,3]]
    m2 = [[3,4],
          [5,6]]
    # Calling function to add to matrics
    m = add_sparse_matrix(m1, m2)
    print m

# call main function
if __name__ == "__main__":
    main()