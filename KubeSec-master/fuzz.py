"""
Simple Python Program that Fuzzes 5 methods in KubeSec-master
"""
import parser
import graphtaint
import scanner

def simpleFuzzer(): 
    print("Testing")
    """
    10/30/2023 - "No such file or directory" error (Invalid path)
    """
    #parser.readYAMLAsStr("test")
    """
    10/30/2023 - "Cannot unpack non-iterable int object" error (Type error)
    """
    #graphtaint.constructHelmString(int(1))
    """
    10/30/2023 - "Argument of type 'int' is not iterable" error (Type error)
    """
    #parser.checkIfWeirdYAML(int(0))
    """
    10/30/2023 - "Not enough values to unpack (expected 2, got 1)" error 
    """
    #graphtaint.getValidTaints("xcrx       999999998724234545dafsdk"+"crthflaksdhfkjlasdhlfasdlfsdkflkasdhfdsjkx")
    """
    10/31/2023 - "'list' object has no attribute 'items' error (Type error)
    """
    #scanner.getItemFromSecret([], 1)

if __name__=='__main__':
    simpleFuzzer()