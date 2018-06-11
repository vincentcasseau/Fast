C        Generated by TAPENADE     (INRIA, Ecuador team)
C  Tapenade 3.13 (r6666M) -  1 Mar 2018 15:30
C
C  Differentiation of bflwall in forward (tangent) mode:
C   variations   of useful results: drodm
C   with respect to varying inputs: rop drodm
      SUBROUTINE BFLWALL_D(ndom, idir, mobile_coef, neq_mtr, param_int, 
     +                     param_real, incijk, ind_loop, rop, ropd, 
     +                     drodm, drodmd, tijk, ventijk)
      IMPLICIT NONE
C
C
C
C
C
C
      INTEGER*4 ndom, neq_mtr, incijk, idir, ind_loop(6), param_int(0:*)
C
      REAL*8 rop(param_int(41)*param_int(36))
      REAL*8 ropd(param_int(41)*param_int(36))
      REAL*8 drodm(param_int(41)*param_int(36))
      REAL*8 drodmd(param_int(41)*param_int(36))
      REAL*8 ventijk(param_int(44)*param_int(40))
C
      REAL*8 tijk(param_int(43)*param_int(37))
C
      REAL*8 param_real(0:*), mobile_coef
C
C var loc
      INTEGER*4 im, jm, km, ijkm, l, l0, iadrf, i, j, k, lj, ic, jc, kc
     +          , kc_vent, v1, v2, v3, v4, v5, v6, vmtr, vven, shift, lt
     +          , lven, lij, ltij, lvij
C
      REAL*8 p, r, u, v, w, qen, ci_mtr, cj_mtr, ck_mtr, ck_vent, c_ale
     +       , ck_mtr_vent, u_int, sens, rgp, flu1, flu2, flu3, flu4, 
     +       flu5, flu6, tcx, tcy, tcz
      REAL*8 pd, rd, ud, vd, wd, u_intd, flu2d, flu3d, flu4d, flu5d
C    adresse point courant pour tableau de la taille d'un domaine 
      INTEGER*4 inddm, i_1, j_1, k_1
C    adresse interface pour tableau metric
      INTEGER*4 indmtr, i_3, j_3, k_3
C    adresse interface pour tableau vitesse entrainement
      INTEGER*4 indven, i_4, j_4, k_4
      INTRINSIC MOD
      EXTERNAL SHAPE_TAB_MTR
C
CCv(gama-1)= R (gas parfait)
      rgp = param_real(2)*(param_real(1)-1.)
C
      v1 = 0
      v2 = param_int(41)
      v3 = 2*param_int(41)
      v4 = 3*param_int(41)
      v5 = 4*param_int(41)
      v6 = 5*param_int(41)
C
      vmtr = param_int(43)
      vven = param_int(44)
C
      sens = 1.
      shift = 0
      IF (MOD(idir, 2) .EQ. 0) THEN
        sens = -1.
        shift = 1
      END IF
C
C!  a mettre dans Fast
      shift = incijk*shift
C
      CALL SHAPE_TAB_MTR(neq_mtr, param_int, idir, ic, jc, kc, kc_vent, 
     +                   ci_mtr, cj_mtr, ck_mtr, ck_vent, c_ale)
C
Ccorrection monoindice
      c_ale = c_ale*mobile_coef
C
C
      ic = ic - 1
      jc = jc - 1
      kc = kc - 1
      kc_vent = kc_vent - 1
C
      IF (param_int(36) .EQ. 5) THEN
C
        DO k=ind_loop(5),ind_loop(6)
          DO j=ind_loop(3),ind_loop(4)
            lij = 1 + (ind_loop(1)+param_int(0+3)-1) + (j+param_int(0+3)
     +        -1)*param_int(0) + (k+param_int(0+4)-1)*param_int(0)*
     +        param_int(0+1) - 1
            ltij = lij - (1+(ind_loop(1)+param_int(5+3)-1)*param_int(5)+
     +        (j+param_int(5+3)-1)*param_int(5+1)+(k+param_int(5+4)-1)*
     +        param_int(5+2)) + 1
            lvij = lij - (1+(ind_loop(1)+param_int(15+3)-1)*param_int(15
     +        )+(j+param_int(15+3)-1)*param_int(15+1)+(k+param_int(15+4)
     +        -1)*param_int(15+2)) + 1
