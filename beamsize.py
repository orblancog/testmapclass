import mapclass
import metaclass2
import math


maporder = 2
print "  Map order is",maporder

tw = metaclass2.twiss2("mptline_mu_twiss_mapclass.tfs")
print "  ... reading ",len(tw.elems),"elements"
#print len(tw)
#print tw.elems[2].NAME
#print tw.elems[2].L

mt = mapclass.Map2(tw,order=maporder)
mf = mapclass.Map2(maporder,"fort.18")

sigma  =150e-6
div    = 0.45e-3
sigmax = sigma
sigmay = sigma
divx   = div
divy   = div
dpp = 0.2
ct=3e-3;

print "  fort.18 beamsize output"
meanx=mf.offset('x',[sigmax,divx,sigmay,divy,dpp,ct])
snd2x=mf.sigma('x',[sigmax,divx,sigmay,divy,dpp,ct])
meany=mf.offset('y',[sigmax,divx,sigmay,divy,dpp,ct])
snd2y=mf.sigma('y',[sigmax,divx,sigmay,divy,dpp,ct])
print "    beamsizex =", math.sqrt(snd2x - meanx**2),';'
print "    beamsizey =", math.sqrt(snd2y - meany**2),';'

print "  twiss beamsize output"
meanx=mt.offset('x',[sigmax,divx,sigmay,divy,dpp,ct])
snd2x=mt.sigma('x',[sigmax,divx,sigmay,divy,dpp,ct])
meany=mt.offset('y',[sigmax,divx,sigmay,divy,dpp,ct])
snd2y=mt.sigma('y',[sigmax,divx,sigmay,divy,dpp,ct])
print "    beamsizex =", math.sqrt(snd2x - meanx**2),';'
print "    beamsizey =", math.sqrt(snd2y - meany**2),';'
