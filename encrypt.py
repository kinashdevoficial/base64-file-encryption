import base64
import sys
var_1 = sys.argv[1]
var_2 = 'r'
var_3 = 'w'
var_2 = open(var_1, var_2)
var_5 = var_2.read()
var_5 = base64.b64encode(var_5)
var_2.close()
var_3 = open(var_1, var_3)
var_3.write(var_5)
var_3.close()
var_6 = 'file encrypted with base64.'
print var_6
