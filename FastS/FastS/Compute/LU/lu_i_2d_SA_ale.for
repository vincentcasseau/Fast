 
       l1  = l -inci
       lt1 = lt-inci_mtr
       lt2 = lt-inci2_mtr

       lv1 = lv-inci_ven
       lv2 = lv-inci2_ven
 
       tcx = 0.5*(ti(lt2,1)+ti(lt1,1))
       tcy = 0.5*(ti(lt2,2)+ti(lt1,2))

       r    = rop(l1,1)
       u    = rop(l1,2)
       v    = rop(l1,3)
       t    = rop(l1,5)
       q2   = .5*(u*u+v*v)
       h    = cp*t + q2
       ph2  = gamm1*q2

       qn    = tcx*u+tcy*v
 
       ue  = 0.5*(venti(lv2      )+venti(lv1      ))
       ve  = 0.5*(venti(lv2+v2ven)+venti(lv1+v2ven))
       qen = tcx*ue+tcy*ve
 
       b11=coe(l1,2)*signe -qen
       b12=tcx
       b13=tcy
       b21=(tcx*ph2-u*qn)
       b22=(qn-tcx*gam2*u)+coe(l1,2)*signe -qen
       b23=(tcy*u-tcx*gamm1*v)
       b25=tcx*gamm1
       b31=(tcy*ph2-v*qn)
       b32=(tcx*v-tcy*gamm1*u)
       b33=(qn-tcy*gam2*v)+coe(l1,2)*signe -qen
       b35=tcy*gamm1
       b51=qn*(ph2 - h)
       b52=(tcx*h-gamm1*u*qn)
       b53=(tcy*h-gamm1*v*qn)
       b55=(gam1*qn)+coe(l1,2)*signe -qen

      b6 = (qn+coe(l1,2)*signe -qen)*drodm_out(l1,6)

      b1= b11*drodm_out(l1,1)+b12*drodm_out(l1,2)+b13*drodm_out(l1,3)
      b2= b21*drodm_out(l1,1)+b22*drodm_out(l1,2)+b23*drodm_out(l1,3)
     1   +b25*drodm_out(l1,5)
      b3= b31*drodm_out(l1,1)+b32*drodm_out(l1,2)+b33*drodm_out(l1,3)
     1   +b35*drodm_out(l1,5)
      b5= b51*drodm_out(l1,1)+b52*drodm_out(l1,2)+b53*drodm_out(l1,3)
     1   +b55*drodm_out(l1,5)
