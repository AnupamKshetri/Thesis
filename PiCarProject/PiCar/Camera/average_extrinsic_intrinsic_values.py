import numpy as np
import os

def load_intrinsic_params(file_number):
    intrinsic_data = np.load(f'intrinsic_params_{file_number}.npz')
    camera_matrix = intrinsic_data['camera_matrix']
    dist_coeffs = intrinsic_data['dist_coeffs']
    return camera_matrix, dist_coeffs

def load_extrinsic_params(file_number):
    extrinsic_data = np.load(f'extrinsic_params_{file_number}.npz')
    rotation_matrices = extrinsic_data['rotation_matrices']
    translation_vectors = extrinsic_data['translation_vectors']
    euler_angles = extrinsic_data['euler_angles']
    return rotation_matrices, translation_vectors, euler_angles

def main():
    num_images = 5
    data_path = '/home/pi/Desktop/Thesis/PiCarProject/PiCar/Camera'

    all_camera_matrices = []
    all_dist_coeffs = []
    all_rotation_matrices = []
    all_translation_vectors = []
    all_euler_angles = []

    for i in range(1, num_images + 1):
        intrinsic_camera_matrix, intrinsic_dist_coeffs = load_intrinsic_params(i)
        extrinsic_rotation_matrices, extrinsic_translation_vectors, extrinsic_euler_angles = load_extrinsic_params(i)

        all_camera_matrices.append(intrinsic_camera_matrix)
        all_dist_coeffs.append(intrinsic_dist_coeffs)
        all_rotation_matrices.extend(extrinsic_rotation_matrices)
        all_translation_vectors.extend(extrinsic_translation_vectors)
        all_euler_angles.extend(extrinsic_euler_angles)

    avg_camera_matrix = np.mean(all_camera_matrices, axis=0)
    avg_dist_coeffs = np.mean(all_dist_coeffs, axis=0)
    avg_rotation_matrix = np.mean(all_rotation_matrices, axis=0)
    avg_translation_vector = np.mean(all_translation_vectors, axis=0)
    avg_euler_angles = np.mean(all_euler_angles, axis=0)

    print("Average Camera Matrix:\n", avg_camera_matrix)
    print("Average Distortion Coefficients:\n", avg_dist_coeffs)
    print("Average Rotation Matrix:\n", avg_rotation_matrix)
    print("Average Translation Vector:\n", avg_translation_vector)
    print("Average Euler Angles (in radians):\n", avg_euler_angles)

if __name__ == "__main__":
    main()
