c***********************************************************************
c     $Date: 2010-11-04 13:25:50 +0100 (Thu, 04 Nov 2010) $
c     $Revision: 64 $
c     $Author: IvanMary $
c***********************************************************************
      subroutine viles( ndo, nidom, Nbre_thread_actif, 
     &        ithread, Nbre_socket, socket, mx_synchro, neq_rot,
     &        param_int, param_real, 
     &        ijkv_sdm,
     &        ind_dm_zone, ind_dm_socket, ind_dm_omp,
     &        socket_topology, lok ,
     &        rop , ti, tj, tk, vol, xmut, dist, rot)

c***********************************************************************
c_U   USER : TERRACOL
c
c     ACT
c_A    Appel du calcul des flux explicites
c
c     VAL
c_V    gaz parfait monoespece
c_V    processeur domaine
c_V    steady/unsteady
c
c     INP
c_I    tijk     : vecteur param_int( IO_THREAD)rmale aux facettes des mailles
c_I    vent     : vitesses d'entrainement aux facettes preced.
c
c     LOC
c_L    flu      : flux convectifs dans une direction de maillage
c
c     I/O
c_/    rot    : increment de la solution
c
c***********************************************************************
      implicit none

      INTEGER_E ndo, nidom, Nbre_thread_actif , mx_synchro, 
     & ithread, Nbre_socket, socket , neq_rot


      INTEGER_E  ijkv_sdm(3),ind_dm_zone(6),
     & ind_dm_omp(6), ind_dm_socket(6), socket_topology(3),
     & param_int(0:*), lok(*)

      REAL_E rop(*), ti(*),tj(*),tk(*),vol(*), xmut(*), dist(*),rot(*)

      REAL_E param_real(0:*)

C Var loc 
      INTEGER_E nitrun, depth, ind_flt(6), ind_extrap(6)
#include "FastS/HPC_LAYER/LOC_VAR_DECLARATION.for"


#include "FastS/param_solver.h"
#include "FastS/formule_param.h"
#include "FastS/formule_mtr_param.h"

      nitrun =0
      !Calcul de la taille minimal 1D du bloc thread 
      if(param_int(ITYPCP).eq.2) then
        lmin = 8
      else
        lmin =10
      endif
#include "FastS/HPC_LAYER/WORK_DISTRIBUTION_BEGIN.for"
#include "FastS/HPC_LAYER/LOOP_CACHE_BEGIN.for"
#include "FastS/HPC_LAYER/INDICE_RANGE.for"

       call synchro_omp_scater(param_int, ithread,
     &                     lth, sens,lgo,lwait,Nbre_socket,
     &                     Nbre_thread_actif,thread_parsock,
     &                     lok_shap_sock, lok_shap,neq_lok,
     &                     socket , socket_topology, socket_pos,
     &                     ithread, thread_topology,thread_pos_tmp,
     &                     synchro_receive_sock, synchro_send_sock,
     &                     synchro_receive_th  , synchro_send_th,
     &                     ibloc , jbloc , kbloc , ijkv_thread,
     &                     icache, jcache, kcache, ijkv_sdm,
     &                     ind_dm_omp,
     &                     rot, rot, rot, 
     &                     lok(1),lok(ipt_lok_sock),
     &                     lok(ipt_lok), omp_wait )


      !Calcul de la viscosite laminaire si nslaminar ou (nsles + dom 2D)
      if(param_int(IFLOW).eq.2) then
c
         if(param_int(ILES).eq.0.or.param_int(NIJK+4).eq.0) then
c
            call invist(ndo, param_int, param_real, ind_coe, rop, xmut )
c
         !LES selective mixed scale model
         else
            depth =  param_int(NIJK+3)
            call lesvist(ndo, param_int, param_real, neq_rot,depth,
     &                   ind_grad, ind_coe, ind_dm_zone,
     &                   xmut, rop, ti,tj,tk, vol, rot)
         endif

      !! remplissage tableau xmut si SA uniquememnt. 
      !! Pour ZDES, remplissage dans terme source inline avec
      !! calcul pas de temps
      elseif(param_int(IFLOW).eq.3) then

          call vispalart(ndo, param_int, param_real, ind_coe,
     &                   ti, tj, tk, vol, dist, xmut,rop)

      endif
               
      call synchro_omp_scater(param_int, ithread,
     &                        lth, sens,lgo,lwait,Nbre_socket,
     &                        Nbre_thread_actif,thread_parsock,
     &                        lok_shap_sock, lok_shap,neq_lok,
     &                        socket , socket_topology, socket_pos,
     &                        ithread, thread_topology,thread_pos_tmp,
     &                        synchro_receive_sock, synchro_send_sock,
     &                        synchro_receive_th  , synchro_send_th,
     &                        ibloc , jbloc , kbloc , ijkv_thread,
     &                        icache, jcache, kcache, ijkv_sdm,
     &                        ind_dm_omp,
     &                        rot, rot, rot, 
     &                        lok(1),lok(ipt_lok_sock),
     &                        lok(ipt_lok), omp_go )

#include "FastS/HPC_LAYER/LOOP_CACHE_END.for"
#include "FastS/HPC_LAYER/WORK_DISTRIBUTION_END.for"


      end