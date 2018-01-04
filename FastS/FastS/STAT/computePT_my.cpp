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


# include "fastS.h"
# include "param_solver.h"
# include "string.h"
#ifdef _OPENMP
# include <omp.h>
#endif
using namespace std;
using namespace K_FLD;

//=============================================================================
// Compute pour l'interface pyTree
//=============================================================================
PyObject* K_FASTS::computePT_my(PyObject* self, PyObject* args)
{
  PyObject* zones; PyObject* zones_my;  PyObject* metrics; 
  if (!PyArg_ParseTuple(args, "OOO", &zones , &zones_my, &metrics)) 
    return NULL;

  /* tableau pour stocker dimension sous-domaine omp */
  E_Int threadmax_sdm = 1;
#ifdef _OPENMP
  threadmax_sdm  = omp_get_max_threads();
#endif

  E_Int nidom        = PyList_Size(zones);

  //printf("nombre de zone a traiter= %d\n",nidom);

  E_Float** iptro; E_Float** iptmut; E_Float** iptromoy;
  E_Float** ipti;  E_Float** iptj;  E_Float** iptk; E_Float** iptvol;
  E_Float** ipti_df; E_Float** iptj_df;  E_Float** iptk_df ; E_Float** iptvol_df;
  E_Float** ipt_param_real;

  E_Int** iptmoy_param; E_Int**   ipt_param_int;

  ipt_param_real    = new  E_Float*[nidom*12];
  iptro             = ipt_param_real + nidom;
  iptmut            = iptro          + nidom;
  ipti              = iptmut         + nidom;
  iptj              = ipti           + nidom;
  iptk              = iptj           + nidom;
  iptvol            = iptk           + nidom;
  ipti_df           = iptvol         + nidom;
  iptj_df           = ipti_df        + nidom;
  iptk_df           = iptj_df        + nidom;
  iptvol_df         = iptk_df        + nidom;
  iptromoy          = iptvol_df      + nidom;

  ipt_param_int     = new  E_Int*[nidom*2];
  iptmoy_param      = ipt_param_int    + nidom;

  vector<PyArrayObject*> hook;

  for (E_Int nd = 0; nd < nidom; nd++)
  { 
    // check zone
    PyObject* zone    = PyList_GetItem(zones   , nd); // domaine i
    PyObject* zone_my = PyList_GetItem(zones_my, nd); // domaine i pour les stat

    /* Get numerics from zone */
    PyObject*   numerics  = K_PYTREE::getNodeFromName1(zone    , ".Solver#ownData");
    PyObject*          t  = K_PYTREE::getNodeFromName1(numerics, "Parameter_int"); 
    ipt_param_int[nd]     = K_PYTREE::getValueAI(t, hook);
                       t  = K_PYTREE::getNodeFromName1(numerics, "Parameter_real"); 
    ipt_param_real[nd]    = K_PYTREE::getValueAF(t, hook);


    PyObject* sol_center;
    sol_center   = K_PYTREE::getNodeFromName1(zone      , "FlowSolution#Centers");
    t            = K_PYTREE::getNodeFromName1(sol_center, "Density");
    iptro[nd]    = K_PYTREE::getValueAF(t, hook);

    if(ipt_param_int[nd][ IFLOW ] > 1)
      { t  = K_PYTREE::getNodeFromName1(sol_center, "ViscosityEddy");
        if (t == NULL) { PyErr_SetString(PyExc_ValueError, "viscosity is missing for NS computation."); return NULL; }
        else           { iptmut[nd]   = K_PYTREE::getValueAF(t, hook);}
      }
    else {iptmut[nd] = iptro[nd];}


    // Check metrics
    PyObject* metric = PyList_GetItem(metrics, nd); // metric du domaine i

    GET_TI(   METRIC_TI  , metric, ipt_param_int[nd], ipti [nd]  , iptj [nd]  , iptk [nd]  , iptvol[nd]    )
    GET_TI(   METRIC_TIDF, metric, ipt_param_int[nd], ipti_df[nd], iptj_df[nd], iptk_df[nd], iptvol_df[nd] )


    /*----------------------------------*/
    // Extraction des pointers et parametres stats
    /*----------------------------------*/
    sol_center   = K_PYTREE::getNodeFromName1(zone_my   , "FlowSolution#Centers");
    t            = K_PYTREE::getNodeFromName1(sol_center, "MomentumX");
    iptromoy[nd] = K_PYTREE::getValueAF(t, hook);

    t  = K_PYTREE::getNodeFromName1(zone_my, ".Solver#post");
    if ( t == NULL) { PyErr_SetString(PyExc_ValueError, "stat: .Solver#post is missing or is invalid."); return 0; }

    iptmoy_param[nd]= K_PYTREE::getValueAI(t, hook);


    //
    //
    // on incremente le nombre d'echantillon dans la zone sequentielle
    //
    //
    //nbtps = nbtps +1 (funk)
    iptmoy_param[nd][2] = iptmoy_param[nd][2] +1;

  }
  
//
//  
//  Reservation tableau travail temporaire pour calcul du champ N+1
//

  //printf("thread =%d\n",threadmax_sdm);
  FldArrayI topology(  3*threadmax_sdm); E_Int* ipt_topology   =  topology.begin();
  FldArrayI ind_dm_omp(6*threadmax_sdm); E_Int* ipt_ind_dm_omp =  ind_dm_omp.begin();


#pragma omp parallel default(shared)
  {
#ifdef _OPENMP
    E_Int  ithread           = omp_get_thread_num() +1;
    E_Int  Nbre_thread_actif = omp_get_num_threads();
#else
    E_Int ithread = 1;
    E_Int Nbre_thread_actif = 1;
#endif
      //
      //---------------------------------------------------------------------
      // -----Boucle sur num.les domaines de la configuration
      // ---------------------------------------------------------------------
        E_Int lthermique =0; E_Int lreynolds =0; E_Int neq_grad = 3;
        for (E_Int nd = 0; nd < nidom; nd++)
          {  

             E_Int* ipt_topology_thread    = ipt_topology    + (ithread-1)*3; 
             E_Int* ipt_ind_dm_omp_thread  = ipt_ind_dm_omp  + (ithread-1)*6;

             // Distribution de la sous-zone sur les threads
             E_Int type_decoup =2;
             indice_boucle_lu_(nd, ithread, Nbre_thread_actif, type_decoup,
                               iptmoy_param[nd]+11, 
                               ipt_topology_thread, ipt_ind_dm_omp_thread );

            //!!! Mettre un test pour ne pas les declarer si moyenne standard
            //if(lreynolds.or.lthermique) lgrad=.true.
            //!Tableau gradient                                    
            // neq_grad = 3
            // if(lthermique) neq_grad = 4
            //!coeficient pour calcul gradient ordre4 !c1=1 c2 =0 ordre 2
            //c1 = 7./6
            //c2 = 1./6


             cpmys_rij_(nd,  ipt_param_int[nd][ NDIMDX ] , ipt_param_int[nd][ NDIMDX_MTR ], iptmoy_param[nd][3],
                             ipt_param_int[nd][ NEQ ]    , iptmoy_param[nd][4]            , neq_grad           ,
                             ipt_param_int[nd][ NEQ_IJ ] , ipt_param_int[nd][ NEQ_K ]     ,  ipt_param_int[nd][ ITYPZONE ],
                             lthermique                  , lreynolds                      ,
                             ipt_param_int[nd]+ NIJK_MTR , ipt_param_int[nd]+ NIJK        ,  iptmoy_param[nd]+6,  ipt_param_int[nd]+ IJKV     ,
                             iptmoy_param[nd]        ,
                             ipt_ind_dm_omp_thread   , ipt_param_real[nd][ GAMMA ],  ipt_param_real[nd][ CVINF ], ipt_param_real[nd][ PRANDT ],
                             iptro[nd]               , iptmut[nd]             ,
                             ipti[nd]                , iptj[nd]               , iptk[nd]                , iptvol[nd]       , 
                             ipti_df[nd]             , iptj_df[nd]            , iptk_df[nd]             , iptvol_df[nd]    ,
                             iptromoy[nd]);           

          }// boucle zone 
  }  // zone OMP


  delete [] ipt_param_real;
  delete [] ipt_param_int;

  RELEASEHOOK(hook)

  Py_INCREF(Py_None);
  return Py_None;
}
