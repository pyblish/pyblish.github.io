---
layout: default
---

Pyblish is a plug-in driven automation framework for content.

# Overview

Some of the immediate benefits of using Pyblish are

- [Higher quality content](#higher-quality-content)
- [Greater content reuse](#greater-reuse-of-content)
- [Lower iteration times](#lower-iteration-time)
- [Shortened learning curve](#shortened-learning-curve)

##### Higher quality content

When looking out over your content, it can be difficult to know what quality standards it all falls under. Some files may have been perfected while others may be haphazardly put together by an intern. Passing data through validations is one way of reducing the range of quality differences throughout your library of content.

##### Greater reuse of content

Traditionally, as projects come and go, you tend to end up with a rather large library of assets. Unfortunately, most of these assets are often tightly tailored to their parent project and rarely usable once complete. But when content from Project A looks and works similar to Project B, it isn't too far of a stretch to imagine it fitting in with Project C, D and E as well.

##### Lowered iteration time

Sending content back to the artist responsible for creating it is a major time sink. Due to data being validated prior to being passed on using Pyblish, this can be reduced drastically and artists can share content effortlessly and with confident that it will work.

##### Shortened learning curve

When validating data, the state of each file may come as less of a surprise to the artist making use of it. Traditionally, handing data from one artist to another typically involves an ad-hoc process of one explaining his methods and conventions to the other so that the content can be continued upon. With Pyblish, an organisation can pre-define conventions upon each category of content so as to minimise the amount of new information present within each file.

This works both ways, a new artists sharing his work with others must first become comfortable with the conventions already in place. Traditionally, this is a process of trail and error where an artist must study the implicit conventions of others and continually make improvements upon his work until it conforms to the overall quality produced by his peers. This comes at a cost not only to himself, but to others who discover the flaws and send it back. A process known as "passing shit downstream". With Pyblish, this can be drastically reduced and artist, both veteran or novice, can confidently provide others with content living up to par with the organisation.

# Installation

The best way to learn anything is to try things out. So let's get Pyblish installed!

```bash
# Pyblish is a regular Python package, available on PyPI
$ pip install pyblish
```

To test things out, let's try and import our newly installed package.

```python
Python 2.7.7 (default, Jun  1 2014, 14:21:57)
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyblish
>>> pyblish.version
'0.1.16'
```

> If this isn't the results you've got, head on over to [[Troubleshooting|end-user-troubleshooting]] and we'll try and get things sorted.

For a gold star, run the included test-suite.

```cmd
$ cd c:\Python27\Lib\site-packages\pyblish
$ python -m pyblish.vendor.nose --verbose --exclude=vendor --with-doctest
The data() interface works ... ok
Config works as expected ... ok
Main interface works ... ok
...

----------------------------------------------------------------------
Ran 25 tests in 0.071s
```

Unless it said anything except how many tests it ran, you're good to go!

# Integrations

You've just installed Pyblish, but Pyblish isn't much without any of its integrations. Head on over to our Autodesk Maya integration for further instructions on how to get setup.

[![](https://github.com/abstractfactory/pyblish/wiki/images/maya-pyblish.png)][maya]

If you have any other integrations in mind, do let us know and we'll get you set up on developing your very own integration with Pyblish!

[maya]: https://github.com/abstractfactory/pyblish-maya/wiki
