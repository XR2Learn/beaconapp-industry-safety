using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Randomizers;


public class GridEnablerTag : RandomizerTag 
{
    public bool Status { private set; get; }
    public bool PrevStatus { private set; get; }   
  
    [SerializeField] public SeatPickerTag[] children;
    private void Awake()
    {
        Status = false;
        PrevStatus = false;

        int childCount = transform.childCount;
        children = new SeatPickerTag[childCount];

        for (int i = 0; i < childCount; i++)
        {
            children[i] = transform.GetChild(i).GetComponent<SeatPickerTag>();
        }        
    }

    public void SetStatus(bool status) 
    {
        Status = status;
    }

    public void UpdatePrevStatus()
    {
        PrevStatus = Status;
    }
    
    public bool GetStatus()
    {
        return Status;
    }

    public bool GetPrevStatus()
    {
        return PrevStatus;
    }
}

[Serializable]
[AddRandomizerMenu("Grid Enabler")]
public class GridEnabler : Randomizer
{
    protected override void OnIterationStart()
    {
        var tags = tagManager.Query<GridEnablerTag>();

        foreach (var tag in tags)
        {
            if (tag.PrevStatus != tag.Status)
            { 
                foreach (var child in tag.children)
                {                    
                    child.ChangeStatus(tag.Status);
                }
                tag.UpdatePrevStatus();
            }             
        }
    }
}
