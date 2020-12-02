using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HomeGenerator : MonoBehaviour
{

    int[,] layoutModel;
    public int maxHeight = 10, maxWidth = 10, tileSize = 10;

    public GameObject tileFloor;
    public GameObject tileWall;
    public GameObject tileWallCorner;

    // Start is called before the first frame update
    void Start()
    {
        layoutModel = GridGenerator.GenerateLayout(maxWidth, maxHeight);
        DisplayLayout(layoutModel);
    }

    void DisplayLayout(int[,] layoutModel) {

        for (int i = 0; i < layoutModel.GetLength(0); i++) {
            for (int j = 0; j < layoutModel.GetLength(1); j++) {
                Vector3 pos = new Vector3(i * tileSize, 0, j * tileSize);
                switch(layoutModel[i,j]) {
                    case 0:
                        Instantiate(tileFloor, pos, Quaternion.identity);
                        break;
                    case 1:
                        Instantiate(tileWall, pos, Quaternion.identity);
                        break;
                    case 2:
                        Instantiate(tileWallCorner, pos, Quaternion.identity);
                        break;
                    default:
                        break;
                }
            }
        }
    }
}
