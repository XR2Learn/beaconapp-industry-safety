using System;
using UnityEngine;
using UnityEngine.Perception.Randomization.Randomizers;
using UnityEngine.Perception.Randomization.Samplers;

public class SeatPickerTag : RandomizerTag
{
    public bool Status { private set; get; }
    public bool PrevStatus { private set; get; }
    public GameObject[] Humans { private set; get; }

    public bool rotate = true;
    public int possibility = 50;
    public UniformSampler xAngle = new(-25f, 25f);
    public UniformSampler yAngle = new(-60f, 60f);
    public UniformSampler zAngle = new(0f, 0f);

    public bool scale = true;
    public UniformSampler scaleFactor = new(0.5f, 1f);

    private System.Random random = new System.Random();

    private void Start()
    {
        Status = false;
        PrevStatus = true;

        int childCount = transform.childCount;
        Humans = new GameObject[childCount];

        for (int i = 0; i < childCount; i++)
        {
            Humans[i] = transform.GetChild(i).gameObject;
        }

        foreach (GameObject child in Humans)
        {
            var childSettings = child.GetComponent<ForegroundObjectRandomizerTag>();
            childSettings.SetRotationAngles(rotate, possibility, xAngle, yAngle, zAngle);
            childSettings.SetScaleParameters(scale, scaleFactor);

            /*child.GetComponent<ForegroundObjectRandomizerTag>().minFactor = minScale;
            child.GetComponent<ForegroundObjectRandomizerTag>().maxFactor = maxScale;*/
        }
    }

    public void ActivateRandomHuman()
    {
        if (Humans.Length == 0)
            return;

        foreach (var human in Humans)
        {
            human.SetActive(false);
        }

        int randomIndex = random.Next(0, Humans.Length);
        Humans[randomIndex].SetActive(true);
    }

    public void ChangeStatus(bool newStatus)
    {
        Status = newStatus;
    }

    public void UpdatePrevStatus()
    {
        PrevStatus = Status;
    }
}

[Serializable]
[AddRandomizerMenu("Seat Picker")]
public class SeatPicker : Randomizer
{
    protected override void OnIterationStart()
    {
        var tags = tagManager.Query<SeatPickerTag>();
        foreach (var tag in tags)
        {
            if (tag.PrevStatus != tag.Status && !tag.Status)
            {
                foreach (var human in tag.Humans)
                {
                    human.SetActive(tag.Status);
                }
                tag.UpdatePrevStatus();
            }
            else if (tag.Status)
            {
                tag.ActivateRandomHuman();
                if (tag.PrevStatus != tag.Status)
                    tag.UpdatePrevStatus();
            }
        }
    }
}
