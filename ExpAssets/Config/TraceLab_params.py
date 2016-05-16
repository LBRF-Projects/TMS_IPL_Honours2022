# TraceLab Param overrides
#
# Any param that is commented out by default is either deprecated or else not yet implemented--don't uncomment or use

#########################################
# Available Hardware
#########################################
eye_tracker_available = False
eye_tracking = False
labjack_available = False
labjacking = False

#########################################
# Environment Aesthetic Defaults
#########################################
default_fill_color = (0, 0, 0, 255)
default_color = (255, 255, 255, 255)
default_response_color = default_color
default_input_color = default_color
default_font_size = 28
default_font_name = 'Frutiger'
default_timeout_message = "Too slow!"

#########################################
# EyeLink Sensitivities
#########################################
saccadic_velocity_threshold = 20
saccadic_acceleration_threshold = 5000
saccadic_motion_threshold = 0.15

fixation_size = 1 # deg of visual angle
box_size = 1 # deg of visual angle
cue_size = 1 # deg of visual angle
cue_back_size = 1 # deg of visual angle

#########################################
# Experiment Structure
#########################################
collect_demographics = True
run_practice_blocks = False
trials_per_block = 200
trials_per_practice_block = 0
blocks_per_experiment = 1
practice_blocks_per_experiment = 0
trials_per_participant = 0
pre_render_block_messages = False
show_practice_messages = True

#########################################
# Development Mode Settings
#########################################
dm_suppress_debug_pane = False
dm_auto_threshold = True

########################################
# Figure Controls
########################################
outer_margin = 150
inner_margin = 300
avg_seg_per_f = (15, 0)  # (avg number, variance)
avg_seg_per_q = (3, 1)  # (avg number, variance)
angularity = 0  # 0 = all curves, 1 = all lines
sharpness = 0.5  # 0 = bell curves & obtuse angle, 1 = sheer, elliptical curves & acute angles
path_length = -1  # length in px; -1 ignores this parameter; path length will override seg_length params if they conflict
avg_segment_length = 50  # in px
segment_length_variance = 0.25  # ie. percent of avg_segment_length