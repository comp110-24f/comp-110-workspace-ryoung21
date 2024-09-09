# (1>2) or not (1>7)
# 1>2 false, 1>7 false, have False or not False, not evaluates before or, so not False is True,
# then have False or True, evaluates to True

# if <Boolean expression>:
#   <"then block, does something"
# <rest of program>
>>> True
True
>>> not True
False
>>> not False
True
>>> not not False
False
>>> 1>2
False
>>> 3>2
True
>>> not 3>2
False
>>> (3>2) and (1>2)
False
>>> (3>2) and (5>2)
True
>>> (3>2) or (1>2)
True
>>> (1>2) or not (1>7) 
True

