using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Parameters;
using UnityEngine.Perception.Randomization.Randomizers;
using UnityEngine.Perception.Randomization.Samplers;


public class HueRandomizerTag : RandomizerTag 
{
    public Color[] colors;
    public int materialIndex=0;
}

[Serializable]
[AddRandomizerMenu("Hue Randomizer")]
public class HueRandomizer : Randomizer
{
    
    System.Random random = new System.Random();

    protected override void OnIterationStart()
    {
        

        var tags = tagManager.Query<HueRandomizerTag>();
        foreach (var tag in tags)
        {
            int randomInt = random.Next(0, tag.colors.Length);
            Color newColor = tag.colors[randomInt];
            Renderer renderer = tag.GetComponent<Renderer>();
            Material material = renderer.materials[tag.materialIndex];
            material.SetColor("_BaseColor", newColor);

        }
           
    }
}
