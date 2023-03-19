#!/usr/bin/python3
# Show multiplication table from 1 to 10.

for i in range(1, 10+1):
    for j in range(1,10+1):
        print(f"{str(i)} x {str(j)} = {str(i*j)}")
    print("---------------")