/*    
    Copyright 2013-2017 Onera.

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
#include <iostream>
# include "fastS.h"
# include "param_solver.h"
# include <string.h>

using namespace std;
using namespace K_FLD;


//=============================================================================
// Idem: in place + from zone + tc compact au niveau base 
//=============================================================================
void K_FASTS::recup3para_c(E_Float**& iptro, E_Int*& ipt_param_int,
				E_Float*& ipt_param_real, E_Int**& param_intt, 
				E_Float*& iptstk, E_Int& nstep, E_Int& omp_mode, E_Int& taille_tabs, E_Int& nidom)

   
{

  omp_mode = 0;

#pragma omp parallel default(shared) //private(cycle)
  {
#ifdef _OPENMP
    E_Int  ithread           = omp_get_thread_num() +1;
    E_Int  Nbre_thread_actif = omp_get_num_threads();
#else
    E_Int ithread = 1;
    E_Int Nbre_thread_actif = 1;
#endif
    E_Int Nbre_socket   = NBR_SOCKET;                       // nombre de proc (socket) sur le noeud a memoire partagee
    if( Nbre_thread_actif < Nbre_socket) Nbre_socket = 1;

    E_Int Nbre_thread_actif_loc, ithread_loc;
    if( omp_mode == 1) { Nbre_thread_actif_loc = 1;                 ithread_loc = 1;}
    else               { Nbre_thread_actif_loc = Nbre_thread_actif; ithread_loc = ithread;}

    E_Int topology[3];
    topology[0]=0;
    topology[1]=0;
    topology[2]=0;

    for (E_Int NoTransfert = 1; NoTransfert < ipt_param_int[0] + 1; NoTransfert++)

      {

	E_Int nbcomIBC = ipt_param_int[1];
	E_Int nbcomID  = ipt_param_int[2+nbcomIBC];
  
	E_Int shift_graph = nbcomIBC + nbcomID + 2;

	E_Int ech            = ipt_param_int[ NoTransfert +shift_graph];
 
	E_Int nrac = ipt_param_int[ ech +1 ];


	for  (E_Int irac=0; irac< nrac; irac++) // Boucle sur les différents raccords (frontières)
	  {

	    //E_Int shift_rac =  ech + 2 + irac;
	    E_Int timelevel = ipt_param_int[ ech +3 ];
	    E_Int shift_rac =  ech + 4 + timelevel*2 + irac;

	    E_Int NoD      =  ipt_param_int[ shift_rac + nrac*5     ]; // Numero zone donneuse du irac concerné
	    E_Int NoR      =  ipt_param_int[ shift_rac + nrac*11 +1 ]; // Numero zone receveuse du irac concerné

	    E_Int debut_rac = ech + 4 + timelevel*2 + 1 + nrac*16 + 27*irac;

	    E_Int ibcType = ipt_param_int[shift_rac + nrac * 3];

	    E_Int cycle;

	    cycle = param_intt[NoD][NSSITER]/ipt_param_int[debut_rac +25];

	    if (ipt_param_int[debut_rac + 25] > ipt_param_int[debut_rac + 24]) /// Le pas de temps de la zone donneuse est plus petit que celui de la zone receveuse 

	      {
		
		E_Int donorPts_[6];  E_Int idir = 2;
		donorPts_[0] =  ipt_param_int[debut_rac + 7];
		donorPts_[1] =  ipt_param_int[debut_rac + 8] ;
		donorPts_[2] =  ipt_param_int[debut_rac + 9];
		donorPts_[3] =  ipt_param_int[debut_rac + 10];
		donorPts_[4] =  ipt_param_int[debut_rac + 11];
		donorPts_[5] =  ipt_param_int[debut_rac + 12];
		int dir = ipt_param_int[debut_rac + 13];
		E_Int profondeur = ipt_param_int[debut_rac + 20];

		donorPts_[2*abs(dir)-1-(dir+abs(dir))/(2*abs(dir))] = donorPts_[2*abs(dir)-1-(dir+abs(dir))/(2*abs(dir))] -(dir/abs(dir))*(profondeur);

		E_Int taillefenetre;
		taillefenetre = (donorPts_[1] - donorPts_[0] + 1)*(donorPts_[3] - donorPts_[2] + 1)*(donorPts_[5] - donorPts_[4] + 1); 

		E_Int ipt_ind_dm_omp_thread[6]; 

		indice_boucle_lu_(NoD, ithread_loc, Nbre_thread_actif_loc, param_intt[NoD][ ITYPCP ],
				  donorPts_,
				  topology, ipt_ind_dm_omp_thread);
		E_Int donorPts[6];
		donorPts[0]=ipt_ind_dm_omp_thread[0];
		donorPts[1]=ipt_ind_dm_omp_thread[1];
		donorPts[2]=ipt_ind_dm_omp_thread[2];
		donorPts[3]=ipt_ind_dm_omp_thread[3];
		donorPts[4]=ipt_ind_dm_omp_thread[4];
		donorPts[5]=ipt_ind_dm_omp_thread[5];
	  
		if (nstep%cycle==cycle/2 and (nstep/cycle)%2==1) 
		  {

		    E_Int pos_tab = ipt_param_int[debut_rac + 26];

		    //// Recuperation de y6 en position 1 dans le tableau de stockage du raccord
		    E_Int ind=2;
		    copy_rk3localpara_(param_intt[NoD], donorPts , donorPts_, iptro[NoD], iptstk + pos_tab + 1*5*taillefenetre,ind,taillefenetre); 


		  }

	      }

	    else if (ipt_param_int[debut_rac + 25] < ipt_param_int[debut_rac + 24]) /// Le pas de temps de la zone donneuse est plus grand que celui de la zone receveuse
	      {

		E_Int donorPts_[6];  E_Int idir = 2;
		donorPts_[0] =  ipt_param_int[debut_rac + 7];
		donorPts_[1] =  ipt_param_int[debut_rac + 8] ;
		donorPts_[2] =  ipt_param_int[debut_rac + 9];
		donorPts_[3] =  ipt_param_int[debut_rac + 10];
		donorPts_[4] =  ipt_param_int[debut_rac + 11];
		donorPts_[5] =  ipt_param_int[debut_rac + 12];
		int dir = ipt_param_int[debut_rac + 13];
		E_Int profondeur = ipt_param_int[debut_rac + 20];

		donorPts_[2*abs(dir)-1-(dir+abs(dir))/(2*abs(dir))] = donorPts_[2*abs(dir)-1-(dir+abs(dir))/(2*abs(dir))] -(dir/abs(dir))*(profondeur);

		E_Int taillefenetre;
		taillefenetre = (donorPts_[1] - donorPts_[0] + 1)*(donorPts_[3] - donorPts_[2] + 1)*(donorPts_[5] - donorPts_[4] + 1);


		E_Int ipt_ind_dm_omp_thread[6]; 

		indice_boucle_lu_(NoD, ithread_loc, Nbre_thread_actif_loc, param_intt[NoD][ ITYPCP ],
				  donorPts_,
				  topology, ipt_ind_dm_omp_thread);
		E_Int donorPts[6];
		donorPts[0]=ipt_ind_dm_omp_thread[0];
		donorPts[1]=ipt_ind_dm_omp_thread[1];
		donorPts[2]=ipt_ind_dm_omp_thread[2];
		donorPts[3]=ipt_ind_dm_omp_thread[3];
		donorPts[4]=ipt_ind_dm_omp_thread[4];
		donorPts[5]=ipt_ind_dm_omp_thread[5];

 
		if (nstep%cycle==cycle/2 + cycle/4) 	   
	
		  {

		    E_Int pos_tab = ipt_param_int[debut_rac + 26];

		    E_Int ind=2;
		    copy_rk3localpara_(param_intt[NoD], donorPts ,donorPts_,  iptro[NoD], iptstk + pos_tab + 2*5*taillefenetre,ind,taillefenetre);

		  }







	      }




	  }

      } //boucle NoTransfert

  } // fin zone omp

  //#pragma omp barrier



}