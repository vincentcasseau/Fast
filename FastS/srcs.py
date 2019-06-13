#==============================================================================
# Fichiers C++
#==============================================================================
cpp_srcs = ['FastS/Metric/allocate_metric.cpp',
            'FastS/Compute/LU/allocate_ssor.cpp',
            'FastS/Metric/init_metric.cpp',
            'FastS/Init/cart.cpp',
            'FastS/Init/initVars.cpp',
            'FastS/Init/initNuma.cpp',
            'FastS/Init/itt.cpp',
            'FastS/Init/computePT_velocity_ale.cpp',
            'FastS/Compute/computePT.cpp',
            'FastS/Compute/gsdr3.cpp',
            'FastS/Compute/souszones_list.cpp',
            'FastS/Compute/DTLOC/souszones_list2.cpp',
            'FastS/Compute/DTLOC/souszones_list3.cpp',
            'FastS/Compute/DTLOC/stockrecup.cpp',
            'FastS/Compute/DTLOC/recup.cpp',
            'FastS/Compute/DTLOC/recup2.cpp',
            'FastS/Compute/DTLOC/recup3.cpp',
            'FastS/Compute/DTLOC/recup3para.cpp',
            'FastS/Compute/DTLOC/recup3para_.cpp',
            'FastS/Compute/DTLOC/recup3para_mpi.cpp',
            'FastS/Compute/DTLOC/dtlocal.cpp',
            'FastS/Compute/DTLOC/dtlocal2.cpp',
            'FastS/Compute/DTLOC/dtlocal2para.cpp',
            'FastS/Compute/DTLOC/dtlocal2para_.cpp',
            'FastS/Compute/DTLOC/dtlocal2para_mpi.cpp',
            'FastS/Compute/DTLOC/dtlocal2para_c.cpp',
            'FastS/Compute/DTLOC/BC_local.cpp',
            'FastS/Compute/DTLOC/recup3para_c.cpp',
            'FastS/Compute/DTLOC/prep_cfl.cpp',
            'FastS/Compute/DTLOC/decoupe_maillage.cpp',
            'FastS/Compute/getbcfromzone.cpp',
            'FastS/BC/applyBC.cpp',
            'FastS/BC/BCzone.cpp',
            'FastS/BC/BCzone_d.cpp',
            'FastS/BC/compute_effort.cpp',
            'FastS/DISPLAY/display_ss_iteration.cpp',
            'FastS/Compute/ALE/movegrid.cpp',
            'FastS/Compute/LES/computePT_mut.cpp',
            'FastS/POST/computePT_enstrophy.cpp',
            'FastS/POST/computePT_variables.cpp',
            'FastS/POST/computePT_gradient.cpp',
            'FastS/HPC_LAYER/work_thread_distribution.cpp',
            'FastS/HPC_LAYER/distributeThreads.cpp',
            'FastS/Compute/Linear_solver/matvec.cpp',
            'FastS/Compute/Linear_solver/matvecPT.cpp',
            'FastS/ADJOINT/compute_dpJ_dpW.cpp',
            'FastS/Com/setInterpTransfersFastS.cpp',
            #'FastS/ADJOINT/compute_RhsIterAdjoint.cpp',
            #'FastS/ADJOINT/rhs_Iter_Adj.cpp',
            #'FastS/ADJOINT/TAPENADE_FUNCTIONS/adStack.c',
            'FastS/stretch.cpp',
            'FastS/testlinlets.cpp',
            'FastS/STAT/computePT_my.cpp']

