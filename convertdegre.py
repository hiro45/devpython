def convertdegreCF(tc):
    tf = tc * 1.8 + 32
    return tf

def convertdegreFC(tf):
    tc = (tf-32) / 1.8
    return tc
