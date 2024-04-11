# Synthetic Dataset Generator

Synthetic Dataset Generator is a unity project that generates annotated RGB images for the purpose of training object detection algorithms. The scenario that gets examined by this application is the detection of hazards inside industrial environments through training machine learning components to recognize whether the appropriate safety equipment is worn.

Through the Unity game engine, 3D models of working employees equipped with different combinations of safety wearables are placed in various poses around the capturing frame. The resulting composition is being saved as a PNG accompanied by a JSON file containing annotations about the objects of the image. The dataset creation workflow will be broken down into different parts below in order to be better understood and utilized in scenarios other than hazard detection.

## Table of Contents

- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Labeling](#labeling)
- [Defining a scenario](#defining-a-scenario)
- [Creating randomizers](#creating-randomizers)
- [Custom Randomizers](#custom-randomizers)
  - [Grid Picker](#grid-picker)
  - [Grid Enabler](#grid-enabler)
  - [Seat Picker](#seat-picker)
  - [Foreground Object Randomizer](#foreground-object-randomizer)
  - [Wearable Randomizers](#wearable-randomizers)
  - [Hue Randomizer](#hue-randomizer)
  - [Custom Texture Randomizer](#custom-texture-randomizer)

## Dependencies

The project is built on top of the [Perception package](https://github.com/Unity-Technologies/com.unity.perception), available from the Unity Asset Store. We exploit the option for labelling 3D models, injecting custom randomizing scripts and exporting RGB annotated images that this package offers. If you want to run Beacon Application 3 or to develop a similar application, make sure the Perception package is properly included inside your Unity project.

Large models of the project are available [here](https://drive.google.com/drive/folders/1X5IiqP73NPqwTjkL7KiycRXF4Z2NAhHN?usp=sharing).
Download the three .fbx models and place each one inside path: **Assets/Models/[Νame_Οf Μodel].fbx**

## Project Structure

The scene that we run to create the dataset is located inside the Scenes folder. This is the correct directory to place any new scene that corresponds to the creation of a different dataset type. Currently, inside this directory there is only this one scene active scene file.

The orchestration of all the procedures that take place according to given configuration settings is the WearablesScenario game object to which a Fixed Length Scenario component is attached. Through this component it gets decided how many iterations will take place during runtime and which randomizing script will be active. All custom randomizing scripts are located inside the Scripts directory, but we will dig into the concept of randomizing scripts later.

The models that are being instantiated during the creation process are located inside the Models directory. We are working with 3 different human models that contain the available safety wearables inside the model file (in FBX format). This approach, instead of loading each 3D model of the equipment one by one, was chosen because it allows for personalized modifications to be applied to the wearables giving a more realistic result when worn by each human figure.

Out of every human model, we created prefabs, to represent the variation of their body pose directly thought Unity and stored those in inside the Prefabs directory.

The color variations of the safety equipment demand access to a pool of textures, created in our case manually using photo editing software, more specifically GIMP. At runtime, randomizers assign a texture to the material of every wearable that is intended to change color. For this to be achieved, wearables attached to each human figure have their own personal material instead of sharing one, to avoid capturing identical objects during sampling. However, in cases of objects that do not participate in this procedure, some materials are being shared, for memory efficiency. This process led us to separate textures from materials and store them in different directories.

## Labeling

We are using perception’s labeling component for the desired categories that we want the object detection algorithms to learn.

When this component is attached to a game object, spatial information about it from the output RGB sample gets recorded in the annotation file along with its label name and ID. In our example, we only use information about the 2d bounding boxes (center, width, height) but the choice depends on the type of information that your machine learning algorithm uses.

Other information provided by Perception includes Depth Labeling, Instance Segmentation Labeling, Semantic Segmentation Labeling etc.

Controlling the exported information type is done via the Perception Camera Script that needs to be attached in the scene’s main camera. The script allows for more than one type of information can be extracted together in a single run

## Defining a scenario

To train the object detection algorithm successfully and reach comprehensive results we need to provide sufficient data that is also diverse, resilient, and representative. To achieve this, we determined 8 different layouts for our created scene that work as grids which contain predefined positions for the 3D human objects to spawn.

Each placeholding position constrains the scale and rotation of the human model that will take over this position inside a configurable limit and the selection of the model is happening randomly. Random is also the selection of the equipment, and its color, provided to a human object, the posture of the model and its rotation and scale (always within the configured limits).

This way we control how random the results will be, and we depict equipped human models in more natural positions. Those 8 different layouts succeed each other in a rotational order until the dataset creation process is finished.

This scenario is developed by a combination of custom randomizing scripts attached to game objects of the scene, to orchestrate the layout system and give the desired behavior to each one. However, keep in mind that different requirements for your dataset may need different scenarios and concluding to one is a process of continuous testing and refinement of your developed scene

## Creating Randomizers

The configuration of the perception’s scenario component decides which randomizers will be active at runtime and the order of their execution. Randomizers are scripts provided by the package, that in every iteration of the program apply their functionality to a set of game objects that get defined using randomizer tags or placeholders (for prefabs).

Attaching a randomizer tag to a game object gives access to the randomizing script to modify its properties in various ways such as: change its quaternion, spawn it to a random position, create background noise, change scene lighting etc. For more information about randomizers, you can read the Perception’s documentation.

In cases where a specific functionality is needed that is not provided by the built-in randomizers, there is the option to create your own. In our application, we used our own scripts to manage the spatial distribution of our models, the way they rotate and change colors. The table below describes the functionality of every custom script created for this purpose.

## Custom Randomizers

### `Grid Picker`

It is attached to the `Grid` game objects, making it behave as an orchestrator of the available layouts. Through it, a time interval is configured. When a time interval is passed the script iterates through its child objects, and randomly enables one of them utilizing the exposed methods of the `Grid Enabler` script. The children of the `Grid` game object represent all the available layouts of the scene

### `Grid Enabler`

Besides exposing functionality to enable/disable the `Grid` game object, it provides layout functionality to every game object it is attached to. The enabled layout activates its children, that work as fixed placeholding positions.

### `Seat Picker`

Attached to every child of a `Grid Enabler`, it renders a different human model in each iteration, when it is active. This script lets you configure if you want to define limit values for the scale and rotation of its models. An additional functionality, to configure the probability of scale and rotation to not be randomized is implemented.

### `Foreground Object Randomizer`

Attached to every rendered human model. It randomizes scale and rotation of the model respecting the limits set by the `Seat Picker`

### `Wearable Randomizers`

It separates wearables into different categories, in our case in `Helmets`, `Vests`, `Glasses` and `Gloves`. The game objects that represent those wearables can be dragged and dropped into those categories, so that the model is completely customizable. The script randomly picks one object of each category to be rendered. In our case we also provide a blank game object for each category for the option of no equipment.

### `Hue Randomizer`

It accepts different color options and applies a random one to the game object it is attached to in every iteration. `Hue Randomizer` is used to change the color of the wearables.

### `Custom Texture Randomizer`

It applies a different random texture to the game object it is attached to. Its functionality is similar to the `Hue Randomizer`’s but is useful for elements that require different materials instead of different colors. The pool of the available materials for each instance must be an existing directory of the project and the selected directory is configurable.
