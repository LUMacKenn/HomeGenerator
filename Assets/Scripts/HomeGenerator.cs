using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HomeGenerator : MonoBehaviour
{

    int[,] layoutModel;
    int[,] boundaries; 
    int[,] lampLayoutModel; 
    public int maxHeight = 10, maxWidth = 10, tileSize = 10;

    public GameObject tileFloor;
    public GameObject tileWall;
    public GameObject tileWallCorner;
    public GameObject tileWallOutsideCorner;
    public GameObject tileWallDoorway;
    public GameObject lamp; 
    // Start is called before the first frame update
    void Start()
    {
        //Debug.Log("hello start")
        layoutModel = GridGenerator.GenerateLayout(maxWidth, maxHeight);
        layoutModel = GridGenerator.ReadLayoutFromFile("layout2.txt");
        lampLayoutModel = GridGenerator.ReadLayoutFromFile("lampLayout.txt");
        boundaries = GridGenerator.SetBoundaries(maxWidth, maxHeight); 
        DisplayLayout(layoutModel);
        DisplayLayout(boundaries);
        DisplayFurniture(lampLayoutModel); 
        //DisplayFurniture()
    }

    void DisplayLayout(int[,] layoutModel) {

        for (int i = 0; i < layoutModel.GetLength(0); i++) {
            for (int j = 0; j < layoutModel.GetLength(1); j++) {
                int tileCode = layoutModel[i,j];
                // int angle = (int) Random.Range(0f,4f) * 90;
                int angle = (tileCode % 4) * 90;
                int tileType = tileCode / 4;
                Vector3 center = new Vector3(i * tileSize, 0, j * tileSize);
                Vector3 diff = new Vector3(0, 0, 0);
                switch (angle) {
                    case 0:
                        diff = new Vector3(-tileSize/2, 0, -tileSize/2);
                        break;
                    case 90:
                        diff = new Vector3(-tileSize/2, 0, tileSize/2);
                        break;
                    case 180:
                        diff = new Vector3(tileSize/2, 0, tileSize/2);
                        break;
                    case 270:
                        diff = new Vector3(tileSize/2, 0, -tileSize/2);
                        break;
                }
                Vector3 pos = center + diff;
                Quaternion rot = Quaternion.Euler(0, angle, 0);
                switch(tileType) {
                    case 0:
                        Instantiate(tileFloor, pos, rot);
                        break;
                    case 1:
                        Instantiate(tileWall, pos, rot);
                        break;
                    case 2:
                        Instantiate(tileWallCorner, pos, rot);
                        break;
                    case 3:
                        Instantiate(tileWallOutsideCorner, pos, rot);
                        break;
                    default:
                        break;
                }
            }
        }
    }

    void DisplayFurniture(int[,] layout) {
        for (int i = 0; i < layout.GetLength(0); i++) {
            for (int j = 0; j < layout.GetLength(1); j++) {
                int hasLamp = layout[i, j]; 
                if (hasLamp == 1) {
                    Vector3 pos = new Vector3(i * tileSize - 5 , (float) 0.5, j * tileSize - 5);
                    Instantiate(lamp, pos, Quaternion.identity);
                }
      
            }
        }
    }
}
