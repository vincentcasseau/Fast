c***********************************************************************
c     $Date: 2013-08-26 16:00:23 +0200 (lun. 26 août 2013) $
c     $Revision: 35 $
c     $Author: IvanMary $
c***********************************************************************
      subroutine bvbs_wall_inviscid(idir,lrhs, neq_mtr, mobile_coef,
     &                             param_int, ind_loop,
     &                             ventijk, tijk, rop)
c***********************************************************************
c_U   USER : PECHIER
c
c     ACT
c     Paroi glissante
c     VAL
c_V    Optimisation NEC
c
c     COM
c_C    MODIFIER bvas3.f (passage de ird1,ird2a,ird2b ?????)
c***********************************************************************
      implicit none

#include "FastS/param_solver.h"

      INTEGER_E idir,lrhs, neq_mtr, ind_loop(6), param_int(0:*)

      REAL_E rop    (param_int(NDIMDX     ), param_int(NEQ)      )
      REAL_E ventijk(param_int(NDIMDX_VENT), param_int(NEQ_VENT) )
      REAL_E tijk   (param_int(NDIMDX_MTR ), neq_mtr             )
      REAL_E mobile_coef
C Var local
      INTEGER_E  inc2,inc3,li1,li2,l,iref,jref,kref,
     & njf,nkf,ldjr,ic,jc,kc,i,j,k,li3,ldp,kc_vent,lmtr
      REAL_E ci_mtr,cj_mtr,ck_mtr,ck_vent,c_ale,tcx,tcy,tcz,
     & ventx,venty,ventz,r,u,v,w,ut,vt,wt,ua,va,wa,s_1,qn,surf

#include "FastS/formule_param.h"
#include "FastS/formule_mtr_param.h"
#include "FastS/formule_vent_param.h"

!      write(*,*)'idir=', idir,nijk(4),nijk(5),ndimdx
!      write(*,*)'nijk=', nijk
!      write(*,*)'loop=', ind_loop


c......determine la forme des tableuz metrique en fonction de la nature du domaine
      !Seule la valeur de k_vent et ck_vent a un sens dans cet appel
      call shape_tab_mtr(neq_mtr, param_int, idir,
     &                   ic,jc,kc,kc_vent,
     &                   ci_mtr,cj_mtr,ck_mtr,ck_vent,c_ale)

      ! c_ale=0: paroi fixe, 1 sinon
      c_ale=c_ale*mobile_coef
      
      if(lrhs.eq.1) c_ale = 0.

      IF (idir.eq.1) THEN

       iref = 2*ind_loop(2) + 1

       if(param_int(NEQ).eq.5) then

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

            l    = inddm(  i             , j,  k ) 
            ldjr = inddm(  iref - i      , j,  k )
            ldp  = indven( ind_loop(2)+1 , j,  k )
            lmtr = indmtr( ind_loop(2)+1 , j,  k )

#include     "FastS/BC/BCWallInviscid.for"
          enddo
          enddo
          enddo

       else

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

            l    = inddm(  i             , j,  k ) 
            ldjr = inddm(  iref - i      , j,  k )
            ldp  = indven( ind_loop(2)+1 , j,  k )
            lmtr = indmtr( ind_loop(2)+1 , j,  k )

#include     "FastS/BC/BCWallInviscid.for"
              rop(l,6) =rop(ldjr,6)
          enddo
          enddo
          enddo
        endif !param_int(NEQ)

      ELSEIF (idir.eq.2) THEN

       iref = 2*ind_loop(1) - 1

       if(param_int(NEQ).eq.5) then

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

              l    = inddm(  i           , j, k ) 
              ldjr = inddm(  iref - i    , j, k )
              ldp  = indven( ind_loop(1) , j, k )
              lmtr = indmtr( ind_loop(1) , j, k )
#include     "FastS/BC/BCWallInviscid.for"

          enddo
          enddo
          enddo
       else

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

              l    = inddm(  i           , j, k ) 
              ldjr = inddm(  iref - i    , j, k )
              ldp  = indven( ind_loop(1) , j, k )
              lmtr = indmtr( ind_loop(1) , j, k )
