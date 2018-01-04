/*    
    Copyright 2013-2018 Onera.

    This file is part of Cassiopee.

    Cassiopee is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Cassiopee is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Cassiopee.  If not, see <http://www.gnu.org/licenses/>.
*/
#define K_ARRAY_UNIQUE_SYMBOL
#include "fast.h"

// ============================================================================
/* Dictionnary of all functions of the python module */
// ============================================================================
static PyMethodDef Pyfast [] =
{
  {NULL, NULL}
};

// ============================================================================
/* Init of module */
// ============================================================================
extern "C"
{
  void initfast();
  void initfast()
  {
    Py_InitModule("fast", Pyfast);
    import_array();
  }
}
//=============================================================================
/* Fonctions fortran declarees dans Fast mais non appelees dans Fast   
   Used to force some functions to belong to fast library  */
//=============================================================================
void K_FAST::testFooFast()
{
  E_Int i; E_Float f;
  cptimestepconv_(i, f, NULL, NULL, NULL, NULL, NULL, NULL, f, f);
  cptimestepconvmotion_(i, NULL, NULL, NULL, f,  NULL, NULL, NULL, NULL, NULL, NULL, f, f);
  cptimesteptur_(i, NULL, f, NULL, NULL, NULL, NULL, f, f, f, f);
  denconvec_(i, NULL, NULL, NULL, NULL, NULL, NULL,NULL, NULL, NULL);
  pressure_(i, NULL, NULL, NULL, NULL, NULL, f, NULL);
  cons2velocity_(i, NULL, NULL, NULL, NULL,NULL, NULL, NULL);
  viscosity_(i, f, f, NULL, NULL);
  heatcoef_(i, f, f, NULL, NULL);
  temp_(i, f, NULL, NULL, NULL, NULL, NULL, NULL);
  heatflux_(i, NULL, NULL, NULL, NULL, NULL, NULL, NULL); 
  visctensor_(i, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
  densfluxdiff_(i, NULL, NULL, NULL, NULL, NULL, NULL, 
                NULL, NULL, NULL, NULL, NULL, NULL,
                NULL, NULL, NULL, NULL, NULL, NULL,
                NULL, NULL, NULL, NULL, NULL, NULL);
  setallbvaluesatf_(i, i, NULL, f, i, i, i, i);
  extrapallbvaluesf_(i, i, NULL, i, i, i, i);
}
