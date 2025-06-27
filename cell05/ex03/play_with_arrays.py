#!/usr/bin/env python3
original_arrary = [ 2 ,3 ,4, 5, 6, 7 ,8]
new_arrary = {x + 23 for x in original_arrary if x >4 }
print(original_arrary)
print(new_arrary)
