#==============================================================================
# Fichiers C++
#==============================================================================
cpp_srcs = ['FastS/Metric/allocate_metric.cpp',
            'FastS/Metric/init_metric.cpp',
            'FastS/Init/cart.cpp',
            'FastS/Init/initVars.cpp',
            'FastS/Init/initNuma.cpp',
            'FastS/Init/itt.cpp',
            'FastS/Init/computePT_velocity_ale.cpp',
            'FastS/Compute/computePT.cpp',
            'FastS/Compute/gsdr3.cpp',
            'FastS/Compute/souszones_list.cpp',
            'FastS/Compute/DTLOC/stockrecup.cpp',
            'FastS/Compute/getbcfromzone.cpp',
            'FastS/BC/applyBC.cpp',
            'FastS/BC/BCzone.cpp',
            'FastS/BC/compute_effort.cpp',
            'FastS/DISPLAY/display_ss_iteration.cpp',
            'FastS/Compute/ALE/movegrid.cpp',
            'FastS/Compute/ALE/motionlaw.cpp',
            'FastS/Compute/LES/computePT_mut.cpp',
            'FastS/POST/computePT_enstrophy.cpp',
            'FastS/POST/computePT_variables.cpp',
            'FastS/POST/computePT_gradient.cpp',
            'FastS/HPC_LAYER/work_thread_distribution.cpp',
            'FastS/ADJOINT/compute_dpJ_dpW.cpp',
            'FastS/Com/setInterpTransfersFastS.cpp',
            #'FastS/ADJOINT/compute_RhsIterAdjoint.cpp',
            #'FastS/ADJOINT/rhs_Iter_Adj.cpp',
            #'FastS/ADJOINT/TAPENADE_FUNCTIONS/adStack.c',
            'FastS/STAT/computePT_my.cpp']

