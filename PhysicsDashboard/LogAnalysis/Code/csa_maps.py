"Dictionary relating sequence CSA hints to SED attributes"

"Dictionary relating sequence CSA hints to attributes"
sequence_csa_map = {"100  ": "date_and_time",
            "304  ": "measurement_time",
            "305  ": "allowed_meas_pause",
            "903  ": "calculated_predelay",
            "904  ": "calculated_measpause",
            "1104  ": "readout_and_check_time_bb",
            "1203  ": "start_of_measurement_host_time",
            "1204  ": "finish_of_measurement_host_time",
            "1206  ": "start_of_measurement_mcir_time",
            "1207  ": "finish_of_measurement_mcir_time",
            "1205  ": "total_measurement_time_host",
            "1208  ": "total_measurement_time_mcir",
            "1209  ": "pause_after_measurement",
            "1210  ": "pause_averaging_time",
            "1211  ": "meas_uid",
            "301  ": "protocol_name"}


b1_csa_map = {"100  ": "date_and_time",
              "201  ": "patient_weight",
              "204  ": "patient_height",
              "205  ": "patient_gender",
              "804  ": "aspect_prim_name_a0",
              "907  ": "aspect_sec_name_a0",
              "805  ": "aspect_prim_name_a1",
              "908  ": "aspect_sec_name_a1",
              "806  ": "aspect_prim_name_a2",
              "909  ": "aspect_sec_name_a2",
              "807  ": "aspect_prim_name_a3",
              "910  ": "aspect_sec_name_a3",
              "808  ": "aspect_prim_name_a4",
              "911  ": "aspect_sec_name_a4",
              "809  ": "aspect_prim_name_a5",
              "912  ": "aspect_sec_name_a5",
              "810  ": "aspect_prim_name_a6",
              "913  ": "aspect_sec_name_a6",
              "811  ": "aspect_prim_name_a7",
              "914  ": "aspect_sec_name_a7",
              "812  ": "aspect_prim_name_a8",
              "915  ": "aspect_sec_name_a8",
              "813  ": "aspect_prim_name_a9",
              "916  ": "aspect_sec_name_a9",
              "900  ": "most_critical_aspect_number_name",
              "1112  ": "palipeakpowerforw_0",
              "1112b  ": "palipeakpowerrefl_0",
              "1113  ": "palipeakpowerforw_90",
              "1113b  ": "palipeakpowerrefl_90",
              "905  ":  "sed_limit",
              "1208 ": "total_measurement_time_mcir",
              "301  ": "protocol_name"}


"Dictionary relating SAR CSA hints to attributes"
sar_csa_map = {"401  ": "nominal_b0",
            "409  ": "tx_coil_serial_no",
            "412  ": "coil_power_loss_cp",
            "413  ": "coil_power_loss_ep",
            "414  ": "avg_b1_contact_lim_cp",
            "415  ": "avg_b1_contact_lim_ep",
            "416  ": "avg_b1_contact_lim_error",
            "423  ": "coil_sar_conv_factor",
            "504  ": "exposition_factor",
            "505  ": "irrad_factor_head",
            "506  ": "irrad_factor_torso",
            "507  ": "irrad_factor_leg",
            "508  ": "kr_scaling_factor",
            "600  ": "absolute_table_factor",
            "601  ": "adj_power",
            "301  ": "protocol_name"}


sed_csa_map = {"214  ": "current_sed_value",
               "905  ": "sed_limit",
               "906  ": "sed_threshold",
               "906a  ":  "predicted_sed_absolute",
               "906b  ":  "predicted_sed_rel_limit",
               "906c  ":  "predicted_sed_rel_threshold",
               "1201  ": "sed_after_measurement",
               "301  ": "protocol_name"}


