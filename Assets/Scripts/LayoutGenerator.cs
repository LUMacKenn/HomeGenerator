using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class GridGenerator
{
    public static int[,] GenerateLayout(int maxWidth, int maxHeight) {

        int[,] layoutModel = new int[maxHeight, maxWidth];
        
        for (int i = 0; i < maxHeight; i++) {
            for (int j = 0; j < maxWidth; j++) {
                float selection = Random.Range(0f,1f);
                if (selection < 0.5) {
                    layoutModel[i,j] = 0;
                } else if (selection < 0.75) {
                    layoutModel[i,j] = 1;
                } else if (selection < 0.97) {
                    layoutModel[i,j] = 2;
                } else {
                    layoutModel[i,j] = 3;
                }
            }
        }
        //Debug.Log("generated")

        return layoutModel;
    }

    public static int[,] ReadLayoutFromFile(string fileName) {
        Debug.Log("wow");
        string[] lines = System.IO.File.ReadAllLines($"../HomeGenerator/Assets/Layouts/{fileName}");
        int height = lines.Length;
        int width = lines[0].Trim().Split(' ').Length;

        int[,] layoutModel = new int[height, width];
        for (int j = 0; j < height; j++) {
            string[] chars = lines[j].Trim().Split(' ');
            for (int i = 0; i < width; i++) {
                int tileNum = int.Parse(chars[i]);
                layoutModel[i,j] = tileNum;
            }
        }
        

        return layoutModel;
    }

    public static int[,] SetBoundaries(int maxWidth, int maxHeight) {

        int[,] layoutModel = new int[maxHeight, maxWidth];
        
        for (int i = 1; i < maxWidth - 1; i++) {
            // first and last rows 
            layoutModel[i, 0] = 4;
            layoutModel[i, maxHeight - 1] = 6;
        }

        for (int j = 1; j < maxHeight - 1; j++) {
            // first and last columns 
            layoutModel[0, j] = 5;
            layoutModel[maxWidth - 1, j] = 7;
        }
        // set corners
        layoutModel[0, 0] = 8;
        layoutModel[0, maxHeight - 1] = 9;
        layoutModel[maxWidth - 1, 0] = 11;
        layoutModel[maxWidth - 1, maxHeight - 1] = 10;


        //Debug.Log("generated")

        return layoutModel;
    }
}