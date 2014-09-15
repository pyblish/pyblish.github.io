### ![](images/logo_macaw_small.png)
<!-- ### ![](images/logo_macaw_extrasmall.png) -->

This repository hosts the website located at http://pyblish.com and consists of the following elements.

- [Jekyll][] for page rendering
- [Markdown][] for content
- HTML and CSS for layout
- [Liquid][] for templating

Some links

- [Project Repository][repo]
- [Usergroup][usergroup]
- [Wiki][wiki]

### Contributing

If you'd like to contribute, let me first tell you a little bit about how it works.

Looking at the above file-listing, you'll notice a directory called `_posts`. As per Jekyll's default behaviour, this is traditionally where blog-posts lie, but here they host each paragraph you see on [the website][web].

Each paragraph is formatted in markdown and is "dynamically" merged upon loading the page. Each page then takes its place to the left of the page as *table of contents* along with providing *anchors* with which you can jump directly to that particular section of the page.

If you find an error or would otherwise like to contribute to the site, simply edit one or more files located within the `_posts` directory, or add your own. 

Each paragraph is then sorted by their "date"; as you can see, each date is in fact starting at year zero, and month 1, day 1.

### Why use GitHub for hosting?

Besides being free, here are some additional benefits:

- Issue tracking
- Revision history
- Contributor-friendly

How many public websites have a common place in which issues can be reported and maintained? How many sites maintain a history of their edits? And finally, how many of them can be contributed to by anyone?

That's why GitHub for hosting is the way to go.

### Why a single page?

You mean instead of having smaller pages per chapter? With a single page, it is clear where you are, how much progress you've made and how far you have left to go.

With smaller pages, you can never be sure of your progress or how far you have left to go; a tutorial could be endless for all you know.

A single page keeps us honest and you informed and we'll know instantly if the documentation ever grows too large.

[usergroup]: https://groups.google.com/forum/#!forum/pyblish
[wiki]: https://github.com/abstractfactory/pyblish/wiki
[repo]: https://github.com/abstractfactory/pyblish
[Jekyll]: http://jekyllrb.com
[Liquid]: http://liquidmarkup.org/
[web]: http://pyblish.com
[Markdown]: http://daringfireball.net/projects/markdown/