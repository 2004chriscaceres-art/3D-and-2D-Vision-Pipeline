import open3d as o3d

# This downloads a sample "Bunny" 3D model automatically
bunny_data = o3d.data.BunnyMesh()

# This loads that data into the program
pcd = o3d.io.read_point_cloud(bunny_data.path)

# This opens a window so you can see the 3D model
o3d.visualization.draw_geometries([pcd])

import open3d as o3d

# 1. Load
dataset = o3d.data.BunnyMesh()
pcd = o3d.io.read_point_cloud(dataset.path)
print(f"Original points: {len(pcd.points)}")

# 2. Voxel Downsampling (Makes it look 'blocky' or less dense)
# Change voxel_size to 0.01 or 0.05 to see the difference
downsampled_pcd = pcd.voxel_down_sample(voxel_size=0.02)
print(f"Downsampled points: {len(downsampled_pcd.points)}")

# 3. Filtering (Removes random 'noisy' dots)
cl, ind = downsampled_pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
filtered_pcd = downsampled_pcd.select_by_index(ind)

# 4. Show the result
o3d.visualization.draw_geometries([filtered_pcd])
# Change this line to make the points larger (size=2)
o3d.visualization.draw_geometries([filtered_pcd], point_show_normal=True, mesh_show_back_face=True)