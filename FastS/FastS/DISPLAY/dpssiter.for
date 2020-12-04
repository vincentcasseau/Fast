c***********************************************************************
c     $Date: 2014-03-19 20:08:08 +0100 (mer. 19 mars 2014) $
c     $Revision: 59 $
c     $Author: IvanMary $
c***********************************************************************
      subroutine dpssiter(nitrun, neq, nssiter_loc, iflw, iles, lft,
     &   zone_name, size_name, rdm, cvg_ptr)
c***********************************************************************
c_U   USER : PECHIER
c
c     ACT
c_A    Impression et stockage des residus moyens du processus sous iteratif (L_2) 
c
c     INP
c_I    neq,ndimkt,rdmoy,rdmax
c
c     OUT
c_O    rdm: residus moyens par sous iteration / variable /domaine
c_O    cvg_ptr: pointeur residus
c***********************************************************************
c UTILISATION
c                    display ss_iteration +ndoms
c+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      implicit none
#define ALOG10 LOG10
      INTEGER_E nitrun, neq,nssiter_loc,lft,iles,iflw,size_name
      REAL_E rdm(nssiter_loc,neq,2), cvg_ptr(2*neq)

      character(len=size_name) zone_name 
c Var loc
      INTEGER_E ndm,i,ne,last_it,iverbs_loc,
     &     nitcfg,ndsdm,i_loc,itest,ii,ipass,inds
      REAL_E xro,xrou,xrov,xrow,xroe,xro1,xrou1,xrov1,xrow1,xroe1,
     &     xnut,xnut1,test,test1, cut0x
      cut0x = 1.e-30

c-----Affichage de l'iteration N+1 :
c      write(*,*) " "
c      write(*,1000) nitrun,temps

c-----Boucle sur les domaines :

      last_it = nssiter_loc
    
      iverbs_loc  = 2
      do ii = 1,neq
         if (rdm(last_it,ii,2).gt.rdm(1,ii,2)) iverbs_loc = 2
      enddo

c        i_loc = 1
c        do ii = 1, Niter_max - 1
c
c            itest = iskip_lu(Niter_max - 1, ii) + 3
c         
c            if(itest.le. last_it - 1 ) then
c 
c              it_reelle(i_loc) = ii
c              i_loc            = i_loc + 1
c            endif
c        enddo
c        it_reelle(last_it) = Niter_max

      if(lft.lt.3)then
      do 2 i=1,last_it
         
            nitcfg = i
              !nitcfg = it_reelle(i)

               !souci procedure merge sous-bloc LU
c               if(nidom_loc(nitcfg).lt.1) 
c     &       write(*,'(a18,4i5)')'WARNING dpssiter, nidom_loc=',
c     &        nidom_loc(nitcfg),nitcfg,im

           !Norme L2
           xro   = ALOG10(max(rdm(i,1,1),cut0x)) 
           xrou  = ALOG10(max(rdm(i,2,1),cut0x)) 
           xrov  = ALOG10(max(rdm(i,3,1),cut0x)) 
           xrow  = ALOG10(max(rdm(i,4,1),cut0x)) 
           xroe  = ALOG10(max(rdm(i,5,1),cut0x))
