using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

[CustomEditor(typeof(CustomTextureRandomizerTag))]
public class TextureRandomizerEditor : Editor
{
    SerializedProperty folderPath;
    SerializedProperty fileNames;

    private void OnEnable()
    {
        folderPath = serializedObject.FindProperty("folderPath");
        fileNames = serializedObject.FindProperty("fileNames");
    }
    public override void OnInspectorGUI()
    {
        
      
        CustomTextureRandomizerTag customRandomizerTag = (CustomTextureRandomizerTag) target;       

        EditorGUILayout.PropertyField(folderPath);
        EditorGUILayout.PropertyField(fileNames);

        // Display the file picker button
        if (GUILayout.Button("Open File Picker"))
        {

            string fullPath =  EditorUtility.OpenFolderPanel("Load Textures", "C:/Users/konto/Documents/xr2learn/Unity/Perception/Assets/Materials/", "");
            string relativePath = "Assets" + fullPath.Substring(Application.dataPath.Length) +  "/";

            if (!string.IsNullOrEmpty(relativePath))
            {
                folderPath.stringValue = relativePath;

                string[] jpgFiles = Directory.GetFiles(relativePath, "*.jpg");
                string[] jpegFiles = Directory.GetFiles(relativePath, "*.jpeg");
                string[] pngFiles = Directory.GetFiles(relativePath, "*.png");
                string[] files = new string[jpgFiles.Length + jpegFiles.Length + pngFiles.Length];

                jpgFiles.CopyTo(files, 0);
                jpegFiles.CopyTo(files, jpgFiles.Length);
                pngFiles.CopyTo(files, jpgFiles.Length + jpegFiles.Length);

                fileNames.ClearArray();

                for (int i = 0; i < files.Length; i++)
                {
                    fileNames.InsertArrayElementAtIndex(i);
                    SerializedProperty element = fileNames.GetArrayElementAtIndex(i);
                    element.stringValue = files[i];
                }
               
            }
        }

        if (customRandomizerTag.fileNames != null && customRandomizerTag.fileNames.Length > 0)
        {
            EditorGUILayout.LabelField("Files in Folder:");
            foreach (string fileName in customRandomizerTag.fileNames)
            {
                EditorGUILayout.LabelField(fileName);
            }
        }

        serializedObject.ApplyModifiedProperties();



    }

      /*  if (EditorGUI.EndChangeCheck())
        {
            // If any variable values changed, mark the prefab as dirty
            EditorUtility.SetDirty(target);
        }*/
    
}
