from termcolor import colored
def calculate_torque(motor_weight_g, link_weight_g, joint_shaft_to_ee_distance_mm, ee_payload_kg, ee_len_mm=0, arm_ratio=1.0):
    """
    Calculate the torque for each joint.

    Parameters:
    motor_weight_g (list): List of motor weights in grams for each joint.
    link_weight_g (list): List of link weights in grams for each joint.
    joint_shaft_to_ee_distance_mm (list): List of distances from each joint to the end of the arm in mm.
    ee_payload_kg (float): Payload weight at the end effector in kg.
    ee_len (int): Length of end effector in mm.
    arm_ratio (float): Ratio for scaling the arm length and weight.
    
    Returns:
    list: List of torques required at each joint in Nm.
    """
    gravity = 9.8
    num_joints = len(motor_weight_g)
    torque_list = []

    # Apply the arm ratio to weights and distances
    # motor_weight_g = [weight * arm_ratio for weight in motor_weight_g]
    link_weight_g = [weight * arm_ratio for weight in link_weight_g]
    joint_shaft_to_ee_distance_mm = [distance * arm_ratio for distance in joint_shaft_to_ee_distance_mm]

    # Convert weights from grams to kilograms
    motor_weight_kg = [weight / 1000 for weight in motor_weight_g]
    link_weight_kg = [weight / 1000 for weight in link_weight_g]

    # Calculate total weights
    total_motor_weight_kg = sum(motor_weight_kg)
    total_link_weight_kg = sum(link_weight_kg)
    total_motor_link_weight_kg = total_motor_weight_kg + total_link_weight_kg
    print(f"Reach : {joint_shaft_to_ee_distance_mm[0]} mm")
    print(f"Payload : {ee_payload_kg} kg")
    print(f"=========================================")
    # print(f"Motor weights: {motor_weight_kg}")
    # print(f"Motor weights: {link_weight_kg}")
    print(f"Total motor weight: {total_motor_weight_kg:.2f} kg")
    print(f"Total link weight: {total_link_weight_kg:.2f} kg")
    print(f"Total motor and link weight: {total_motor_link_weight_kg:.2f} kg")

    # Add end effector length to the joint_shaft_to_ee_distance_mm
    adjusted_distances_mm = [distance + ee_len_mm for distance in joint_shaft_to_ee_distance_mm]
    
    # Verify distances
    print(f"Adjusted distances with EE (mm): {adjusted_distances_mm}")

    # Calculate the torque for each joint
    for i in range(num_joints):
        total_mass = ee_payload_kg
        torque = total_mass * gravity * (adjusted_distances_mm[i] / 1000)
        
        for j in range(i, num_joints):
            total_mass += motor_weight_kg[j] + link_weight_kg[j]
            torque += (motor_weight_kg[j] + link_weight_kg[j]) * gravity * (adjusted_distances_mm[j] / 1000)
        
        torque_list.append(torque)
    
    return torque_list

# Define the parameters
ee_payload_kg = 1.2
ee_len_mm = 40

# Estimation of link weight
link_weight_g = [150, 100, 100, 100, 100, 50]
# Distance if joint to EE frame
joint_shaft_to_ee_distance_mm = [550, 550, 300, 300, 30, 30]

# Motor weight specs
motor_weight_g = [517, 436, 391, 436, 190, 199]
# Motor Rated Toruqe (Pass/Fail) Check 
rated_static_toruqe = [12, 6.6, 6.6, 6.6, 1.0, 1.0]
rated_max_toruqe = [18, 14, 14, 14, 2.2, 2.2]

# Experiment with different arm length ratios
arm_ratios_to_test = [0.8, 1.0, 1.2]


for arm_ratio in arm_ratios_to_test:
    print("\033[0m\n\n################################################")
    print(f"Calculating for arm length ratio factor: {arm_ratio}")
    # Calculate the torques
    torques = calculate_torque(motor_weight_g, link_weight_g, joint_shaft_to_ee_distance_mm, ee_payload_kg, ee_len_mm=ee_len_mm, arm_ratio=arm_ratio)
    print("================== RESULT ====================")
    # Print the results
    for i, torque in enumerate(torques):
        if torque > rated_static_toruqe[i]:
            print(f"\033[91mFAIL: Torque needed at joint {i + 1}: {torque:.2f} Nm, rated torque {rated_static_toruqe[i]}/{rated_max_toruqe[i]}")
        else:
            print(f"\033[92mOK:Torque needed at joint {i + 1}: {torque:.2f} Nm, rated torque {rated_static_toruqe[i]}/{rated_max_toruqe[i]}")
    