c            
c          !Norme Loo
           xro1  = ALOG10(max(rdm(i,1,2),cut0x)) 
           xrou1 = ALOG10(max(rdm(i,2,2),cut0x)) 
           xrov1 = ALOG10(max(rdm(i,3,2),cut0x)) 
           xrow1 = ALOG10(max(rdm(i,4,2),cut0x)) 
           xroe1 = ALOG10(max(rdm(i,5,2),cut0x))

           !IF(iverbs_loc.le.1) THEN

           if(i==1 .or. iverbs_loc.gt.1) then

              if(iflw.eq.3.and.iles.eq.0)  then

                xnut  = ALOG10(max(rdm(i,6,1),cut0x)) !Norme L2
                xnut1 = ALOG10(max(rdm(i,6,2),cut0x)) !Norme Loo
                if(lft.eq.0) then
                 write(*,3011)zone_name,i,xro ,xrou,xrov ,xrow,xroe,xnut
                 write(*,4011)zone_name,i,xro1,xrou1,xrov1,xrow1,xroe1,
     &                        xnut1
                else
                 write(*,3311)zone_name,i,xro,xrou,xrov,xrow,xroe ,xnut 
                 write(*,4311)zone_name,i,xro1,xrou1,xrov1,xrow1,xroe1,
     &                        xnut1
                endif
              else

               if(lft.eq.0) then
                write(*,3010)zone_name,i, xro ,xrou ,xrov ,xrow ,xroe 
                write(*,4010)zone_name,i, xro1,xrou1,xrov1,xrow1,xroe1
               else
                write(*,3310)zone_name,i, xro ,xrou ,xrov ,xrow ,xroe 
                write(*,4310)zone_name,i, xro1,xrou1,xrov1,xrow1,xroe1
               endif  !format

              endif!5/6 eq
           endif !iteration= 1


             if(i==last_it)then
              !Norme L2
              xro   = ALOG10(max(rdm(last_it,1,1),cut0x))
     &              - ALOG10(max(rdm(      1,1,1),cut0x))
              xrou  = ALOG10(max(rdm(last_it,2,1),cut0x))
     &              - ALOG10(max(rdm(      1,2,1),cut0x)) 
              xrov  = ALOG10(max(rdm(last_it,3,1),cut0x))
     &              - ALOG10(max(rdm(      1,3,1),cut0x)) 
              xrow  = ALOG10(max(rdm(last_it,4,1),cut0x)) 
     &              - ALOG10(max(rdm(      1,4,1),cut0x))
              xroe  = ALOG10(max(rdm(last_it,5,1),cut0x))
     &              - ALOG10(max(rdm(      1,5,1),cut0x))
c
              !Norme Loo
              xro1  = ALOG10(max(rdm(last_it,1,2),cut0x))
     &              - ALOG10(max(rdm(      1,1,2),cut0x))
              xrou1 = ALOG10(max(rdm(last_it,2,2),cut0x))
     &              - ALOG10(max(rdm(      1,2,2),cut0x)) 
              xrov1 = ALOG10(max(rdm(last_it,3,2),cut0x))
     &              - ALOG10(max(rdm(      1,3,2),cut0x)) 
              xrow1 = ALOG10(max(rdm(last_it,4,2),cut0x)) 
     &              - ALOG10(max(rdm(      1,4,2),cut0x))
              xroe1 = ALOG10(max(rdm(last_it,5,2),cut0x))
     &              - ALOG10(max(rdm(      1,5,2),cut0x))
           
              if(neq.eq.6) then
                 xnut  = ALOG10(max(rdm(last_it,6,1),cut0x))
     &                 - ALOG10(max(rdm(      1,6,1),cut0x))
                 xnut1 = ALOG10(max(rdm(last_it,6,2),cut0x))
     &                 - ALOG10(max(rdm(      1,6,2),cut0x))

                 if(lft.eq.0) then
                  write(*,3021)zone_name,last_it,xro,xrou,xrov,xrow,
     &                         xroe ,xnut 
                  write(*,4021)zone_name,last_it,xro1,xrou1,xrov1,
     &                         xrow1,xroe1,xnut1
                 else
                  write(*,3321)zone_name,last_it,xro,xrou,xrov,xrow,
     &                         xroe ,xnut 
                  write(*,4321)zone_name,last_it,xro1,xrou1,xrov1,
     &                         xrow1,xroe1,xnut1
                 endif

                 test =max(xro,xrou,xrov,xrow,xroe,xnut)
                 if(test.gt.0)
     &           write(*,'(a,a,a,i6,a,f12.5)')'Warning convergence
     &             L2  Newton: dom=',zone_name,
     &             ' Pas de temps=',nitrun,' divergence=',test
                 test1=max(xro1,xrou1,xrov1,xrow1,xroe1,xnut1)
                 if(test1.gt.0)
     &           write(*,'(a,a,a,i6,a,f12.5)')'Warning convergence
     &             Loo Newton: dom=',zone_name,
     &          ' Pas de temps=',nitrun,' divergence=',test1

              else !neq=5

                if(lft.eq.0) then
                write(*,3020)zone_name,last_it,xro,xrou,xrov,xrow,xroe
                write(*,4020)zone_name,last_it,xro1,xrou1,xrov1,
     &                 xrow1,xroe1
                else
                write(*,3320)zone_name,last_it,xro,xrou,xrov,xrow,xroe
                write(*,4320)zone_name,last_it,xro1,xrou1,xrov1,
     &                 xrow1,xroe1
                endif
 
                test =max(xro,xrou,xrov,xrow,xroe)
                if(test.gt.0)
     &           write(*,'(a,a,a,i6,a,f12.5)')'Warning convergence
     &             L2  Newton: dom=',zone_name,' Pas de temps=',nitrun,
     &             ' divergence=', test
                test1=max(xro1,xrou1,xrov1,xrow1,xroe1)
                if(test1.gt.0)
     &           write(*,'(a,a,a,i6,a,f12.5)')'Warning convergence
     &             Loo Newton: dom=',zone_name,' Pas de temps=',nitrun,
     &            ' divergence=',test1

              endif !neq
             endif !i=last_it

 2        continue