abstract_csa_map = {"201  ": "patient_weight",
                    "202  ": "patient_registered_weight",
                    "203  ": "patient_age",
                    "204  ": "patient_height",
                    "205  ": "patient_gender",
                    "206  ": "patient_position",
                    "207  ": "superman_position",
                    "208  ": "patient_direction",
                    "209  ": "patient_kind",
                    "210  ": "head_cylinder_mass",
                    "210b  ": "head_cylinder_length",
                    "210c  ": "head_cylinder_radius",
                    "211  ": "torso_cylinder_mass",
                    "211b  ": "torso_cylinder_length",
                    "211c  ": "torso_cylinder_radius",
                    "212  ": "leg_cylinder_mass",
                    "212b  ": "leg_cylinder_length",
                    "212c  ": "leg_cylinder_radius",
                    "213  ": "last_examination",
                    "214  ": "current_sed_value",
                    "500  ": "sar_model_type",
                    "501  ": "sar_model_b1_ref",
                    "502  ": "head_position_relative_coil_n0",
                    "503  ": "relative_position_relative_top_of_head_n0",
                    "600  ": "absolute_table_position_n0",
                    "804  ": "aspect_prim_name_a0",
                    "804b  ": "factor_a0n0",
                    "805  ": "aspect_prim_name_a1",
                    "805b  ": "factor_a1n0",
                    "806  ": "aspect_prim_name_a2",
                    "806b  ": "factor_a2n0",
                    "807  ": "aspect_prim_name_a3",
                    "807b  ": "factor_a3n0",
                    "808  ": "aspect_prim_name_a4",
                    "808b  ": "factor_a4n0",
                    "809  ": "aspect_prim_name_a5",
                    "809b  ": "factor_a5n0",
                    "810  ": "aspect_prim_name_a6",
                    "810b  ": "factor_a6n0",
                    "811  ": "aspect_prim_name_a7",
                    "811b  ": "factor_a7n0",
                    "812  ": "aspect_prim_name_a8",
                    "812b  ": "factor_a8n0",
                    "813  ": "aspect_prim_name_a9",
                    "813b  ": "factor_a9n0",
                    "900  ": "most_critical_aspect_number",
                    "901  ": "most_critical_sar_aspect_number",
                    "902  ": "bore_temperature",
                    "903  ": "calculated_pre_delay",
                    "904  ": "calculated_meas_pause",
                    "905  ": "sed_limit",
                    "906  ": "sed_threshold",
                    "906b": "predicted_sed_absolute",
                    "906c": "predicted_sed_rel_limit",
                    "906d": "predicted_sed_rel_threshold",
                    "907  ": "aspect_sec_name_a0",
                    "907b  ": "aspect_limit_a0i0",
                    "907c  ": "aspect_averaging_time_a0i0",
                    "907d  ": "aspect_value_absolute_a0i0",
                    "907e  ": "aspect_value_relative_a0i0",
                    "907f  ": "aspect_limit_a0i1",
                    "907g  ": "aspect_averaging_time_a0i1",
                    "907h  ": "aspect_value_absolute_a0i1",
                    "907i  ": "aspect_value_relative_a0i1",
                    "907j  ": "aspect_limit_a0i2",
                    "907k  ": "aspect_averaging_time_a0i2",
                    "907l  ": "aspect_value_absolute_a0i2",
                    "907m  ": "aspect_value_relative_a0i2",
                    "907n  ": "aspect_limit_a0i3",
                    "907o  ": "aspect_averaging_time_a0i3",
                    "907p  ": "aspect_value_absolute_a0i3",
                    "907q  ": "aspect_value_relative_a0i3",
                    "908  ": "aspect_sec_name_a1",
                    "908b  ": "aspect_limit_a1i0",
                    "908c  ": "aspect_averaging_time_a1i0",
                    "908d  ": "aspect_value_absolute_a1i0",
                    "908e  ": "aspect_value_relative_a1i0",
                    "908f  ": "aspect_limit_a1i1",
                    "908g  ": "aspect_averaging_time_a1i1",
                    "908h  ": "aspect_value_absolute_a1i1",
                    "908i  ": "aspect_value_relative_a1i1",
                    "908j  ": "aspect_limit_a1i2",
                    "908k  ": "aspect_averaging_time_a1i2",
                    "908l  ": "aspect_value_absolute_a1i2",
                    "908m  ": "aspect_value_relative_a1i2",
                    "908n  ": "aspect_limit_a1i3",
                    "908o  ": "aspect_averaging_time_a1i3",
                    "908p  ": "aspect_value_absolute_a1i3",
                    "908q  ": "aspect_value_relative_a1i3",
                    "909  ": "aspect_sec_name_a2",
                    "909b  ": "aspect_limit_a2i0",
                    "909c  ": "aspect_averaging_time_a2i0",
                    "909d  ": "aspect_value_absolute_a2i0",
                    "909e  ": "aspect_value_relative_a2i0",
                    "909f  ": "aspect_limit_a2i1",
                    "909g  ": "aspect_averaging_time_a2i1",
                    "909h  ": "aspect_value_absolute_a2i1",
                    "909i  ": "aspect_value_relative_a2i1",
                    "909j  ": "aspect_limit_a2i2",
                    "909k  ": "aspect_averaging_time_a2i2",
                    "909l  ": "aspect_value_absolute_a2i2",
                    "909m  ": "aspect_value_relative_a2i2",
                    "909n  ": "aspect_limit_a2i3",
                    "909o  ": "aspect_averaging_time_a2i3",
                    "909p  ": "aspect_value_absolute_a2i3",
                    "909q  ": "aspect_value_relative_a2i3",
                    "910  ": "aspect_sec_name_a3",
                    "910b  ": "aspect_limit_a3i0",
                    "910c  ": "aspect_averaging_time_a3i0",
                    "910d  ": "aspect_value_absolute_a3i0",
                    "910e  ": "aspect_value_relative_a3i0",
                    "910f  ": "aspect_limit_a3i1",
                    "910g  ": "aspect_averaging_time_a3i1",
                    "910h  ": "aspect_value_absolute_a3i1",
                    "910i  ": "aspect_value_relative_a3i1",
                    "910j  ": "aspect_limit_a3i2",
                    "910k  ": "aspect_averaging_time_a3i2",
                    "910l  ": "aspect_value_absolute_a3i2",
                    "910m  ": "aspect_value_relative_a3i2",
                    "910n  ": "aspect_limit_a3i3",
                    "910o  ": "aspect_averaging_time_a3i3",
                    "910p  ": "aspect_value_absolute_a3i3",
                    "910q  ": "aspect_value_relative_a3i3",
                    "911  ": "aspect_sec_name_a4",
                    "911b  ": "aspect_limit_a4i0",
                    "911c  ": "aspect_averaging_time_a4i0",
                    "911d  ": "aspect_value_absolute_a4i0",
                    "911e  ": "aspect_value_relative_a4i0",
                    "911f  ": "aspect_limit_a4i1",
                    "911g  ": "aspect_averaging_time_a4i1",
                    "911h  ": "aspect_value_absolute_a4i1",
                    "911i  ": "aspect_value_relative_a4i1",
                    "911j  ": "aspect_limit_a4i2",
                    "911k  ": "aspect_averaging_time_a4i2",
                    "911l  ": "aspect_value_absolute_a4i2",
                    "911m  ": "aspect_value_relative_a4i2",
                    "911n  ": "aspect_limit_a4i3",
                    "911o  ": "aspect_averaging_time_a4i3",
                    "911p  ": "aspect_value_absolute_a4i3",
                    "911q  ": "aspect_value_relative_a4i3",
                    "912  ": "aspect_sec_name_a5",
                    "912b  ": "aspect_limit_a5i0",
                    "912c  ": "aspect_averaging_time_a5i0",
                    "912d  ": "aspect_value_absolute_a5i0",
                    "912e  ": "aspect_value_relative_a5i0",
                    "912f  ": "aspect_limit_a5i1",
                    "912g  ": "aspect_averaging_time_a5i1",
                    "912h  ": "aspect_value_absolute_a5i1",
                    "912i  ": "aspect_value_relative_a5i1",
                    "912j  ": "aspect_limit_a5i2",
                    "912k  ": "aspect_averaging_time_a5i2",
                    "912l  ": "aspect_value_absolute_a5i2",
                    "912m  ": "aspect_value_relative_a5i2",
                    "912n  ": "aspect_limit_a5i3",
                    "912o  ": "aspect_averaging_time_a5i3",
                    "912p  ": "aspect_value_absolute_a5i3",
                    "912q  ": "aspect_value_relative_a5i3",
                    "913  ": "aspect_sec_name_a6",
                    "913b  ": "aspect_limit_a6i0",
                    "913c  ": "aspect_averaging_time_a6i0",
                    "913d  ": "aspect_value_absolute_a6i0",
                    "913e  ": "aspect_value_relative_a6i0",
                    "913f  ": "aspect_limit_a6i1",
                    "913g  ": "aspect_averaging_time_a6i1",
                    "913h  ": "aspect_value_absolute_a6i1",
                    "913i  ": "aspect_value_relative_a6i1",
                    "913j  ": "aspect_limit_a6i2",
                    "913k  ": "aspect_averaging_time_a6i2",
                    "913l  ": "aspect_value_absolute_a6i2",
                    "913m  ": "aspect_value_relative_a6i2",
                    "913n  ": "aspect_limit_a6i3",
                    "913o  ": "aspect_averaging_time_a6i3",
                    "913p  ": "aspect_value_absolute_a6i3",
                    "913q  ": "aspect_value_relative_a6i3",
                    "914  ": "aspect_sec_name_a7",
                    "914b  ": "aspect_limit_a7i0",
                    "914c  ": "aspect_averaging_time_a7i0",
                    "914d  ": "aspect_value_absolute_a7i0",
                    "914e  ": "aspect_value_relative_a7i0",
                    "914f  ": "aspect_limit_a7i1",
                    "914g  ": "aspect_averaging_time_a7i1",
                    "914h  ": "aspect_value_absolute_a7i1",
                    "914i  ": "aspect_value_relative_a7i1",
                    "914j  ": "aspect_limit_a7i2",
                    "914k  ": "aspect_averaging_time_a7i2",
                    "914l  ": "aspect_value_absolute_a7i2",
                    "914m  ": "aspect_value_relative_a7i2",
                    "914n  ": "aspect_limit_a7i3",
                    "914o  ": "aspect_averaging_time_a7i3",
                    "914p  ": "aspect_value_absolute_a7i3",
                    "914q  ": "aspect_value_relative_a7i3",
                    "915  ": "aspect_sec_name_a8",
                    "915b  ": "aspect_limit_a8i0",
                    "915c  ": "aspect_averaging_time_a8i0",
                    "915d  ": "aspect_value_absolute_a8i0",
                    "915e  ": "aspect_value_relative_a8i0",
                    "915f  ": "aspect_limit_a8i1",
                    "915g  ": "aspect_averaging_time_a8i1",
                    "915h  ": "aspect_value_absolute_a8i1",
                    "915i  ": "aspect_value_relative_a8i1",
                    "915j  ": "aspect_limit_a8i2",
                    "915k  ": "aspect_averaging_time_a8i2",
                    "915l  ": "aspect_value_absolute_a8i2",
                    "915m  ": "aspect_value_relative_a8i2",
                    "915n  ": "aspect_limit_a8i3",
                    "915o  ": "aspect_averaging_time_a8i3",
                    "915p  ": "aspect_value_absolute_a8i3",
                    "915q  ": "aspect_value_relative_a8i3",
                    "916  ": "aspect_sec_name_a9",
                    "916b  ": "aspect_limit_a9i0",
                    "916c  ": "aspect_averaging_time_a9i0",
                    "916d  ": "aspect_value_absolute_a9i0",
                    "916e  ": "aspect_value_relative_a9i0",
                    "916f  ": "aspect_limit_a9i1",
                    "916g  ": "aspect_averaging_time_a9i1",
                    "916h  ": "aspect_value_absolute_a9i1",
                    "916i  ": "aspect_value_relative_a9i1",
                    "916j  ": "aspect_limit_a9i2",
                    "916k  ": "aspect_averaging_time_a9i2",
                    "916l  ": "aspect_value_absolute_a9i2",
                    "916m  ": "aspect_value_relative_a9i2",
                    "916n  ": "aspect_limit_a9i3",
                    "916o  ": "aspect_averaging_time_a9i3",
                    "916p  ": "aspect_value_absolute_a9i3",
                    "916q  ": "aspect_value_relative_a9i3",
                    "1201  ": "sed_after_measurement",
                    "301  ": "protocol_name"}



