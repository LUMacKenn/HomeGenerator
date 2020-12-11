tile_rules = {
    "tileFloor": {
        "tileNum": 0,
        "neighbors": {
            "posX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [3],
                "tileWallOutsideCorner": [0,3],
                "tileDoorway": [3],
            },
            "negX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [1],
                "tileWallOutsideCorner": [1,2],
                "tileDoorway": [1],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
                "tileWallOutsideCorner": [0,1],
                "tileDoorway": [2],
            },
            "negZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [0],
                "tileWallOutsideCorner": [2,3],
                "tileDoorway": [0],
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
                "tileDoorway": [0],
            },
            "negX": {
                "tileWall": [0],
                "tileWallCorner": [0],
                "tileWallOutsideCorner": [0],
                "tileDoorway": [0],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
                "tileWallOutsideCorner": [2,3],
                "tileDoorway": [2],
            },
            "negZ": {
                "tileWall": [2],
                "tileWallCorner": [1,2],
                "tileBorderWall": [0],
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
                "tileDoorway": [0],
            },
            "negX": {
                "tileWall": [3],
                "tileWallCorner": [2,3],
                "tileBorderWall": [1],
            },
            "posZ": {
                "tileWall": [1],
                "tileWallCorner": [1],
                "tileWallOutsideCorner": [1],
                "tileDoorway": [1],
            },
            "negZ": {
                "tileWall": [2],
                "tileWallCorner": [1,2],
                "tileBorderWall": [0],
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
                "tileDoorway": [0],
            },
            "negX": {
                "tileFloor": [0,1,2,3],
                "tileWall": [1],
                "tileWallOutsideCorner": [1,2],
                "tileDoorway": [1],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
                "tileWallOutsideCorner": [2,3],
                "tileDoorway": [2],
            },
            "negZ": {
                "tileWall": [3],
                "tileWallCorner": [3],
                "tileWallOutsideCorner": [3],
                "tileDoorway": [3],
            },
        },
    },
    "tileDoorway": {
        "tileNum": 4,
        "neighbors": {
            "posX": {
                "tileWall": [0],
                "tileWallCorner": [3],
                "tileWallOutsideCorner": [1],
                # "tileDoorway": [0],
            },
            "negX": {
                "tileWall": [0],
                "tileWallCorner": [0],
                "tileWallOutsideCorner": [0],
                # "tileDoorway": [0],
            },
            "posZ": {
                "tileFloor": [0,1,2,3],
                "tileWall": [2],
                "tileWallOutsideCorner": [2,3],
                "tileDoorway": [2],
            },
            "negZ": {
                "tileDoorway": [2],
            },
        },
    },
    "tileBorderWall": {
        "tileNum": 5,
        "neighbors": {
            "posX": {
                "tileBorderWall": [0],
                "tileEmpty": [0,1,2,3],
            },
            "negX": {
                "tileBorderWall": [0],
                "tileEmpty": [0,1,2,3],
            },
            "posZ": {
                "tileWall": [0],
                "tileWallCorner": [0,3],
            },
            "negZ": {
                "tileEmpty": [0,1,2,3],
            },
        },
    },
    "tileEmpty": {
        "tileNum": 6,
        "neighbors": {
            "posX": {
                "tileBorderWall": [0,1,2,3],  # Will change this probably
                "tileEmpty": [0,1,2,3],
            },
            "negX": {
                "tileBorderWall": [0,1,2,3], # Will change this probably
                "tileEmpty": [0,1,2,3],
            },
            "posZ": {
                "tileBorderWall": [0,1,2,3], # Will change this probably
                "tileEmpty": [0,1,2,3],
            },
            "negZ": {
                "tileBorderWall": [0,1,2,3], # Will change this probably
                "tileEmpty": [0,1,2,3],
            },
        },
    },
}

# def fill_in_missing_adjacencies():
#     for tile_key, tile_info in tile_rules.items():
#         for direction, single_direction_neighbor_lists in tile_info["neighbors"]:
#             for neighbor_key, valid_neighbor_rotations in single_direction_neighbor_lists:
#                 pass

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
            neighbor_lists_rotated = neighbor_lists[-rotation:] + neighbor_lists[:-rotation]
            # Loop through all four directions in the list of lists of neighbors: O(1)
            for direction, neighbor_list in enumerate(neighbor_lists_rotated):
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