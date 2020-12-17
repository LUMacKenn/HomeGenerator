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

        return layoutModel;
    }

    public static int[,] ReadLayoutFromFile(string fileName) {
        string[] lines = System.IO.File.ReadAllLines($"../HomeGenerator/Assets/Layouts/{fileName}");
        int height = lines.Length;
        int width = lines[0].Trim().Split(' ').Length;

        //int[,] layoutModel = new int[height, width];
        int[,] layoutModel = new int[width, height];
        // for (int i = 0; i < width; i++) {
        for (int j = 0; j < height; j++) {
            string[] chars = lines[j].Trim().Split(' ');
            //for (int j = 0; j < height; j++) {
            for (int i = 0; i < width; i++) {

                int tileNum = int.Parse(chars[i]);
                layoutModel[i,j] = tileNum;
            }
        }
        

        return layoutModel;
    }
}