#include     "FastS/BC/BCWallInviscid.for"
              rop(l,6) =rop(ldjr,6)

          enddo
          enddo
          enddo

        endif !param_int(NEQ)


      ELSEIF (idir.eq.3) THEN

       jref = 2*ind_loop(4) + 1

       if(param_int(NEQ).eq.5) then

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

            l    = inddm( i , j             ,  k ) 
            ldjr = inddm( i , jref - j      ,  k )
            ldp  = indven(i , ind_loop(4)+1 ,  k )
            lmtr = indmtr(i , ind_loop(4)+1 ,  k )

#include     "FastS/BC/BCWallInviscid.for"

          enddo
          enddo
          enddo 
       else

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2) 

            l    = inddm( i , j             ,  k ) 
            ldjr = inddm( i , jref - j      ,  k )
            ldp  = indven(i , ind_loop(4)+1 ,  k )
            lmtr = indmtr(i , ind_loop(4)+1 ,  k )

#include     "FastS/BC/BCWallInviscid.for"
              rop(l,6) = rop(ldjr,6)
          enddo
          enddo
          enddo
        endif !param_int(NEQ)

      ELSEIF (idir.eq.4) THEN

       jref = 2*ind_loop(3) - 1

       if(param_int(NEQ).eq.5) then


          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
!DEC$ IVDEP
            do i = ind_loop(1), ind_loop(2)

              l    = inddm( i , j           ,  k ) 
              ldjr = inddm( i , jref - j    ,  k )
              ldp  = inddm( i , ind_loop(3) ,  k )
              lmtr = indmtr(i , ind_loop(3) ,  k )
#include     "FastS/BC/BCWallInviscid.for"
            enddo
          enddo
          enddo
       else

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

              l    = inddm( i , j               ,  k ) 
              ldjr = inddm( i , jref - j        ,  k )
              ldp  = indven(    i , ind_loop(3) ,  k )
              lmtr = indmtr(    i , ind_loop(3) ,  k )
#include     "FastS/BC/BCWallInviscid.for"
              rop(l,6) = rop(ldjr,6)

          enddo
          enddo
          enddo
        endif !param_int(NEQ)


      ELSEIF (idir.eq.5) THEN

       kref = 2*ind_loop(6) + 1

       if(param_int(NEQ).eq.5) then

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

            l    = inddm( i , j,  k             ) 
            ldjr = inddm( i , j,  kref - k      )
            ldp  = indven(i , j,  ind_loop(6)+1 )
            lmtr = indmtr(i , j,  ind_loop(6)+1 )
#include     "FastS/BC/BCWallInviscid.for"

          enddo
          enddo
          enddo
       else
          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

            l    = inddm( i , j,  k             ) 
            ldjr = inddm( i , j,  kref - k      )
            ldp  = indven(i , j,  ind_loop(6)+1 )
            lmtr = indmtr(i , j,  ind_loop(6)+1 )
#include    "FastS/BC/BCWallInviscid.for"
            rop(l,6) = rop(ldjr,6)

          enddo
          enddo
          enddo
        endif !param_int(NEQ)


      ELSE 

       kref = 2*ind_loop(5) - 1

       if (param_int(NEQ).eq.5) then


          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
!DEC$ IVDEP
            do i = ind_loop(1), ind_loop(2)

              l    = inddm( i , j,  k           ) 
              ldjr = inddm( i , j,  kref - k    )
              ldp  = indven(i , j,  ind_loop(5) )
              lmtr = indmtr(i , j,  ind_loop(5) )
#include     "FastS/BC/BCWallInviscid.for"

            enddo
          enddo
          enddo
       else

          do k = ind_loop(5), ind_loop(6)
          do j = ind_loop(3), ind_loop(4)
          do i = ind_loop(1), ind_loop(2)

              l    = inddm( i , j,  k           ) 
              ldjr = inddm( i , j,  kref - k    )
              ldp  = indven(i , j,  ind_loop(5) )
              lmtr = indmtr(i , j,  ind_loop(5) )
#include     "FastS/BC/BCWallInviscid.for"
              rop(l,6) = rop(ldjr,6)

          enddo
          enddo
          enddo
        endif !param_int(NEQ)

      ENDIF !idir


      END