CC    !DIR$ ASSUME (mod(lij,4) .eq. 0)
CDIR$ IVDEP
            DO l=lij+1,lij+1+ind_loop(2)-ind_loop(1)
C
              lt = l - ltij
              lven = l - lvij
C
              iadrf = l - incijk
              l0 = l - shift
C
              tcx = tijk(lt+vmtr*ic)*ci_mtr
              tcy = tijk(lt+vmtr*jc)*cj_mtr
              tcz = tijk(lt+vmtr*kc)*ck_mtr
C
              qen = (ventijk(lven)*tcx+ventijk(lven+vven)*tcy+ventijk(
     +          lven+vven*kc_vent)*tcz*ck_vent)*c_ale
C
              rd = 0.5*(ropd(l+v1)+ropd(iadrf+v1))
              r = 0.5*(rop(l+v1)+rop(iadrf+v1))
              ud = 0.5*(ropd(l+v2)+ropd(iadrf+v2))
              u = 0.5*(rop(l+v2)+rop(iadrf+v2))
              vd = 0.5*(ropd(l+v3)+ropd(iadrf+v3))
              v = 0.5*(rop(l+v3)+rop(iadrf+v3))
              wd = 0.5*(ropd(l+v4)+ropd(iadrf+v4))
              w = 0.5*(rop(l+v4)+rop(iadrf+v4))
C
Cdetermination vitesse normale interface
              pd = 0.5*rgp*(ropd(l+v5)*rop(l+v1)+rop(l+v5)*ropd(l+v1)+
     +          ropd(iadrf+v5)*rop(iadrf+v1)+rop(iadrf+v5)*ropd(iadrf+v1
     +          ))
              p = 0.5*(rop(l+v5)*rop(l+v1)+rop(iadrf+v5)*rop(iadrf+v1))*
     +          rgp
              u_intd = tcx*ud + tcy*vd + tcz*wd
              u_int = tcx*u + tcy*v + tcz*w - qen
C
              flu1 = 0.
              flu2d = tcx*pd + (u_intd*u+u_int*ud)*r + u_int*u*rd
              flu2 = tcx*p + u_int*u*r
              flu3d = tcy*pd + (u_intd*v+u_int*vd)*r + u_int*v*rd
              flu3 = tcy*p + u_int*v*r
              flu4d = tcz*pd + (u_intd*w+u_int*wd)*r + u_int*w*rd
              flu4 = tcz*p + u_int*w*r
              flu5d = qen*pd
              flu5 = p*qen
              drodm(l0+v1) = drodm(l0+v1) + flu1*sens
              drodmd(l0+v2) = drodmd(l0+v2) + sens*flu2d
              drodm(l0+v2) = drodm(l0+v2) + flu2*sens
              drodmd(l0+v3) = drodmd(l0+v3) + sens*flu3d
              drodm(l0+v3) = drodm(l0+v3) + flu3*sens
              drodmd(l0+v4) = drodmd(l0+v4) + sens*flu4d
              drodm(l0+v4) = drodm(l0+v4) + flu4*sens
              drodmd(l0+v5) = drodmd(l0+v5) + sens*flu5d
              drodm(l0+v5) = drodm(l0+v5) + flu5*sens
            ENDDO
          ENDDO
        ENDDO
      ELSE