#==============================================================================
# Fichiers fortran
#==============================================================================
for_srcs = ['FastS/StretchF.for',
            'FastS/Metric/skmtr.for',
            'FastS/Metric/tijk_extrap.for',
            'FastS/Metric/dist_extrap.for',
            'FastS/Metric/skmtr_df.for',
            'FastS/Metric/derdf_xyz.for',
            'FastS/Metric/error.for',
            'FastS/Metric/cp_tijk.for',
            'FastS/Metric/cp_vol.for',
            'FastS/Metric/nature_geom_dom.for',
            'FastS/Metric/move.for',
            'FastS/Metric/cptijk_ale.for',
            'FastS/Metric/cpventijk_ale.for',
            'FastS/Init/copynuma.for',
            'FastS/Init/init_ventijk.for',
            'FastS/STAT/cpmys_rij.for',
            'FastS/POST/Q_1rot/cp_qprime_1rot_3dfull.for',
            'FastS/POST/Q_1rot/cp_qprime_1rot_3dhomo.for',
            'FastS/POST/Q_1rot/cp_qprime_1rot_3dcart.for',
            'FastS/POST/Q_1rot/cp_qprime_1rot_2d.for',
            'FastS/POST/Q_Enst/cp_q_enst_3dfull.for',
            'FastS/POST/Q_Enst/cp_q_enst_3dhomo.for',
            'FastS/POST/Q_Enst/cp_q_enst_3dcart.for',
            'FastS/POST/Q_Enst/cp_q_enst_2d.for',
            'FastS/POST/QCriterion/cp_qprime_3dfull.for',
            'FastS/POST/QCriterion/cp_qprime_3dhomo.for',
            'FastS/POST/QCriterion/cp_qprime_3dcart.for',
            'FastS/POST/QCriterion/cp_qprime_2d.for',
            'FastS/POST/QCriterion/cp_q_3dfull.for',
            'FastS/POST/QCriterion/cp_q_3dhomo.for',
            'FastS/POST/QCriterion/cp_q_3dcart.for',
            'FastS/POST/QCriterion/cp_q_2d.for',
            'FastS/POST/Gradvar/cp_gradvar_3dfull.for',
            'FastS/POST/Gradvar/cp_gradvar_3dhomo.for',
            'FastS/POST/Gradvar/cp_gradvar_3dcart.for',
            'FastS/POST/Gradvar/cp_gradvar_2d.for',
            'FastS/POST/Enstrophy/cp_enst_3dfull.for',
            'FastS/POST/Enstrophy/cp_enst_3dhomo.for',
            'FastS/POST/Enstrophy/cp_enst_3dcart.for',
            'FastS/POST/Enstrophy/cp_enst_2d.for',
            'FastS/POST/extrap.for',
            'FastS/POST/cp_gradu.for',
            'FastS/POST/cp_gradu_2d.for',
            'FastS/POST/cp_gradu_3dcart.for',
            'FastS/POST/cp_gradu_3dhomo.for',
            'FastS/POST/cp_gradu_3dfull.for',
            'FastS/POST/cptaylor.for',
            'FastS/POST/post.for',
            'FastS/POST/post_qprime_1rot.for',
            'FastS/POST/post_qprime.for',
            'FastS/POST/post_q.for',
            'FastS/POST/post_q_enst.for',
            'FastS/POST/post_enst.for',
            'FastS/POST/post_grad.for',
            'FastS/POST/post_drodt.for',
            'FastS/HPC_LAYER/indice_boucle_ssdom.for',
            'FastS/HPC_LAYER/indice_boucle_lu.for',
            'FastS/HPC_LAYER/indice_boucle_scater.for',
            'FastS/HPC_LAYER/crsdm.for',
            'FastS/HPC_LAYER/crsdm_scater.for',
            'FastS/HPC_LAYER/synchro_omp_scater.for',
            'FastS/HPC_LAYER/topo_scater.for',
            'FastS/HPC_LAYER/verrou.for',
            'FastS/HPC_LAYER/flush_integer.for',
            'FastS/HPC_LAYER/flush_real.for',
            'FastS/DISPLAY/dpssiter.for',
            'FastS/DISPLAY/Conv2Pytree.for',
            'FastS/BC/indice_cl_sdm.for',
            'FastS/BC/bvbs_extrapolate.for',
            'FastS/BC/bvbs_extrapolate_d.for',
            'FastS/BC/bvbs_periodique.for',
            'FastS/BC/bvbs_periodique_d.for',
            'FastS/BC/bvbs_periodique_azimuthal.for',
            'FastS/BC/bvbs_periodique_azimuthal_d.for',
            'FastS/BC/bvbs_wall_viscous_transition.for',
            'FastS/BC/bvbs_wall_viscous_transition_d.for',
            'FastS/BC/bvbs_wall_viscous_adia.for',
            'FastS/BC/bvbs_wall_viscous_adia_d.for',
            'FastS/BC/bvbs_wall_inviscid.for',
            'FastS/BC/bvbs_wall_inviscid_d.for',
            'FastS/BC/bvbs_inflow_supersonic.for',
            'FastS/BC/bvbs_inflow_supersonic_d.for',
            'FastS/BC/bvbs_farfield.for',
            'FastS/BC/bvbs_farfield_d.for',
            'FastS/BC/bvbs_outflow.for',
            'FastS/BC/bvbs_outflow_d.for',
            'FastS/BC/bvbs_outpres.for',
            'FastS/BC/bvbs_outpres_d.for',
#            'FastS/BC/bvbs_updatepressure.for',
            'FastS/BC/bvbs_inflow.for',
            'FastS/BC/bvbs_inflow_d.for',
            'FastS/BC/bvbs_inflow_fich.for',
            'FastS/BC/bvbs_inflow_fich_d.for',
            'FastS/BC/bvbs_inflow_newton.for',
            'FastS/BC/bvbs_inflow_newton_d.for',
            'FastS/BC/correct_coins.for',
            'FastS/BC/bceffort.for',
            'FastS/BC/bfl3.for',
            'FastS/BC/bflwall.for',
            'FastS/BC/bflwallslip.for',
            'FastS/BC/bflinj1.for',
            'FastS/Compute/skip_lu.for',
            'FastS/Compute/ssdom_lu_ijk.for',
            'FastS/Compute/navier_stokes_struct.for',
            'FastS/Compute/ALE/mjr_ale.for',
            'FastS/Compute/ALE/mjr_ale_3dhomocart.for',
            'FastS/Compute/ALE/mjrtijk_3dfull.for',
            'FastS/Compute/ALE/mjrtijk_2d.for',
            'FastS/Compute/ALE/mjrvent_3dfull.for',
            'FastS/Compute/ALE/mjrvent_2d.for',
            'FastS/Compute/ALE/move_domx.for',
            'FastS/Compute/ALE/spsource_MEANFLOW.for',
            'FastS/Compute/LES/viles.for',
            'FastS/Compute/LES/lesvist.for',
            'FastS/Compute/LES/cp_rot_sij.for',
            'FastS/Compute/LES/mcmvi.for',
            'FastS/Compute/LES/extrap_mut.for',
            'FastS/Compute/shape_tab_mtr.for',
            'FastS/Compute/init_rhs.for',
            'FastS/Compute/init_rhs_dtloc.for',
            'FastS/Compute/init_tab.for',
            'FastS/Compute/invist.for',
            'FastS/Compute/cptst3.for',
            'FastS/Compute/tstb3c.for',
            'FastS/Compute/tstb3_impli.for',
            'FastS/Compute/tstb3_impli_chimer.for',
            'FastS/Compute/tstb3_expli.for',
            'FastS/Compute/tstb3_expli_chimer.for',
            'FastS/Compute/tstb3_global.for',
            'FastS/Compute/cpcfl3.for',
            'FastS/Compute/ibcsource.for',
            'FastS/Compute/src_term.for',
            'FastS/Compute/src_term_d.for',
            'FastS/Compute/update_src.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_lamin_minmod_3dfull.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_lamin_minmod_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_lamin_minmod_2d.for',
            'FastS/Compute/ROE/2d/corr_fluroe_lamin_minmod_2d_d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_lamin_o3_3dfull.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_lamin_o3_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_lamin_o3_2d.for',
            'FastS/Compute/ROE/2d/corr_fluroe_lamin_o3_2d_d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_lamin_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_lamin_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_lamin_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_lamin_o3_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_SA_o3_3dfull.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_SA_o3_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_SA_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_SA_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_SA_o3_2d.for',
            'FastS/Compute/ROE/2d/corr_fluroe_SA_o3_2d_d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_euler_o3_3dfull.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_euler_o3_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_euler_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_euler_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_euler_o3_2d.for',
            'FastS/Compute/ROE/2d/corr_fluroe_euler_o3_2d_d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_SA_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_SA_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_SA_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_SA_o3_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_euler_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_euler_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_euler_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_euler_o3_2d.for',
            'FastS/Compute/ROE/3dfull/eff_fluroe_lamin_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/eff_fluroe_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/eff_fluroe_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/eff_fluroe_lamin_o3_2d.for',
            'FastS/Compute/ROE/3dfull/eff_fluroe_euler_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/eff_fluroe_euler_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/eff_fluroe_euler_o3_3dcart.for',
            'FastS/Compute/ROE/2d/eff_fluroe_euler_o3_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_lamin_o3_3dfull.for',
            'FastS/Compute/ROE/3dfull/fluroe_lamin_o3_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/fluroe_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_lamin_o3_2d.for',
            'FastS/Compute/ROE/2d/fluroe_lamin_o3_2d_d.for',
            'FastS/Compute/ROE/3dfull/fluroe_SA_o3_3dfull.for',
            'FastS/Compute/ROE/3dfull/fluroe_SA_o3_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/fluroe_SA_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_SA_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_SA_o3_2d.for',
            'FastS/Compute/ROE/2d/fluroe_SA_o3_2d_d.for',
            'FastS/Compute/ROE/3dfull/fluroe_euler_o3_3dfull.for',
            'FastS/Compute/ROE/3dfull/fluroe_euler_o3_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/fluroe_euler_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_euler_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_euler_o3_2d.for',
            'FastS/Compute/ROE/2d/fluroe_euler_o3_2d_d.for',
            'FastS/Compute/ROE/3dfull/fluroe_ale_lamin_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_ale_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_ale_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_ale_lamin_o3_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_ale_SA_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_ale_SA_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_ale_SA_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_ale_SA_o3_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_ale_euler_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_ale_euler_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_ale_euler_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_ale_euler_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/3dfull/eff_flusenseur_init_lamin_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/eff_flusenseur_init_lamin_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/eff_flusenseur_init_lamin_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/eff_flusenseur_init_lamin_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/3dfull/eff_flusenseur_init_euler_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/eff_flusenseur_init_euler_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/eff_flusenseur_init_euler_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/eff_flusenseur_init_euler_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/effort_flusenseur_init_select.for',
            'FastS/Compute/SENSOR_INIT/3dfull/flusenseur_init_lamin_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/flusenseur_init_lamin_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/flusenseur_init_lamin_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/flusenseur_init_lamin_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/3dfull/flusenseur_init_SA_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/flusenseur_init_SA_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/flusenseur_init_SA_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/flusenseur_init_SA_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/3dfull/flusenseur_init_euler_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/flusenseur_init_euler_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/flusenseur_init_euler_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/flusenseur_init_euler_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/3dfull/flusenseur_init_ale_lamin_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/flusenseur_init_ale_lamin_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/flusenseur_init_ale_lamin_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/flusenseur_init_ale_lamin_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/3dfull/flusenseur_init_ale_SA_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/flusenseur_init_ale_SA_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/flusenseur_init_ale_SA_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/flusenseur_init_ale_SA_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/3dfull/flusenseur_init_ale_euler_o3_3dfull.for',
            'FastS/Compute/SENSOR_INIT/3dhomo/flusenseur_init_ale_euler_o3_3dhomo.for',
            'FastS/Compute/SENSOR_INIT/3dcart/flusenseur_init_ale_euler_o3_3dcart.for',
            'FastS/Compute/SENSOR_INIT/2d/flusenseur_init_ale_euler_o3_2d.for',
            'FastS/Compute/SENSOR_INIT/flusenseur_init_select.for',
            'FastS/Compute/SENSOR/3dfull/flusenseur_lamin_o3_3dfull.for',
            'FastS/Compute/SENSOR/3dhomo/flusenseur_lamin_o3_3dhomo.for',
            'FastS/Compute/SENSOR/3dcart/flusenseur_lamin_o3_3dcart.for',
            'FastS/Compute/SENSOR/2d/flusenseur_lamin_o3_2d.for',
            'FastS/Compute/SENSOR/3dfull/flusenseur_SA_o3_3dfull.for',
            'FastS/Compute/SENSOR/3dhomo/flusenseur_SA_o3_3dhomo.for',
            'FastS/Compute/SENSOR/3dcart/flusenseur_SA_o3_3dcart.for',
            'FastS/Compute/SENSOR/2d/flusenseur_SA_o3_2d.for',
            'FastS/Compute/SENSOR/3dfull/flusenseur_euler_o3_3dfull.for',
            'FastS/Compute/SENSOR/3dhomo/flusenseur_euler_o3_3dhomo.for',
            'FastS/Compute/SENSOR/3dcart/flusenseur_euler_o3_3dcart.for',
            'FastS/Compute/SENSOR/2d/flusenseur_euler_o3_2d.for',
            'FastS/Compute/SENSOR/3dfull/flusenseur_ale_lamin_o3_3dfull.for',
            'FastS/Compute/SENSOR/3dhomo/flusenseur_ale_lamin_o3_3dhomo.for',
            'FastS/Compute/SENSOR/3dcart/flusenseur_ale_lamin_o3_3dcart.for',
            'FastS/Compute/SENSOR/2d/flusenseur_ale_lamin_o3_2d.for',
            'FastS/Compute/SENSOR/3dfull/flusenseur_ale_SA_o3_3dfull.for',
            'FastS/Compute/SENSOR/3dhomo/flusenseur_ale_SA_o3_3dhomo.for',
            'FastS/Compute/SENSOR/3dcart/flusenseur_ale_SA_o3_3dcart.for',
            'FastS/Compute/SENSOR/2d/flusenseur_ale_SA_o3_2d.for',
            'FastS/Compute/SENSOR/3dfull/flusenseur_ale_euler_o3_3dfull.for',
            'FastS/Compute/SENSOR/3dhomo/flusenseur_ale_euler_o3_3dhomo.for',
            'FastS/Compute/SENSOR/3dcart/flusenseur_ale_euler_o3_3dcart.for',
            'FastS/Compute/SENSOR/2d/flusenseur_ale_euler_o3_2d.for',
            'FastS/Compute/SENSOR/flusenseur_select.for',
            'FastS/Compute/AUSM/3dfull/eff_fluausm_lamin_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/eff_fluausm_lamin_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/eff_fluausm_lamin_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/eff_fluausm_lamin_o3_2d.for',
            'FastS/Compute/AUSM/3dfull/eff_fluausm_euler_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/eff_fluausm_euler_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/eff_fluausm_euler_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/eff_fluausm_euler_o3_2d.for',
            'FastS/Compute/AUSM/effort_fluausm_select.for',
            'FastS/Compute/AUSM/3dfull/fluausm_lamin_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_lamin_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_lamin_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_lamin_o3_2d.for',
            'FastS/Compute/AUSM/2d/fluausm_lamin_o3_2d_d.for',
            'FastS/Compute/AUSM/3dfull/fluausm_SA_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_SA_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_SA_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_SA_o3_2d.for',
            'FastS/Compute/AUSM/2d/fluausm_SA_o3_2d_d.for',
            'FastS/Compute/AUSM/3dfull/fluausm_euler_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_euler_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_euler_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_euler_o3_2d.for',
            'FastS/Compute/AUSM/2d/fluausm_euler_o3_2d_d.for',
            'FastS/Compute/AUSM/3dfull/fluausm_ale_lamin_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_ale_lamin_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_ale_lamin_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_ale_lamin_o3_2d.for',
            'FastS/Compute/AUSM/3dfull/fluausm_ale_SA_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_ale_SA_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_ale_SA_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_ale_SA_o3_2d.for',
            'FastS/Compute/AUSM/3dfull/fluausm_ale_euler_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_ale_euler_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_ale_euler_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_ale_euler_o3_2d.for',
            'FastS/Compute/AUSM/fluausm_select.for',
            'FastS/Compute/AUSM/fluausm_select_d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_SA_minmod_3dfull.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_SA_minmod_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_SA_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_SA_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_SA_minmod_2d.for',
            'FastS/Compute/ROE/2d/corr_fluroe_SA_minmod_2d_d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_euler_minmod_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_euler_minmod_2d.for',
            'FastS/Compute/ROE/2d/corr_fluroe_euler_minmod_2d_d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_SA_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_SA_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_SA_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_SA_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_euler_minmod_2d.for',
            'FastS/Compute/ROE/correction_fluroe_select.for',
            'FastS/Compute/ROE/correction_fluroe_select_d.for',
            'FastS/Compute/ROE/3dfull/eff_fluroe_lamin_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/eff_fluroe_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/eff_fluroe_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/eff_fluroe_lamin_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/eff_fluroe_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/eff_fluroe_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/eff_fluroe_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/eff_fluroe_euler_minmod_2d.for',
            'FastS/Compute/ROE/effort_fluroe_select.for',
            'FastS/Compute/ROE/3dfull/fluroe_lamin_minmod_3dfull.for',
            'FastS/Compute/ROE/3dfull/fluroe_lamin_minmod_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/fluroe_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_lamin_minmod_2d.for',
            'FastS/Compute/ROE/2d/fluroe_lamin_minmod_2d_d.for',
            'FastS/Compute/ROE/3dfull/fluroe_SA_minmod_3dfull.for',
            'FastS/Compute/ROE/3dfull/fluroe_SA_minmod_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/fluroe_SA_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_SA_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_SA_minmod_2d.for',
            'FastS/Compute/ROE/2d/fluroe_SA_minmod_2d_d.for',
            'FastS/Compute/ROE/3dfull/fluroe_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dfull/fluroe_euler_minmod_3dfull_d.for',
            'FastS/Compute/ROE/3dhomo/fluroe_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_euler_minmod_2d.for',
            'FastS/Compute/ROE/2d/fluroe_euler_minmod_2d_d.for',
            'FastS/Compute/ROE/3dfull/fluroe_ale_lamin_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_ale_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_ale_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_ale_lamin_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_ale_SA_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_ale_SA_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_ale_SA_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_ale_SA_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_ale_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_ale_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_ale_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_ale_euler_minmod_2d.for',
            'FastS/Compute/ROE/fluroe_select.for',
            'FastS/Compute/ROE/fluroe_select_d.for',
            'FastS/Compute/SA/vispalart.for',
            'FastS/Compute/SA/vispalart_d.for',
            'FastS/Compute/SA/viszdes_izgris0.for',
            'FastS/Compute/SA/spsource_SA.for',
            'FastS/Compute/SA/spsource_SA_d.for',
            'FastS/Compute/SA/spsource_SA_diff.for',
            'FastS/Compute/SA/spsource_SA_diff_d.for',
            'FastS/Compute/SA/spsource_SA_comp.for',
            'FastS/Compute/SA/spsource_SA_comp_d.for',
            'FastS/Compute/SA/spsource_ZDES2_vol_debug.for',
            'FastS/Compute/SA/spsource_ZDES2_rot_debug.for',
            'FastS/Compute/SA/spsource_ZDES1_vol_debug.for',
            'FastS/Compute/SA/spsource_ZDES1_rot_debug.for',
            'FastS/Compute/SA/spsource_ZDES3_vol_debug.for',
            'FastS/Compute/SA/spsource_ZDES3_rot_debug.for',
            'FastS/Compute/SA/spsource_ZDES2_vol.for',
            'FastS/Compute/SA/spsource_ZDES2_rot.for',
            'FastS/Compute/SA/spsource_ZDES1_vol.for',
            'FastS/Compute/SA/spsource_ZDES1_rot.for',
            'FastS/Compute/SA/spsource_ZDES3_vol.for',
            'FastS/Compute/SA/spsource_ZDES3_rot.for',
            'FastS/Compute/ac_pulse.for',
            'FastS/Compute/core3ark3.for',
            'FastS/Compute/core3_dtloc.for',
            'FastS/Compute/core3as2.for',
            'FastS/Compute/core3as2_chim.for',
            'FastS/Compute/core3as2_kry.for',
            'FastS/Compute/core3as2_chim_kry.for',
            'FastS/Compute/Linear_solver/dp_dw_vect.for',
            'FastS/Compute/Linear_solver/id_vect.for',
            'FastS/Compute/Linear_solver/scal_prod.for',
            'FastS/Compute/Linear_solver/vect_rvect.for',
            'FastS/Compute/Linear_solver/prod_mat_vect.for',
            'FastS/Compute/Linear_solver/normalisation_vect.for',
            'FastS/Compute/Linear_solver/norm_vect.for',
            'FastS/Compute/Linear_solver/mjr_prim_from_cons.for',
            'FastS/Compute/Linear_solver/pre_bc.for',
            'FastS/Compute/Linear_solver/navier_stokes_struct_d.for',
            'FastS/Compute/Linear_solver/bfl3_d.for',
            'FastS/Compute/Linear_solver/bflwall_d.for',
            'FastS/Compute/Linear_solver/core3as2_kry_d.for',
            'FastS/Compute/sfd.for',
            'FastS/Compute/extract_res.for',
            'FastS/Compute/init_ssiter_bloc.for',
            'FastS/Compute/cprdu3s1.for',
            'FastS/Compute/DTLOC/cplevel.for',
            'FastS/Compute/DTLOC/copy.for',
            'FastS/Compute/DTLOC/copyrk3local.for',
            'FastS/Compute/DTLOC/copy_rk3local.for',
            'FastS/Compute/DTLOC/copy_rk3localpara.for',
            'FastS/Compute/DTLOC/extrap_rk3localpara.for',
            'FastS/Compute/DTLOC/copy_rk3locallist.for',
            'FastS/Compute/DTLOC/copyflux.for',
            'FastS/Compute/DTLOC/copyfluxrk3local.for',
            'FastS/Compute/DTLOC/copyflux_rk3local.for',
            'FastS/Compute/DTLOC/copyflux_rk3localpara.for',
            'FastS/Compute/DTLOC/copyflux_rk3locallist.for',
            'FastS/Compute/DTLOC/copyflux_rk3local2.for',
            'FastS/Compute/DTLOC/copyflux_rk3local2para.for',
            'FastS/Compute/DTLOC/copyfluxrk3local2.for',
            'FastS/Compute/DTLOC/interpolation.for',
            'FastS/Compute/DTLOC/interpolation2.for',
            'FastS/Compute/DTLOC/interpolation3.for',
            'FastS/Compute/DTLOC/interpolation4.for',
            'FastS/Compute/DTLOC/interprk3local.for',
            'FastS/Compute/DTLOC/interp_rk3local.for',
            'FastS/Compute/DTLOC/interprk3local2.for',
            'FastS/Compute/DTLOC/interp_rk3local2.for',
            'FastS/Compute/DTLOC/interp_rk3local3.for',
            'FastS/Compute/DTLOC/interp_rk3local3para.for',
            'FastS/Compute/DTLOC/interp_rk3local3list.for',
            'FastS/Compute/DTLOC/interp_rk3local4.for',
            'FastS/Compute/DTLOC/interp_rk3local4para.for',
            'FastS/Compute/DTLOC/conservativite32.for',
            'FastS/Compute/DTLOC/conservrk3local.for',
            'FastS/Compute/DTLOC/conservrk3local2.for',
            'FastS/Compute/DTLOC/conservrk3local3.for',
            'FastS/Compute/DTLOC/conservrk3local3para.for',
            'FastS/Compute/DTLOC/conservrk3local4.for',
            'FastS/Compute/DTLOC/conservrk3local4para.for',
            'FastS/Compute/DTLOC/constantinescu.for',
            'FastS/Compute/DTLOC/constantinescurk32.for',
            'FastS/Compute/DTLOC/constantinescurk3.for',
            'FastS/Compute/DTLOC/switchvectors.for',
            'FastS/Compute/DTLOC/initdrodm.for',
            'FastS/Compute/DTLOC/init_ssiter_bloc2.for',
            'FastS/Compute/DTLOC/remp_cellfictives.for',
            'FastS/Compute/DTLOC/remp_cellfictivespara.for',
#            'FastS/Compute/FLU_GUILLLAUME/flu_burgers.for',
            'FastS/Compute/DTLOC/calcul_cfl.for',
            'FastS/Compute/LU/extrap_coe.for',
            'FastS/Compute/LU/mjro_newton.for',
#            'FastS/Compute/LU/invlu_luSA.for',
            'FastS/Compute/LU/invlu_ale_l_SA.for',
            'FastS/Compute/LU/invlu_ale_u_SA.for',
            'FastS/Compute/LU/invlu_l_SA.for',
            'FastS/Compute/LU/invlu_u_SA.for',
            'FastS/Compute/LU/invlu_overlap_ale_l_SA.for',
            'FastS/Compute/LU/invlu_overlap_ale_u_SA.for',
            'FastS/Compute/LU/invlu_overlap_ale_l.for',
            'FastS/Compute/LU/invlu_overlap_ale_u.for',
            'FastS/Compute/LU/invlu_overlap_l_SA.for',
            'FastS/Compute/LU/invlu_overlap_u_SA.for',
            'FastS/Compute/LU/invlu_overlap_l.for',
            'FastS/Compute/LU/invlu_overlap_u.for',
#            'FastS/Compute/LU/invlu_lu.for',
            'FastS/Compute/LU/invlu_ale_l.for',
            'FastS/Compute/LU/invlu_ale_u.for',
            'FastS/Compute/LU/invlu_l.for',
            'FastS/Compute/LU/invlu_u.for',
#            'FastS/Compute/LU/invlu_d.for',
            'FastS/Compute/LU/invlu.for',
            'FastS/Compute/LU/invlussor1_l.for',
            'FastS/Compute/LU/invlussor_l.for',
            'FastS/Compute/LU/invlussor_u.for',
            'FastS/Compute/LU/invlussor1_l_SA.for',
            'FastS/Compute/LU/invlussor_l_SA.for',
            'FastS/Compute/LU/invlussor_u_SA.for',
            'FastS/Compute/LU/invlussor1_ale_l.for',
            'FastS/Compute/LU/invlussor_ale_l.for',
            'FastS/Compute/LU/invlussor_ale_u.for',
            'FastS/Compute/LU/invlussor1_ale_l_SA.for',
            'FastS/Compute/LU/invlussor_ale_l_SA.for',
            'FastS/Compute/LU/invlussor_ale_u_SA.for',
            'FastS/Compute/Linear_solver/init_gram_schmidt.for',
            'FastS/Compute/Linear_solver/normalisation_vect.for',
            'FastS/Compute/Linear_solver/scal_prod.for',
            'FastS/Compute/Linear_solver/vect_rvect.for',
            'FastS/Compute/Linear_solver/prod_mat_vect.for',
            'FastS/Compute/Linear_solver/id_vect.for',
            'FastS/Compute/Linear_solver/precond_select.for',
            'FastS/Compute/Linear_solver/pre_bc.for',
            #TAPENADE GMRES
            'FastS/Compute/Linear_solver/dp_dw_vect.for',
            #TAPENADE
            'FastS/ADJOINT/dpj_dpw_calc_meth.for',
            'FastS/ADJOINT/AUSM/dpJ_dpW_fluausm_select.for',
            'FastS/ADJOINT/AUSM/2d/dpJ_dpW_fluausm_euler_o3_2d.for']
            #'FastS/ADJOINT/rhs_adjoint.for',
            #'FastS/ADJOINT/AUSM/fluausm_adjoint_select.for',
            #'FastS/ADJOINT/AUSM/2d/fluausm_euler_o3_2d_b.for',
            #'FastS/ADJOINT/calc_rhs.for',
            #'FastS/ADJOINT/TAPENADE_FUNCTIONS/adBuffer.for']
