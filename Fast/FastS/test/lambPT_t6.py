# - compute (pyTree) -
# - Lamb vortex [Euler/explicit] -
# - senseur hyper -
import Generator.PyTree as G
import Converter.PyTree as C
import Initiator.PyTree as I
import Fast.PyTree as Fast
import FastS.PyTree as FastS
import KCore.test as test
import Converter.Internal as Internal
test.TOLERANCE=1.e-8

mach = 0.7
a = G.cart((0,0,0), (0.5,0.5,0.25), (200,100,2))
a = I.initLamb(a, position=(25.,25.), Gamma=2., MInf=mach, loc='centers')
t = C.newPyTree(['Base', a])
t = C.addState(t, 'GoverningEquations', 'Euler')
t = C.addState(t, MInf=mach)

# Numerics
numb = {}
numb["temporal_scheme"]    = "explicit"
numb["ss_iteration"]       = 20
numz = {}
numz["time_step"]          = 0.01
numz["scheme"]             = "senseur"
numz["slope"]              = "o3sc"
Fast._setNum2Zones(t, numz); Fast._setNum2Base(t, numb)

(t, tc, metrics) = FastS.warmup(t, None)

nit = 1000 ; time = 0.
timeStep = numz['time_step']
for it in range(nit):
    FastS._compute(t, metrics, it)
    time += timeStep

Internal._rmNodesByName(t, '.Solver#Param')
Internal._rmNodesByName(t, '.Solver#ownData')
test.testT(t,1)
