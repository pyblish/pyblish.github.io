---
href: publishing---with-autodesk-maya
---

# Publishing - with Autodesk Maya

> The following sections are instructions on how to get Pyblish up and running using Autodesk Maya.


If you haven't already installed Pyblish, head back up to the [installation guide][Pyblish] to get started. Once ready, run this.

```bash
# Pyblish for Maya is a regular Python package on PyPI
$ pip install pyblish-maya
```

> Pyblish is being tested using versions 2013, 2014 and 2015

[Pyblish]: #installation

### Installing the integration into Maya

The next step is to expose the integration to Maya. For this, you've got two options.

1. Append a `userSetup.py` to your PYTHONPATH

    ```bash
    # Typically, the integration is located here
    c:\Python27\Lib\site-packages\pyblish_maya\pythonpath
    ```

    Append this path to your `PYTHONPATH`. See here for [help with modifying your environment][var]

2. Append to your own `userSetup.py`

    ```bash
    # Typically located here:
    C:\Users\marcus\Documents\maya\scripts\userSetup.py
    ```

     Append the following

     ```python
    import pyblish_maya.lib
    pyblish_maya.lib.register_plugins()
    pyblish_maya.lib.add_to_filemenu()
    ```

[var]: https://github.com/abstractfactory/pyblish/wiki/Adding-an-environment-variable

### Testing things out

The next time you open up Maya, look for an item in your `File` menu that reads "Publish". If you haven't got it, head over to the [Troubleshooting](#troubleshooting) section and we'll get you sorted out.


# Making your first publish

> This guide assumes you've got a freshly installed version of Maya and that you haven't changed it's project directory.

By the end of this page, sir, *you* will have made your first publish. Just follow these steps one by one and we'll take you through how to make it happen.

**Table of contents**

