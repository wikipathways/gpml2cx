import ndex2

mycx = ndex2.create_nice_cx_from_file('./myfile.cx')
print(mycx)
print(type(mycx))

mynx = mycx.to_networkx(mode='default')
print(mynx)
print(type(mynx))
