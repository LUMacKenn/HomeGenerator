using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LayoutGenerator : MonoBehaviour
{

    int[,] layoutModel;
    public int maxHeight = 10, maxWidth = 10, tileSize = 10;

    public GameObject tileFloor;
    public GameObject tileWall;
    public GameObject tileWallCorner;

    // Start is called before the first frame update
    void Start()
    {
        layoutModel = new int[maxHeight, maxWidth];
        
        for (int i = 0; i < maxHeight; i++) {
            for (int j = 0; j < maxWidth; j++) {
                float selection = Random.Range(0f,1f);
                if (selection < 0.33) {
                    layoutModel[i,j] = 0;
                } else if (selection < 0.66) {
                    layoutModel[i,j] = 1;
                } else {
                    layoutModel[i,j] = 2;
                }
            }
        }

        DisplayGrid(layoutModel);
    }

    void DisplayGrid(int[,] layoutModel) {

        for (int i = 0; i < layoutModel.GetLength(0); i++) {
            for (int j = 0; j < layoutModel.GetLength(1); j++) {
                switch(layoutModel[i,j]) {
                    case 0:
                        Instantiate(tileFloor, new Vector3(i * tileSize, 0, j * tileSize), Quaternion.identity);
                        break;
                    case 1:
                        Instantiate(tileWall, new Vector3(i * tileSize , 0, j * tileSize), Quaternion.identity);
                        break;
                    case 2:
                        Instantiate(tileWallCorner, new Vector3(i * tileSize , 0, j * tileSize), Quaternion.identity);
                        break;
                    default:
                        break;
                }
            }
        }
    }
}
