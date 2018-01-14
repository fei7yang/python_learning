import cPickle

shoplistfile='shoplist.data'
shoplist=['apple','mange','carrot']

f=file(shoplistfile,'w')
cPickle.dump(shoplist,f)
f.close()

del shoplist

f=file(shoplistfile)
storedlist=cPickle.load(f)
print storedlist
