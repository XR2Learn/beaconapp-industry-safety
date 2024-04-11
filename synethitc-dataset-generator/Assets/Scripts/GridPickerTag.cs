using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Randomizers;


public class GridPickerTag : RandomizerTag
{
    
    [SerializeField] public GridEnablerTag[] children;

    public bool debug = false;
    public float timeInterval = 10f;
    private float timeElapsed;
    private int counter = 0;

    private void Awake()
    {
        timeElapsed = timeInterval + 1f;
        int childCount = transform.childCount;
        children = new GridEnablerTag[childCount];

        for (int i = 0; i < childCount; i++)
        {
            children[i] = transform.GetChild(i).GetComponent<GridEnablerTag>();
        }
    }
    private void Update()
    {
        timeElapsed += Time.deltaTime;
    }
    public void ActivateRandomChild()
    {
        if (timeElapsed < timeInterval) return;
        timeElapsed = 0;

        for (int i = 0; i < children.Length; i++)
        {
            children[i].SetStatus(false);
        }

        int nextIndex = counter % children.Length;

        children[nextIndex].SetStatus(true);

        if (debug)
        {
            Debug.Log($"Next index: {nextIndex}. {children[nextIndex].name} Status: {children[nextIndex].GetStatus()} PrevStatus: {children[nextIndex].GetPrevStatus()}");
        }

        counter++;
    }
}


[Serializable]
[AddRandomizerMenu("Grid Picker")]
public class GridPicker : Randomizer
{
    protected override void OnIterationStart()
    {        
        var tags = tagManager.Query<GridPickerTag>();
        foreach (var tag in tags)
        {
            tag.ActivateRandomChild();
        }
    }        
}
