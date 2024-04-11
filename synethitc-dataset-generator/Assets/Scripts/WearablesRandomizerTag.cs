using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Parameters;
using UnityEngine.Perception.Randomization.Randomizers;
using UnityEngine.Perception.Randomization.Samplers;

// Add this Component to any GameObject that you would like to be randomized. This class must have an identical name to
// the .cs file it is defined in.
public class WearablesRandomizerTag : RandomizerTag 
{
    public GameObject[] helmets;
    public GameObject[] vest;
    public GameObject[] glasses;
    public GameObject[] gloves;

}

[Serializable]
[AddRandomizerMenu("Wearables Randomizer")]
public class WearablesRandomizer : Randomizer
{
    
    
    protected override void OnIterationStart()
    {
        System.Random random = new System.Random();
        var tags = tagManager.Query<WearablesRandomizerTag>();
        foreach (var tag in tags)
        {

            GameObject[][] wearables = new GameObject[][]
            {
                tag.helmets,
                tag.vest,
                tag.glasses,
                tag.gloves
            };


            foreach (GameObject[] category in wearables)
            {
                int randomInt = random.Next(0, category.Length);
                foreach(GameObject gameObject in category)
                {
                    gameObject.SetActive(false);
                }
                category[randomInt].SetActive(true);
            }
        }            
    }
}
