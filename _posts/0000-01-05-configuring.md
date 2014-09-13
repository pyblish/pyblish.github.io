---
href: configuring-pyblish
---

# Configuring Pyblish

Besides being completely driven by plug-in, Pyblish also provides options to be configured further. Primarily in the form of exposing the various plug-ins to your various circumstances. You can do that, let's find out how.

- [Custom paths](#custom-paths)
 - [Via Python](#custom-paths-via-python)
 - [Via configuration](#custom-paths-via-configuration)
 - [Via environment](#custom-paths-via-environment)

### Custom paths

The most important aspect of configuration is how you expose your plugins to your pipeline. As mentioned in [[the previous tutorial|Creating-Your-First-Plugin]], paths have three levels of configuration, each with its own benefits and disadvantages.

#### Custom paths via python

Exposing plug-ins via Python is known as *registering paths* and can be done like this:

```python
>>> import pyblish.backend.plugin
>>> pyblish.backend.plugin.register_plugin_path(r'c:\my_path')
```

You can manipulate the paths further with the following functions:

```python
>>> pyblish.backend.plugin.deregister_plugin_path(r'c:\my_path')
>>> pyblish.backend.plugin.deregister_all()
```

To inspect which paths are currently registered, you can use this:

```python
>>> pyblish.backend.plugin.registered_paths
['c:\my_path']
```

To inspect ALL paths exposed to Pyblish, including those added via PUBLISHPLUGINPATH and configuration, you can use this:

```python
>>> pyblish.backend.plugin.plugin_paths()
['c:\my_path', 'c:\my_configured_path', 'c:\my_environment_path']
```

This is can be great for debugging if you ever get lost in the midst of paths. You can also inspect configured paths individually:

```python
>>> pyblish.backend.config
>>> pyblish.backend.config.paths
['c:\my_configured_path']
```

Along with those added via the environment

```python
>>> import os
>>> os.environ['PYBLISHPLUGINPATH']
'c:\my_environment_path'
```

#### Custom paths via configuration

But how do you actually add paths via configuration? If you head into the Python package, typically located here:

```
c:\Python27\Lib\site-packages\pyblish
```

And look within your `\backend` directory for a `config.yaml`. This file contains everything that can be configured about the internals of Pyblish, including plugin paths.

**config.yaml**

```yaml
paths: 
    - "{pyblish}/plugins"
```

In this YAML-formatted file you can see a rather odd looking path. This is the default plug-in path for Pyblish and points to an inner directory of the Python library called `plugins`. The curly-braces represents string-substitution; at run-time, this is replaced with the actual path to the Pyblish Python library.

- For a full view of this file, [see here][config].

Ok, so you now know where paths are being configured, but it's best to avoid tampering with files within an actual library. Not only due to risk of losing your work if the library were to be reinstalled or updated.

A better way is to augment this configuration with your own. This is where the `.pyblish` yaml file comes in.

```
c:\users\marcus\.pyblish
```

Information stored in this file will augment the default configuration of Pyblish. To add your own paths to this file, simply do what was done in the original.

```yaml
paths:
    - "c:/my_configured_path"
```

Don't forget to also include the default path, if you are still interested in having them exposed to your pipeline.

```yaml
paths:
    - "{pyblish}/plugins"
    - "c:/my_configured_path"
```

##### Configuration and its location

User-configuration defaults to your home-directory. With this, it is possible to maintain an overarching configuration on a shared drive that sym-links into each users home-directory.

- See [symlinking][] for more information.

However it may be beneficial to provide an option for where Pyblish looks for its configuration. Feel free to drop us a line (or a pull-request) with any ideas.

[symlinking]: http://www.howtogeek.com/howto/16226/complete-guide-to-symbolic-links-symlinks-on-windows-or-linux/
[config]: https://github.com/abstractfactory/pyblish/blob/master/pyblish/backend/config.yaml

### Custom paths via environment

You may also inject plug-in paths directly into your environment. These will get picked up by Pyblish at run-time and augment any pre-existing paths already exposed via Python or configuration.

This is particularly helpful if you launch processes via a [wrapper][], which you can configure to append plugins relevant to your particular project.

```python
import os
import subprocess

custom_environment = os.environ.copy()
custom_environment['PYBLISHPLUGINPATH'] = "c:\spiderman_plugins"

subprocess.Popen('maya', env=custom_environment)
```