C
        DO k=ind_loop(5),ind_loop(6)
          DO j=ind_loop(3),ind_loop(4)
            lij = 1 + (ind_loop(1)+param_int(0+3)-1) + (j+param_int(0+3)
     +        -1)*param_int(0) + (k+param_int(0+4)-1)*param_int(0)*
     +        param_int(0+1) - 1
            ltij = lij - (1+(ind_loop(1)+param_int(5+3)-1)*param_int(5)+
     +        (j+param_int(5+3)-1)*param_int(5+1)+(k+param_int(5+4)-1)*
     +        param_int(5+2)) + 1
            lvij = lij - (1+(ind_loop(1)+param_int(15+3)-1)*param_int(15
     +        )+(j+param_int(15+3)-1)*param_int(15+1)+(k+param_int(15+4)
     +        -1)*param_int(15+2)) + 1
CC    !DIR$ ASSUME (mod(lij,4) .eq. 0)
CDIR$ IVDEP
            DO l=lij+1,lij+1+ind_loop(2)-ind_loop(1)
C
              lt = l - ltij
              lven = l - lvij
C
              iadrf = l - incijk
              l0 = l - shift
C
              tcx = tijk(lt+vmtr*ic)*ci_mtr
              tcy = tijk(lt+vmtr*jc)*cj_mtr
              tcz = tijk(lt+vmtr*kc)*ck_mtr
C
              qen = (ventijk(lven)*tcx+ventijk(lven+vven)*tcy+ventijk(
     +          lven+vven*kc_vent)*tcz*ck_vent)*c_ale
C
              rd = 0.5*(ropd(l+v1)+ropd(iadrf+v1))
              r = 0.5*(rop(l+v1)+rop(iadrf+v1))
              ud = 0.5*(ropd(l+v2)+ropd(iadrf+v2))
              u = 0.5*(rop(l+v2)+rop(iadrf+v2))
              vd = 0.5*(ropd(l+v3)+ropd(iadrf+v3))
              v = 0.5*(rop(l+v3)+rop(iadrf+v3))
              wd = 0.5*(ropd(l+v4)+ropd(iadrf+v4))
              w = 0.5*(rop(l+v4)+rop(iadrf+v4))
C
Cdetermination vitesse normale interface
              pd = 0.5*rgp*(ropd(l+v5)*rop(l+v1)+rop(l+v5)*ropd(l+v1)+
     +          ropd(iadrf+v5)*rop(iadrf+v1)+rop(iadrf+v5)*ropd(iadrf+v1
     +          ))
              p = 0.5*(rop(l+v5)*rop(l+v1)+rop(iadrf+v5)*rop(iadrf+v1))*
     +          rgp
C
Cp = p-r*sqrt(param_real(1)*rgp*rop(l+v5))*u_int
              u_intd = tcx*ud + tcy*vd + tcz*wd
              u_int = tcx*u + tcy*v + tcz*w - qen
C
              flu1 = 0.
              flu2d = tcx*pd + (u_intd*u+u_int*ud)*r + u_int*u*rd
              flu2 = tcx*p + u_int*u*r
              flu3d = tcy*pd + (u_intd*v+u_int*vd)*r + u_int*v*rd
              flu3 = tcy*p + u_int*v*r
              flu4d = tcz*pd + (u_intd*w+u_int*wd)*r + u_int*w*rd
              flu4 = tcz*p + u_int*w*r
              flu5d = qen*pd
              flu5 = p*qen
              flu6 = 0.
              drodm(l0+v1) = drodm(l0+v1) + flu1*sens
              drodmd(l0+v2) = drodmd(l0+v2) + sens*flu2d
              drodm(l0+v2) = drodm(l0+v2) + flu2*sens
              drodmd(l0+v3) = drodmd(l0+v3) + sens*flu3d
              drodm(l0+v3) = drodm(l0+v3) + flu3*sens
              drodmd(l0+v4) = drodmd(l0+v4) + sens*flu4d
              drodm(l0+v4) = drodm(l0+v4) + flu4*sens
              drodmd(l0+v5) = drodmd(l0+v5) + sens*flu5d
              drodm(l0+v5) = drodm(l0+v5) + flu5*sens
              drodm(l0+v6) = drodm(l0+v6) + flu6*sens
            ENDDO
          ENDDO
        ENDDO
      END IF
      END
