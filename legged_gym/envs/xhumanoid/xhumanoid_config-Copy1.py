from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class XHumanoidRoughCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.9] # x,y,z [m]
        default_joint_angles = {
        'hip_roll_l_joint':0, 
        'hip_yaw_l_joint':0, 
        'hip_pitch_l_joint':-0.1, 
        'knee_pitch_l_joint':0.3, 
        'ankle_pitch_l_joint':0, 
        'ankle_roll_l_joint':-0.2, 
        'hip_roll_r_joint':0, 
        'hip_yaw_r_joint':0, 
        'hip_pitch_r_joint':-0.1, 
        'knee_pitch_r_joint':0.3, 
        'ankle_pitch_r_joint':0, 
        'ankle_roll_r_joint':-0.2, 
        'left_joint1':0, 
        'shoulder_roll_l_joint':0, 
        'left_joint3':0, 
        'elbow_l_joint':0, 
        'left_joint5':0, 
        'left_joint6':0, 
        'left_joint7':0, 
        'L_index_proximal_joint':0, 
        'L_index_intermediate_joint':0, 
        'L_middle_proximal_joint':0, 
        'L_middle_intermediate_joint':0, 
        'L_pinky_proximal_joint':0, 
        'L_pinky_intermediate_joint':0, 
        'L_ring_proximal_joint':0, 
        'L_ring_intermediate_joint':0, 
        'L_thumb_proximal_yaw_joint':0, 
        'L_thumb_proximal_pitch_joint':0, 
        'L_thumb_intermediate_joint':0, 
        'L_thumb_distal_joint':0, 
        'right_joint1':0, 
        'shoulder_roll_r_joint':0, 
        'right_joint3':0, 
        'elbow_r_joint':0, 
        'right_joint5':0, 
        'right_joint6':0, 
        'right_joint7':0, 
        'R_index_proximal_joint':0, 
        'R_index_intermediate_joint':0, 
        'R_middle_proximal_joint':0, 
        'R_middle_intermediate_joint':0, 
        'R_pinky_proximal_joint':0, 
        'R_pinky_intermediate_joint':0, 
        'R_ring_proximal_joint':0, 
        'R_ring_intermediate_joint':0, 
        'R_thumb_proximal_yaw_joint':0, 
        'R_thumb_proximal_pitch_joint':0, 
        'R_thumb_intermediate_joint':0, 
        'R_thumb_distal_joint':0
}
    
    class env(LeggedRobotCfg.env):
        # 3 + 3 + 3 + 50 + 50 + 50 + 2 = 161
        num_observations = 161
        num_privileged_obs = 164
        num_actions = 50


    class domain_rand(LeggedRobotCfg.domain_rand):
        randomize_friction = True
        friction_range = [0.1, 1.25]
        randomize_base_mass = True
        added_mass_range = [-1., 3.]
        push_robots = True
        push_interval_s = 5
        max_push_vel_xy = 1.5

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
          # PD Drive parameters:
        stiffness = {
        'hip_roll_l_joint':113, 
        'hip_yaw_l_joint':68, 
        'hip_pitch_l_joint':113, 
        'knee_pitch_l_joint':100, 
        'ankle_pitch_l_joint':60, 
        'ankle_roll_l_joint':30, 
        'hip_roll_r_joint':113, 
        'hip_yaw_r_joint':68, 
        'hip_pitch_r_joint':113, 
        'knee_pitch_r_joint':100, 
        'ankle_pitch_r_joint':60, 
        'ankle_roll_r_joint':30, 
        'left_joint1':113, 
        'shoulder_roll_l_joint':150, 
        'left_joint3':83, 
        'elbow_l_joint':122, 
        'left_joint5':150, 
        'left_joint6':150, 
        'left_joint7':150, 
        'L_index_proximal_joint':150, 
        'L_index_intermediate_joint':150, 
        'L_middle_proximal_joint':150, 
        'L_middle_intermediate_joint':150, 
        'L_pinky_proximal_joint':150, 
        'L_pinky_intermediate_joint':150, 
        'L_ring_proximal_joint':150, 
        'L_ring_intermediate_joint':150, 
        'L_thumb_proximal_yaw_joint':150, 
        'L_thumb_proximal_pitch_joint':150, 
        'L_thumb_intermediate_joint':150, 
        'L_thumb_distal_joint':150, 
        'right_joint1':113, 
        'shoulder_roll_r_joint':150, 
        'right_joint3':83, 
        'elbow_r_joint':122, 
        'right_joint5':150, 
        'right_joint6':150, 
        'right_joint7':150, 
        'R_index_proximal_joint':150, 
        'R_index_intermediate_joint':150, 
        'R_middle_proximal_joint':150, 
        'R_middle_intermediate_joint':150, 
        'R_pinky_proximal_joint':150, 
        'R_pinky_intermediate_joint':150, 
        'R_ring_proximal_joint':150, 
        'R_ring_intermediate_joint':150, 
        'R_thumb_proximal_yaw_joint':150, 
        'R_thumb_proximal_pitch_joint':150, 
        'R_thumb_intermediate_joint':150, 
        'R_thumb_distal_joint':150
        }

        damping = {
        'hip_roll_l_joint':1.7, 
        'hip_yaw_l_joint':1.3, 
        'hip_pitch_l_joint':1.7, 
        'knee_pitch_l_joint':2.8, 
        'ankle_pitch_l_joint':2.2, 
        'ankle_roll_l_joint':1.7, 
        'hip_roll_r_joint':1.7, 
        'hip_yaw_r_joint':1.3, 
        'hip_pitch_r_joint':1.7, 
        'knee_pitch_r_joint':2.8, 
        'ankle_pitch_r_joint':2.2, 
        'ankle_roll_r_joint':1.7, 
        'left_joint1':1.7, 
        'shoulder_roll_l_joint':2, 
        'left_joint3':1.5, 
        'elbow_l_joint':2.2, 
        'left_joint5':2, 
        'left_joint6':2, 
        'left_joint7':2, 
        'L_index_proximal_joint':2, 
        'L_index_intermediate_joint':2, 
        'L_middle_proximal_joint':2, 
        'L_middle_intermediate_joint':2, 
        'L_pinky_proximal_joint':2, 
        'L_pinky_intermediate_joint':2, 
        'L_ring_proximal_joint':2, 
        'L_ring_intermediate_joint':2, 
        'L_thumb_proximal_yaw_joint':2, 
        'L_thumb_proximal_pitch_joint':2, 
        'L_thumb_intermediate_joint':2, 
        'L_thumb_distal_joint':2, 
        'right_joint1':1.7, 
        'shoulder_roll_r_joint':2, 
        'right_joint3':1.5, 
        'elbow_r_joint':2.2, 
        'right_joint5':2, 
        'right_joint6':2, 
        'right_joint7':2, 
        'R_index_proximal_joint':2, 
        'R_index_intermediate_joint':2, 
        'R_middle_proximal_joint':2, 
        'R_middle_intermediate_joint':2, 
        'R_pinky_proximal_joint':2, 
        'R_pinky_intermediate_joint':2, 
        'R_ring_proximal_joint':2, 
        'R_ring_intermediate_joint':2, 
        'R_thumb_proximal_yaw_joint':2, 
        'R_thumb_proximal_pitch_joint':2, 
        'R_thumb_intermediate_joint':2, 
        'R_thumb_distal_joint':2
        }
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/xhumanoid/urdf/humanoid.urdf'
        name = "xhumanoid"
        foot_name = "ankle_roll"
        penalize_contacts_on = ["hip", "knee"]
        terminate_after_contacts_on = ["pelvis"]
        self_collisions = 1 # 1 to disable, 0 to enable...bitwise filter
        flip_visual_attachments = False
  
    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.78
        class scales( LeggedRobotCfg.rewards.scales ):
            tracking_lin_vel = 1.0
            tracking_ang_vel = 0.5
            lin_vel_z = -2.0
            ang_vel_xy = -0.05
            orientation = -1.0
            base_height = -10.0
            dof_acc = -2.5e-7
            feet_air_time = 0.0
            collision = -1.0
            action_rate = -0.01
            torques = 0.0
            dof_pos_limits = -5.0
            alive = 0.15
            hip_pos = -1.0
            contact_no_vel = -0.2
            feet_swing_height = -20.0
            contact = 0.18

class XHumanoidRoughCfgPPO( LeggedRobotCfgPPO ):
    class policy:
        init_noise_std = 0.8
        actor_hidden_dims = [32]
        critic_hidden_dims = [32]
        activation = 'elu' # can be elu, relu, selu, crelu, lrelu, tanh, sigmoid
        # only for 'ActorCriticRecurrent':
        rnn_type = 'lstm'
        rnn_hidden_size = 64
        rnn_num_layers = 1
    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.01
    class runner( LeggedRobotCfgPPO.runner ):
        policy_class_name = "ActorCriticRecurrent"
        max_iterations = 10000
        run_name = ''
        experiment_name = 'xhumanoid'

  
