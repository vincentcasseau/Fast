# - display_temporal_criteria (pyTree) - 
import Converter.PyTree as C
import Generator.PyTree as G
import Connector.PyTree as X
import FastS.PyTree as FastS
import Fast.PyTree as Fast
import Initiator.PyTree as I
import KCore.Adim as Adim

ni = 155; dx = 100./(ni-1); dz = 0.01
a = G.cart((-50,-50,0.), (dx,dx,dz), (ni,ni,2))
a = C.fillEmptyBCWith(a, 'far', 'BCFarfield', dim=2)
I._initConst(a, MInf=0.4, loc='centers')
C._addState(a, 'GoverningEquations', 'Euler')
C._addState(a, MInf=0.4)
t = C.newPyTree(['Base',a])

# Numerics
numb = {}
numb["temporal_scheme"]    = "explicit"
numb["ss_iteration"]       = 20
numb["modulo_verif"]       = 1
numz = {}
#numz["time_step"]          = 0.00004444
numz["time_step_nature"]    = "local"
numz["cfl"]    = 0.6
numz["scheme"]             = "ausmpred"
Fast._setNum2Zones(t, numz); Fast._setNum2Base(t, numb)

# Prim vars, solver tag, compact, metric
(t, tc, metrics) = FastS.warmup(t, None)

# Compute
for it in range(1,5):
    FastS._compute(t, metrics, it)
    FastS.display_temporal_criteria(t, metrics, it)

# Save
C.convertPyTree2File(t, 'out.cgns')
