# tile_rules = {
#     "tileFloor": {
#         "posX": [("tileFloor", 0), ("tileWall", 0)],
#         "negX": [("tileFloor", 0), ("tileWall", 0)],
#         "posZ": [("tileFloor", 0)],
#         "negZ": [("tileFloor", 0), ("tileWall", 0)],
#     },
#     "tileWall": {
#         "posX": [("tileWall", 0)],
#         "negX": [("tileWall", 0)],
#         "posZ": [("tileFloor", 0), ("tileWall", 2)],
#         "negZ": [("tileWall", 2)],
#     },
#     "tileWallCorner": {
#         "posX": [("tileWall", 0)],
#         "negX": [],
#         "posZ": [("tileFloor", 0), ("tileWall", )],
#         "negZ": [("tileWall", 2)],
#     },
# }

tile_rules = {
    "tileFloor": {
        "tileNum": 0,
        "neighbors": {
            "posX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [3],
            },
            "negX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [1],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
            },
            "negZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [0],
            },
        },
    },
    "tileWall": {
        "tileNum": 1,
        "neighbors": {
            "posX": {
                "tileWall": [0],
                "tileWallCorner": [3],
            },
            "negX": {
                "tileWall": [0],
                "tileWallCorner": [0],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
            },
            "negZ": {
                "tileWall": [2],
                "tileWallCorner": [1,2],
            },
        },
    },
    "tileWallCorner": {
        "tileNum": 2,
        "neighbors": {
            "posX": {
                # "tileFloor": [0,1,2,3],
                "tileWall": [0],
                "tileWallCorner": [3],
            },
            "negX": {
                "tileWall": [3],
                "tileWallCorner": [2,3],
            },
            "posZ": {
                # "tileFloor": [0,1,2,3],
                "tileWall": [1],
                "tileWallCorner": [1],
            },
            "negZ": {
                "tileWall": [2],
                "tileWallCorner": [1,2],
            },
        },
    },
}

def create_adjacency_mappings():
    adjacency_mappings = {}

    # print(tile_rules.items())

    # For each tile in the defined rules
    for tile_key, tile_info in tile_rules.items():
        tile_num = tile_info["tileNum"]
        neighbors = tile_info["neighbors"]
        neighbor_lists = [neighbors["posX"], neighbors["negZ"], neighbors["negX"], neighbors["posZ"]]
        # For each of the four possible rotations: O(1)
        for rotation in range(4):
            mapping = {
                "neighbors" : []
            }
            variant_num = tile_num * 4 + rotation
            neighbor_lists = neighbor_lists[rotation:] + neighbor_lists[:rotation]
            # Loop through all four directions in the list of lists of neighbors: O(1)
            for neighbor_list in neighbor_lists:
                single_rotation_neighbors = []
                # Loop through all possible neighbor tile types in a single direction
                for neighbor_key, neighbor_rotations in neighbor_list.items():
                    neighbor_base_tilenum = tile_rules[neighbor_key]["tileNum"] * 4
                    # Loop through all rotation types of a single tile type: O(1)
                    for neighbor_rotation in neighbor_rotations:
                        neighbor_variant = neighbor_base_tilenum + neighbor_rotation
                        single_rotation_neighbors.append(neighbor_variant)
                mapping["neighbors"].append(single_rotation_neighbors)

            adjacency_mappings[variant_num] = mapping

    return adjacency_mappings