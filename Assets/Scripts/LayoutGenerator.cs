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
                } else {
                    layoutModel[i,j] = 2;
                }
            }
        }

        return layoutModel;
    }
}