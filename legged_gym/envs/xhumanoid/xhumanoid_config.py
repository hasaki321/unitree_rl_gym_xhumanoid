from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class XHumanoidRoughCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 1] # x,y,z [m]
        default_joint_angles = {
        'hip_roll_l_joint':0, 
        'hip_yaw_l_joint':0, 
        'hip_pitch_l_joint':-0., 
        'knee_pitch_l_joint':0., 
        'ankle_pitch_l_joint':-0., 
        'ankle_roll_l_joint':0, 
        'hip_roll_r_joint':0, 
        'hip_yaw_r_joint':0, 
        'hip_pitch_r_joint':-0., 
        'knee_pitch_r_joint':0., 
        'ankle_pitch_r_joint':-0., 
        'ankle_roll_r_joint':0, 
        'shoulder_roll_l_joint':0, 
        'elbow_l_joint':0, 
        'shoulder_roll_r_joint':0, 
        'elbow_r_joint':0, 
}
    
    class env(LeggedRobotCfg.env):
        # 3 + 3 + 3 + 50 + 50 + 50 + 2 = 161
        num_observations = 47
        num_privileged_obs = 50
        num_actions = 12


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
        # 'shoulder_roll_l_joint':150, 
        # 'elbow_l_joint':122, 
        # 'shoulder_roll_r_joint':150, 
        # 'elbow_r_joint':122, 
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
        # 'shoulder_roll_l_joint':2, 
        # 'elbow_l_joint':2.2, 
        # 'shoulder_roll_r_joint':2, 
        # 'elbow_r_joint':2.2, 
        }
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/lite/urdf/humanoid_publish.urdf'
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
            lin_vel_z = -0.2
            ang_vel_xy = -0.05
            orientation = -1.0
            base_height = -10.0
            dof_acc = -2.5e-7
            dof_vel = -1e-3
            feet_air_time = 0.0
            collision = 0.0
            action_rate = -0.01
            dof_pos_limits = -5.0
            alive = 1.5
            hip_pos = -1.0
            contact_no_vel = -0.02
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

  
