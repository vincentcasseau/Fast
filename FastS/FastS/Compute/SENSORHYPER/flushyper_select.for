c***********************************************************************
c     $Date: 2013-08-26 16:00:23 +0200 (lun. 26 aout 2013) $
c     $Revision: 64 $
c     $Author: IvanMary $
c***********************************************************************
      subroutine flushyper_select(ndom, nitcfg, ithread, nptpsi,
     &                        param_int, param_real,
     &                        ind_dm, ind_loop,ijkv_thread, ijkv_sdm,
     &                        synchro_send_sock, synchro_send_th,
     &                        synchro_receive_sock, synchro_receive_th,
     &                        ibloc , jbloc , kbloc ,
     &                        icache, jcache, kcache,
     &                        psi, wig, stat_wig, rop, drodm,
     &                        ti,ti_df,tj,tj_df,tk,tk_df, vol,vol_df,
     &                        venti, ventj, ventk, xmut)
c***********************************************************************
c_U   USER : PECHIER
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
c_I    tijk     : vecteur normale aux facettes des mailles
c_I    ventijk     : vitesses d entrainement aux facettes preced.
c_I    qm,qp    : etats droit et gauche aux interfaces d une maille
c
c     LOC
c_L    flu      : flux convectifs dans une direction de maillage
c
c     I/O
c_/    drodm    : increment de la solution
c***********************************************************************
      implicit none

#include "FastS/param_solver.h"

      INTEGER_E ndom, nitcfg,ithread, nptpsi,
     & icache, jcache, kcache,ibloc, jbloc, kbloc,
     & ijkv_thread(3), ijkv_sdm(3), ind_loop(6),ind_dm(6),
     & synchro_send_sock(3),synchro_send_th(3),
     & synchro_receive_sock(3), synchro_receive_th(3), param_int(0:*)


      REAL_E rop(*),xmut(*),drodm(*), ti(*),tj(*),tk(*),vol(*),
     & venti(*),ventj(*),ventk(*), wig(*),stat_wig(*),
     & ti_df(*),tj_df(*),tk_df(*),vol_df(*)

      REAL_E param_real(0:*)
      REAL_E psi(nptpsi)

C Var loc
      INTEGER_E option, ale

      if(ind_loop(1).gt.ind_loop(2)) return 
      if(ind_loop(3).gt.ind_loop(4)) return 
      if(ind_loop(5).gt.ind_loop(6)) return

      ale = min(param_int(LALE),1)

      option =  1000*ale
     &        +  100*param_int(SLOPE)
     &        +   10*param_int(IFLOW)
     &        +      param_int(ITYPZONE)


       IF  (option.eq.220) THEN
                                               
           call flushyper_lamin_o3_3dfull(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.221) THEN
                                               
           call flushyper_lamin_o3_3dhomo(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.222) THEN
                                               
           call flushyper_lamin_o3_3dcart(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.223) THEN
                                               
           call flushyper_lamin_o3_2d(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.230) THEN
                                               
           call flushyper_SA_o3_3dfull(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.231) THEN
                                               
           call flushyper_SA_o3_3dhomo(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.232) THEN
                                               
           call flushyper_SA_o3_3dcart(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.233) THEN
                                               
           call flushyper_SA_o3_2d(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.210) THEN
                                               
           call flushyper_euler_o3_3dfull(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.211) THEN
                                               
           call flushyper_euler_o3_3dhomo(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.212) THEN
                                               
           call flushyper_euler_o3_3dcart(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.213) THEN
                                               
           call flushyper_euler_o3_2d(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1220) THEN
                                               
           call flushyper_ale_lamin_o3_3dfull(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1221) THEN
                                               
           call flushyper_ale_lamin_o3_3dhomo(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1222) THEN
                                               
           call flushyper_ale_lamin_o3_3dcart(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1223) THEN
                                               
           call flushyper_ale_lamin_o3_2d(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1230) THEN
                                               
           call flushyper_ale_SA_o3_3dfull(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1231) THEN
                                               
           call flushyper_ale_SA_o3_3dhomo(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1232) THEN
                                               
           call flushyper_ale_SA_o3_3dcart(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1233) THEN
                                               
           call flushyper_ale_SA_o3_2d(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1210) THEN
                                               
           call flushyper_ale_euler_o3_3dfull(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1211) THEN
                                               
           call flushyper_ale_euler_o3_3dhomo(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1212) THEN
                                               
           call flushyper_ale_euler_o3_3dcart(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
       ELSEIF (option.eq.1213) THEN
                                               
           call flushyper_ale_euler_o3_2d(ndom, ithread,
     &                 param_int, param_real,
     &                 ind_dm, ind_loop, ijkv_thread, ijkv_sdm,
     &                 synchro_send_sock, synchro_send_th,
     &                 synchro_receive_sock, synchro_receive_th,
     &                 ibloc , jbloc , kbloc ,
     &                 icache, jcache, kcache,
     &                 rop, drodm, wig,
     &                 venti, ventj, ventk,
     &                 ti, tj, tk, vol, xmut)
                                               
      ELSE
         write(*,*) ' option = ' , option 
            write(*,*)'Unknown flux options'
           call error('gtfl3$',70,1)

      ENDIF
 
      end