#==============================================================================
# Fichiers fortran
#==============================================================================
for_srcs = ['FastS/Metric/skmtr.for',
            'FastS/Metric/tijk_extrap.for',
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
            'FastS/BC/bvbs_periodique.for',
            'FastS/BC/bvbs_periodique_azimuthal.for',
            'FastS/BC/bvbs_wall_viscous_transition.for',
            'FastS/BC/bvbs_wall_viscous_adia.for',
            'FastS/BC/bvbs_wall_inviscid.for',
            'FastS/BC/bvbs_inflow_supersonic.for',
            'FastS/BC/bvbs_farfield.for',
            'FastS/BC/bvbs_outflow.for',
            'FastS/BC/bvbs_outpres.for',
#            'FastS/BC/bvbs_updatepressure.for',
            'FastS/BC/bvbs_inflow.for',
            'FastS/BC/bvbs_inflow_fich.for',
            'FastS/BC/bvbs_inflow_newton_ale.for',
            'FastS/BC/correct_coins.for',
            'FastS/BC/bceffort.for',
            'FastS/BC/bfl3.for',
            'FastS/BC/bflwall.for',
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
            'FastS/Compute/invist.for',
            'FastS/Compute/cptst3.for',
            'FastS/Compute/tstb3c.for',
            'FastS/Compute/tstb3_impli.for',
            'FastS/Compute/tstb3_impli_chimer.for',
            'FastS/Compute/tstb3_expli.for',
            'FastS/Compute/tstb3_expli_chimer.for',
            'FastS/Compute/cpcfl3.for',
            'FastS/Compute/src_term.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_lamin_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_lamin_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_lamin_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_lamin_o3_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_lamin_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_lamin_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_lamin_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_lamin_o3_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_SA_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_SA_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_SA_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_SA_o3_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_euler_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_euler_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_euler_o3_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_euler_o3_2d.for',
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
            'FastS/Compute/ROE/3dhomo/fluroe_lamin_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_lamin_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_lamin_o3_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_SA_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_SA_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_SA_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_SA_o3_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_euler_o3_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_euler_o3_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_euler_o3_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_euler_o3_2d.for',
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
            'FastS/Compute/AUSM/3dfull/fluausm_SA_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_SA_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_SA_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_SA_o3_2d.for',
            'FastS/Compute/AUSM/3dfull/fluausm_euler_o3_3dfull.for',
            'FastS/Compute/AUSM/3dhomo/fluausm_euler_o3_3dhomo.for',
            'FastS/Compute/AUSM/3dcart/fluausm_euler_o3_3dcart.for',
            'FastS/Compute/AUSM/2d/fluausm_euler_o3_2d.for',
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
            'FastS/Compute/ROE/3dfull/corr_fluroe_SA_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_SA_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_SA_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_SA_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_euler_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_SA_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_SA_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_SA_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_SA_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/corr_fluroe_ale_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/corr_fluroe_ale_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/corr_fluroe_ale_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/corr_fluroe_ale_euler_minmod_2d.for',
            'FastS/Compute/ROE/correction_fluroe_select.for',
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
            'FastS/Compute/ROE/3dhomo/fluroe_lamin_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_lamin_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_lamin_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_SA_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_SA_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_SA_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_SA_minmod_2d.for',
            'FastS/Compute/ROE/3dfull/fluroe_euler_minmod_3dfull.for',
            'FastS/Compute/ROE/3dhomo/fluroe_euler_minmod_3dhomo.for',
            'FastS/Compute/ROE/3dcart/fluroe_euler_minmod_3dcart.for',
            'FastS/Compute/ROE/2d/fluroe_euler_minmod_2d.for',
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
            'FastS/Compute/SA/vispalart.for',
            'FastS/Compute/SA/viszdes_izgris0.for',
            'FastS/Compute/SA/spsource_SA.for',
            'FastS/Compute/SA/spsource_SA_comp.for',
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
            'FastS/Compute/core3as2.for',
            'FastS/Compute/core3as2_chim.for',
            'FastS/Compute/core3ark3.for',
            'FastS/Compute/sfd.for',
            'FastS/Compute/extract_res.for',
            'FastS/Compute/init_ssiter_bloc.for',
            'FastS/Compute/cprdu3s1.for',
            'FastS/Compute/DTLOC/cplevel.for',
            'FastS/Compute/DTLOC/copy.for',
            'FastS/Compute/DTLOC/copyflux.for',
            'FastS/Compute/DTLOC/interpolation.for',
            'FastS/Compute/LU/mjro_newton.for',
#            'FastS/Compute/LU/invlu_luSA.for',
            'FastS/Compute/LU/invlu_ale_l_SA.for',
            'FastS/Compute/LU/invlu_ale_u_SA.for',
            'FastS/Compute/LU/invlu_l_SA.for',
            'FastS/Compute/LU/invlu_u_SA.for',
#            'FastS/Compute/LU/invlu_lu.for',
            'FastS/Compute/LU/invlu_ale_l.for',
            'FastS/Compute/LU/invlu_ale_u.for',
            'FastS/Compute/LU/invlu_l.for',
            'FastS/Compute/LU/invlu_u.for',
#            'FastS/Compute/LU/invlu_d.for',
            'FastS/Compute/LU/invlu.for',

            'FastS/ADJOINT/dpj_dpw_calc_meth.for',
            'FastS/ADJOINT/AUSM/dpJ_dpW_fluausm_select.for',
            'FastS/ADJOINT/AUSM/2d/dpJ_dpW_fluausm_euler_o3_2d.for']

            #'FastS/ADJOINT/rhs_adjoint.for',
            #'FastS/ADJOINT/AUSM/fluausm_adjoint_select.for',
            #'FastS/ADJOINT/AUSM/2d/fluausm_euler_o3_2d_b.for',
            #'FastS/ADJOINT/AUSM/2d/fluausm_euler_o3_2d_d.for',
            #'FastS/ADJOINT/calc_rhs.for',
            #'FastS/ADJOINT/TAPENADE_FUNCTIONS/adBuffer.for']