C
      endif
          do ne=1,neq
          cvg_ptr(ne)     = ALOG10(max(rdm(1,ne,1),cut0x))
          cvg_ptr(neq+ne) = ALOG10(max(rdm(1,ne,2),cut0x))
          enddo
C


1000  format(' Iteration: ',1x,i5,'  Temps:',1x,E10.3)
2000  format('  Zone  =',a,' / Ss-Iteration',i3)
2001  format('  Zone  =',a,' / Diff SsI 1 -',i3)

3000  format('  Residus L2 (log) : ',5(2x,f14.9))
4000  format('  Residus Loo(log) : ',5(2x,f14.9))
3001  format('  Residus L2 (log) : ',6(2x,f14.9))
4001  format('  Residus Loo(log) : ',6(2x,f14.9))
3300  format('  Residus L2 (log) : ',5(2x,f7.2))
4300  format('  Residus Loo(log) : ',5(2x,f7.2))
3301  format('  Residus L2 (log) : ',6(2x,f7.2))
4301  format('  Residus Loo(log) : ',6(2x,f7.2))

3010  format(' Res_L2 (zone=',a,', ssiter =   ',i3,')',5(2x,f14.9))
4010  format(' Res_Loo(zone=',a,', ssiter =   ',i3,')',5(2x,f14.9))
3011  format(' Res_L2 (zone=',a,', ssiter =   ',i3,')',6(2x,f14.9))
4011  format(' Res_Loo(zone=',a,', ssiter =   ',i3,')',6(2x,f14.9))
3310  format(' Res_L2 (zone=',a,', ssiter =   ',i3,')',5(2x,f7.2))
4310  format(' Res_Loo(zone=',a,', ssiter =   ',i3,')',5(2x,f7.2))
3311  format(' Res_L2 (zone=',a,', ssiter =   ',i3,')',6(2x,f7.2))
4311  format(' Res_Loo(zone=',a,', ssiter =   ',i3,')',6(2x,f7.2))

3020  format(' Res_L2 (zone=',a,', Diff Ssi 1-',i3,')',5(2x,f14.9))
4020  format(' Res_Loo(zone=',a,', Diff Ssi 1-',i3,')',5(2x,f14.9))
3021  format(' Res_L2 (zone=',a,', Diff Ssi 1-',i3,')',6(2x,f14.9))
4021  format(' Res_Loo(zone=',a,', Diff Ssi 1-',i3,')',6(2x,f14.9))
3320  format(' Res_L2 (zone=',a,', Diff Ssi 1-',i3,')',5(2x,f7.2))
4320  format(' Res_Loo(zone=',a,', Diff Ssi 1-',i3,')',5(2x,f7.2))
3321  format(' Res_L2 (zone=',a,', Diff Ssi 1-',i3,')',6(2x,f7.2))
4321  format(' Res_Loo(zone=',a,', Diff Ssi 1-',i3,')',6(2x,f7.2))
 
      end
