tile_rules = {
    "tileFloor": {
        "tileNum": 0,
        "neighbors": {
            "posX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [3],
                "tileWallOutsideCorner": [0,3],
            },
            "negX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [1],
                "tileWallOutsideCorner": [1,2],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
                "tileWallOutsideCorner": [0,1],
            },
            "negZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [0],
                "tileWallOutsideCorner": [2,3],
            },
        },
    },
    "tileWall": {
        "tileNum": 1,
        "neighbors": {
            "posX": {
                "tileWall": [0],
                "tileWallCorner": [3],
                "tileWallOutsideCorner": [1],
            },
            "negX": {
                "tileWall": [0],
                "tileWallCorner": [0],
                "tileWallOutsideCorner": [0],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
                "tileWallOutsideCorner": [2,3],
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
                "tileWall": [0],
                "tileWallCorner": [3],
                "tileWallOutsideCorner": [1],
            },
            "negX": {
                "tileWall": [3],
                "tileWallCorner": [2,3],
            },
            "posZ": {
                "tileWall": [1],
                "tileWallCorner": [1],
                "tileWallOutsideCorner": [1],
            },
            "negZ": {
                "tileWall": [2],
                "tileWallCorner": [1,2],
            },
        },
    },
    "tileWallOutsideCorner": {
        "tileNum": 3,
        "neighbors": {
            "posX": {
                "tileWall": [0],
                "tileWallCorner": [3],
                "tileWallOutsideCorner": [1],
            },
            "negX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [1],
                "tileWallOutsideCorner": [1,2],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
                "tileWallOutsideCorner": [2,3],
            },
            "negZ": {
                "tileWall": [3],
                "tileWallCorner": [3],
                "tileWallOutsideCorner": [3],
            },
        },
    },
}

def create_adjacency_mappings():
    adjacency_mappings = {}

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
            neighbor_lists_rotated = neighbor_lists[rotation:] + neighbor_lists[:rotation]
            # Loop through all four directions in the list of lists of neighbors: O(1)
            # print(neighbor_lists)
            for neighbor_list in neighbor_lists_rotated:
                single_rotation_neighbors = []
                # Loop through all possible neighbor tile types in a single direction
                for neighbor_key, neighbor_rotations in neighbor_list.items():
                    neighbor_base_tilenum = tile_rules[neighbor_key]["tileNum"] * 4
                    # Loop through all rotation types of a single tile type: O(1)
                    for neighbor_rotation in neighbor_rotations:
                        rotated_neighbor_variant = neighbor_base_tilenum + (neighbor_rotation + rotation) % 4
                        single_rotation_neighbors.append(rotated_neighbor_variant)
                mapping["neighbors"].append(single_rotation_neighbors)

            adjacency_mappings[variant_num] = mapping

    return adjacency_mappings