using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Parameters;
using UnityEngine.Perception.Randomization.Randomizers;
using UnityEngine.Perception.Randomization.Samplers;
using static UnityEngine.Rendering.DebugUI;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEditor;


public class CustomTextureRandomizerTag : RandomizerTag
{
    
    public string folderPath;

    public string[] fileNames; 

    public void UpdateFiles()
    {

       if (!string.IsNullOrEmpty(folderPath))
        {
            string[] jpgFiles = Directory.GetFiles(folderPath, "*.jpg");
            string[] jpegFiles = Directory.GetFiles(folderPath, "*.jpeg");
            string[] pngFiles = Directory.GetFiles(folderPath, "*.png");

            fileNames = new string[jpgFiles.Length + jpegFiles.Length + pngFiles.Length];

            jpgFiles.CopyTo(fileNames, 0);
            jpegFiles.CopyTo(fileNames, jpgFiles.Length);
            pngFiles.CopyTo(fileNames, jpgFiles.Length + jpegFiles.Length);
       }

    }
}

[Serializable]
[AddRandomizerMenu("Custom Texture Randomizer")]

public class CustomTextureRandomizer : Randomizer
{
    public string[] Type { get; private set; }
    protected override void OnIterationStart()
    {
        var tags = tagManager.Query<CustomTextureRandomizerTag>();

        foreach (var tag in tags)
        {                   
            if (tag.fileNames.Length == 0) return;
            int randomIndex = UnityEngine.Random.Range(0, tag.fileNames.Length);
            var material = tag.GetComponent<Renderer>().material;
            
            Texture randomTexture = AssetDatabase.LoadAssetAtPath<Texture>(tag.fileNames[randomIndex]);
            material.mainTexture = randomTexture;
        }
    }
}