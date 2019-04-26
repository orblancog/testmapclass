import sys

sys.path.append('/afs/cern.ch/work/o/oblancog/public/progs/mapclass/MapClass2_C++/MapClass2/')
sys.path.append('/afs/cern.ch/work/o/oblancog/public/progs/mapclass/MapClass2_C++/MapClass2/C++MapConstruction/')

import mapclass
import metaclass2
import math

maporder = 5
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
meanxfr=mf.offset('x',[sigmax,divx,sigmay,divy,dpp,ct])
snd2xfr=mf.sigma('x',[sigmax,divx,sigmay,divy,dpp,ct])
meanyfr=mf.offset('y',[sigmax,divx,sigmay,divy,dpp,ct])
snd2yfr=mf.sigma('y',[sigmax,divx,sigmay,divy,dpp,ct])
print "    beamsizex =", math.sqrt(snd2xfr - meanxfr**2),';'
print "    beamsizey =", math.sqrt(snd2yfr - meanyfr**2),';'

print "  twiss beamsize output"
meanxtw=mt.offset('x',[sigmax,divx,sigmay,divy,dpp,ct])
snd2xtw=mt.sigma('x',[sigmax,divx,sigmay,divy,dpp,ct])
meanytw=mt.offset('y',[sigmax,divx,sigmay,divy,dpp,ct])
snd2ytw=mt.sigma('y',[sigmax,divx,sigmay,divy,dpp,ct])
print "    beamsizex =", math.sqrt(snd2xtw - meanxtw**2),';'
print "    beamsizey =", math.sqrt(snd2ytw - meanytw**2),';'


print "  "
print "  Difference between beamsize from fort.18 and twiss maps"
print "    beamsizex =", ( math.sqrt(snd2xfr - meanxfr**2) - math.sqrt(snd2xtw - meanxtw**2) )/ math.sqrt(snd2xfr - meanxfr**2) * 100,"%"
print "    beamsizey =", ( math.sqrt(snd2yfr - meanyfr**2) - math.sqrt(snd2ytw - meanytw**2) )/ math.sqrt(snd2xfr - meanxfr**2) * 100,"%"