- [Create something](#create-something)
- [Select it](#select-it)
- [Make it publishable](#make-it-publishable)
- [Dissection](#dissection)
 - [Where did the publish go?](#where-did-the-publish-go)
 - [How it works](#how-it-works)
 - [5 minutes later](#5-minutes-later)
 - [Why did it go there?](#why-did-the-publish-go-there)
 - [Where did the naming convention come from?](#where-did-the-naming-convention-come-from)
- [Conclusion](#conclusion)

### Create something

How about a cube.

1. In your `Create` menu
2. Click `Polygon Primitives`
3. Click `Cube`
4. Rename your cube to "myCube"

Or type the following in your script editor.

```python
from maya import cmds
cmds.polyCube(name='myCube')
```

### Publish - 1st attempt

Allright, let's try publishing.

1. In your `File` menu
2. Click `Publish`

Or type the following:

```python
import pyblish.main
pyblish.main.publish_all()
```

Hmm. You're cube should have been published by now, but instead you've got a message saying:

```python
# No instances found. # 
```

What is that all about? As it turns out, there are just a few more steps we'll need to take before the button will know of exactly what and how you would like to perform your publish.

### Select it

*Select* is an important keyword in Pyblish. To *Select*, in Pyblish, means to specify what you would like to have published.

To select your cube, add it to a selection set.

1. In your `Create` menu
2. Click `Sets`
3. Followed by `Set`
4. Rename your set to "MyCube"

Or, type the following:

```python
cmds.sets(name='MyCube')
```

If you didn't have `myCube` selected when you created the set, make sure to add it to the set, either by dragging-and-dropping or by typing:

```python
cmds.sets('myCube', addElement='MyCube')
```

### Publish - 2nd attempt

Allright, let's try that again.

1. In your `File` menu
2. Click `Publish`

Or type the following:

```python
import pyblish.main
pyblish.main.publish_all()
```

Hmm, we're still missing something.

```python
# No instances found. # 
```

### Make it publishable

For Pyblish to know that *this* is what you would like to Publish, and nothing else, we need to tag the selection set. To tag it, add the following attributes and values.

```yaml
publishable (bool): True
family (string): "demo.model"
```

You can add it by going to your [Channel Box][chan].

1. In your `Edit` menu
2. Click `Add Attribute`
3. Type `publishable` as `Long name`
4. Click `Boolean` as `Data Type`
5. Hit `Add`
6. Type `family` as `Long name`
7. Click `String` as `Data Type`
8. Hit `OK`

Or type the following:

```python
cmds.addAttr('MyCube', at='bool', longName='publishable')
cmds.addAttr('MyCube', dt='string', longName='family')
```

Next, fill in the values.

1. In your [Attribute Editor][attributeeditor]
2. Under `Extra Attributes`
3. Toggle `publishable` to True
4. Type `demo.model` in the `family` text box

Or type the following:

```python
cmds.setAttr('MyCube.publishable', True)
cmds.setAttr('MyCube.family', 'demo.model', type='string')
```

Now Pyblish will be able to distinguish between this set and any other set you might have.

### Publish - 3rd attempt

Third time's the charm, right?

1. In your `File` menu
2. Click `Publish`

Or type the following:

```python
import pyblish.main
pyblish.main.publish_all()
```

**Error!**

```python
# Error:
# ValueError: The following nodes were misnamed
#   myCube
```

Uh-oh. Looks like we've got a new error this time. By the looks of it, our Cube wasn't named according to the naming conventions. Let's try and remedy this. Currently, the naming convention is for everything you publish to always have a three-letter extension.

1. Rename `myCube` to `myCube_GEO`
2. Re-run the publish

You should now see this message in your script editor.

```bash
# Finished successfully #
```

[chan]: http://download.autodesk.com/global/docs/maya2014/en_us/files/GUID-424694BA-019A-4D05-86EF-F9CD0A69D92C.htm
[attributeeditor]: http://download.autodesk.com/global/docs/maya2014/en_us/files/GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED.htm

## Dissection

Ok, let's back up a second and reflect on what happened. There are a couple of questions left unanswered from running your first publish above.

1. Where did the publish go?
1. Why did it go there?
1. Where did the naming convention come from?
1. Why did we have to add the two attributes, `publishable` and `family`?
1. Why did we have to put `myCube` into a selection set?

From the top:

1. To your workspace.
1. Because the plugin `extract_as_ma` put it there.
1. From the plugin `validate_naming_convention`.
1. Because the plugin `select_object_set` was looking for it.
1. Because the plugin `select_object_set` was looking for this too.

Too direct? Yes, let's have a closer look at how all of this fits together.

### Where did the publish go?

> To your workspace.

If you look within your project directory, you'll notice that you've now got a new folder called `published`.

```
C:\Users\marcus\Documents\maya\projects\default\published
```

This is where Pyblish chose to store `MyCube` when you hit the Publish button. But how did it know to do that? And why did it put it in a subdirectory that looks like the current date and time, followed by a few other directories?

- ![](/images/octicon-file-directory.png) published
 - ![](/images/octicon-file-directory.png) 20140907-174550
   - ![](/images/octicon-file-directory.png) demo.model
     - ![](/images/octicon-file-directory.png) MyCube

And how did it know to produce 4 files? Why not 5, or 3? 

- ![](/images/octicon-file-directory.png) MyCube
 - ![](/images/octicon-file.png) MyCube.ma
 - ![](/images/octicon-file.png) MyCube.mb
 - ![](/images/octicon-file.png) MyCube.obj
 - ![](/images/octicon-file.png) MyCube.mtl

Well, the answer lies in the plugins.

#### How it works

If you haven't already done so, now would be an excellent time to read [How It Works](#how-it-works). It'll provide you with an overview of how Pyblish processes your publishes. Once you're ready, come back here and we'll continue.

- [How It Works](#how-it-works)

### 5 minutes later

> Ok, so a selection plugin *selects* the cube?

Yes. It knows to do this because of how it is implemented.

It looks for nodes of type `objectSet` in your scene; specifically, nodes with the two attributes we added - `publishable` and `family`.

If you were to remove any of these two, the selector would go blind.

> Can I add anything to the `objectSet`?

Yes you can! That is the whole idea - you add what you intend on sharing with others. This way, you can separate the part of your scene that is sharable from the part that is not.

> What about the two attributes. What are they?

That's a good question. The `publishable` is merely an attribute to help the selector distinguish the nodes you are interested in publishing from those you are not. It's a way for the node to say "Me! Me! Me!" when you've got three identical nodes in your scene.

Remember when Neo took the red pill and they were able to locate him amongst a field of pods identical to his own?

`family` is where things start getting interesting. The family is a critical element of Pyblish. It's a way of saying "*this* instance belongs to *this* group of plugins". If you look at the selection set in your scene from your Attribute Editor, under "Extra Attributes", you'll see that the family attribute has the value "demo.model".

```python
print cmds.getAttr('MyCube.family')
```

> "demo.model"?

Yes, this is a way for the instance to say "I'd like all plugins compatible with `demo.model` to process me". Each plugin is associated with at least one (1) family. In effect, the instance is processed by a number of plugins compatible with this family.

```python
# A plugin may support multiple families, but
# an instance may only support one.
 _______________        _______________
|               |      |               |
| Instance      |      | Plugin        |
|               |      |               |
|    demo.model o----->o demo.model    |
|               |      o demo.anim     |
|               |      o demo.rig      |
|_______________|      |_______________|
```

> I'm confused..

Don't worry, this will make more sense once we get a little bit further in learning about Pyblish. All you need to remember from this is that each plugin carries a list of supported families and that all instances carries exactly one (1) family that may or may not match any of the available plugins.

### Why did the publish go there?

> Because the plugin `extract_as_ma` put it there.

Well, if you remember from the [**How It Works**](#how-it-works), once selection and validation was complete, extraction took over. One of the extractors - specifically, one called `extract_as_ma` - is responsible for putting the files where they ended up.

Remember, the primary responsibility of an extractor is *getting data out of an application*. It doesn't have much concern for exactly where the data ends up, as that is not within its responsibilities. Instead, this responsibility is delegated to conformers.

> Why couldn't the extractor just put the files where I want them right away?

They most certainly could, this is merely a guideline. The separation is made due to cases where you have one or more things happening to content once it exits an application.

1. Data is moved to one location
1. Data is archived in another location
1. The event is logger with a task tracking solution

For example, ask yourself these questions.

- What about when the network is down and it can't move the files to where they belong? 
- What about when the internet is down and the event can't be logged?
- Should this stop the application from exporting the data?

These are concerns well suited for conformers.

### Where did the naming convention come from?
-
> From the plugin `validate_naming_convention`.

By now, you can probably answer the remaining questions yourself. But there is one important aspect I'd like to point out regarding the naming convention plugin.

The reason this naming convention was applied to "myCube_GEO" was because we specified that this cube was of family "demo.model".

We associated this family with our cube and in effect said "associate this particular naming convention to this cube".

## Conclusion

Ok, time for a breather. 

We've covered a lot of ground here but if there is one thing I'd like you to take with you it is that the manner in which we just published your first instance is fully dictated by the plugins currently exposed to Pyblish by the time you initiate your publish and that these plugins are just demos.

Pyblish is a "eat your own dog-food" library in that anything it does it does in the same manner you would do it if you were the one implementing the behaviour. We think this is important and it keeps us honest and our implementations open for learning and modification.

You're probably very excited about writing your own plugins by now, so let's do that! If you've saved your work (you'll need it next), read on.

