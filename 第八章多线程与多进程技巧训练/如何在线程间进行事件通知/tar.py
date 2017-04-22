#coding:utf-8
import tarfile
import os
def tarXML(tfname):
    tf=tarfile.open(tfname,"w:gz")
    for fname in os.listdir("."):
        if fname.endswith(".xml"):
            tf.add(fname)
            os.remove(fname)
    tf.close()
    if not tf.members:
        os.remove(tfname)

# tarXML("test.tgz")