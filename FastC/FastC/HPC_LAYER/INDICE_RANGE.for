!DIR$ ATTRIBUTES FORCEINLINE :: indice_boucle_ssdom
           call indice_boucle_ssdom(ndo, extended_range,
     &                              ibloc , jbloc , kbloc,
     &                              icache, jcache, kcache,
     &                              param_int(KFLUDOM),
     &                              topo_s, ithread_sock,thread_pos_tmp,
     &                              size_cache,
     &                              synchro_receive_sock,
     &                              synchro_receive_th  ,
     &                              synchro_send_sock,
     &                              synchro_send_th  ,
     &                              param_int(NIJK), param_int(IJKV),
     &                              ind_dm_zone, ind_dm_socket,
     &                              ind_dm_omp, ijkv_sdm,
     &                              ind_sdm , ind_coe,
     &                              ind_grad, ind_rhs, 
     &                               ind_mjr, ind_ssa)

#if CHECK_BLOCK > 0
       if(ithread.eq.param_int( IO_THREAD).and.nitrun.eq.0)then
          if(ibloc*jbloc*kbloc.le.1) then
           write(*,'(a,6i4)')'sdm =',ind_sdm
           write(*,'(a,6i4)')'grad=',ind_grad
           write(*,'(a,6i4)')'coe =',ind_coe
           write(*,'(a,6i4)')'rhs =',ind_rhs
           write(*,'(a,6i4)')'mjr =',ind_mjr
           write(*,'(a,6i4)')'ssa =',ind_ssa
          endif
       endif
#endif

#if CHECK_SPLIT > 0
#include "FastC/HPC_LAYER/check_split0.for"
#endif