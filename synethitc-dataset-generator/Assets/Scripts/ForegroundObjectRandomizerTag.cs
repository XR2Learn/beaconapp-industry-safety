using System;
using Unity.Mathematics;
using UnityEngine;
using UnityEngine.Perception.Randomization.Parameters;
using UnityEngine.Perception.Randomization.Randomizers;
using UnityEngine.Perception.Randomization.Samplers;
using UnityEngine.UIElements;
using static UnityEngine.Rendering.DebugUI;

public class ForegroundObjectRandomizerTag : RandomizerTag
{
    public Vector3 InitialAngles { get; private set; }
    public int Possibility { get; private set; } = 0;
    public FloatParameter Xangle { get; private set; } =
        new FloatParameter { value = new UniformSampler(-25f, 25f) };
    public FloatParameter Yangle { get; private set; } =
        new FloatParameter { value = new UniformSampler(-60f, 60f) };
    public FloatParameter Zangle { get; private set; } =
        new FloatParameter { value = new UniformSampler(0f, 0f) };
    public Vector3 InitialScale { get; private set; }
    public FloatParameter Scale { get; private set; } =
        new FloatParameter { value = new UniformSampler(0.5f, 1f) };
    public bool CanRotate { get; private set; } = true;
    public bool CanScale { get; private set; } = true;

    private void Awake()
    {
        InitialAngles = transform.eulerAngles;
        InitialScale = transform.localScale;
    }   

    public void SetRotationAngles(
        bool rotate,
        int possibility,
        UniformSampler xAngles,
        UniformSampler yAngles,
        UniformSampler zAngles
    )
    {
        CanRotate = rotate;
        if (!rotate)
            return;

        Possibility = possibility;
        Xangle.value = xAngles;
        Yangle.value = yAngles;
        Zangle.value = zAngles;
    }   

    public void SetScaleParameters(bool scale, UniformSampler scaleFactor)
    {
        CanScale = scale;
        if (!scale)
            return;

        Scale.value = scaleFactor;
    }
}

public class ForegroundObjectRandomizer : Randomizer
{
    System.Random random = new System.Random();

    protected override void OnIterationStart()
    {
        var tags = tagManager.Query<ForegroundObjectRandomizerTag>();

        foreach (var tag in tags)
        {
            if (tag.CanRotate)
            {
                var initAngle = tag.InitialAngles;
                int randomNumber = random.Next(100);

                if (randomNumber < tag.Possibility)
                {
                    var offset = new Vector3(
                        tag.Xangle.Sample(),
                        tag.Yangle.Sample(),
                        tag.Zangle.Sample()
                    );
                    tag.transform.eulerAngles = initAngle + offset;
                }
                else
                {
                    tag.transform.eulerAngles = initAngle;
                }
            }

            if (tag.CanScale)
            {
                Debug.Log(tag.InitialScale);
                float scalar = tag.Scale.Sample();
                Vector3 InitScale = tag.InitialScale;
                tag.transform.localScale = new Vector3(
                    InitScale.x * scalar,
                    InitScale.y * scalar,
                    InitScale.z * scalar
                );
            }
        }
    }
}
