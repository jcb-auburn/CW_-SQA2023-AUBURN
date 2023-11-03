"""
Simple Python Program that Fuzzes 5 methods in KubeSec-master
"""
import parser
import graphtaint
import scanner

def simpleFuzzer(): 
    #print("Testing")
    """
    10/30/2023 - "No such file or directory" error (Invalid path)
    """
    try:
        parser.readYAMLAsStr("test")
    except Exception as e:
        print(e)
    """
    10/30/2023 - "Cannot unpack non-iterable int object" error (Type error)
    """
    try:
        graphtaint.constructHelmString(int(1))
    except Exception as e:
        print(e)
    """
    10/30/2023 - "Argument of type 'int' is not iterable" error (Type error)
    """
    try:
        parser.checkIfWeirdYAML(int(0))
    except Exception as e:
        print(e)
    """
    10/30/2023 - "Not enough values to unpack (expected 2, got 1)" error 
    """
    try:
        graphtaint.getValidTaints("xcrx       999999998724234545dafsdk"+"crthflaksdhfkjlasdhlfasdlfsdkflkasdhfdsjkx")
    except Exception as e:
        print(e)
    """
    10/31/2023 - "'list' object has no attribute 'items' error (Type error)
    """
    try:
        scanner.getItemFromSecret([], 1)
    except Exception as e:
        print(e)

if __name__=='__main__':
    simpleFuzzer()