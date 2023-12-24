from utils import Classifier

### Define x value and y value.  ###
## Example
X_EX:list = [0,1,2,3,4,5,6,7,8,9]
Y_EX:list = [1,1,1,-1,-1,-1,1,1,1,-1]
## Homework
X_HW:list = [1, 3, 9,11]
Y_HW:list = [1,-1, 1,-1]

### Homework ###
## Design a strong Adaboost classifier for the following training set.
classifier_hw = Classifier(X_HW,Y_HW) # Create Classifier object.
for n,datas in enumerate(classifier_hw,1): # Start iterating.
    AVG,E,A,W = datas # Get the data value.
    print(f"Iterate {n}") # Show number of iterations.
    print(f"AVG={AVG}, E={E},  A={A}\nW={W}\n") # Show iteration results

### Adaboosting Example ###
# classifier_ex = Classifier(X_EX,Y_EX)   
# for n,datas in enumerate(classifier_ex,1) :
#     AVG,E,A,W = datas
#     print(f"Iterate {n}")
#     print(f"AVG={AVG}, E={E}, A={A}\nW={W}\n")

