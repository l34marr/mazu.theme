mazu.theme Installation
-----------------------

To install mazu.theme into the global Python environment (or a workingenv),
using a traditional Zope 2 instance, you can do this:

* When you're reading this you have probably already run 
  ``easy_install mazu.theme``. Find out how to install setuptools
  (and EasyInstall) here:
  http://peak.telecommunity.com/DevCenter/EasyInstall

* If you are using Zope 2.9 (not 2.10), get `pythonproducts`_ and install it 
  via::

    python setup.py install --home /path/to/instance

into your Zope instance.

* Create a file called ``mazu.theme-configure.zcml`` in the
  ``/path/to/instance/etc/package-includes`` directory.  The file
  should only contain this::

    <include package="mazu.theme" />

.. _pythonproducts: http://plone.org/products/pythonproducts


Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``mazu.theme`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        mazu.theme
       
* Tell the plone.recipe.zope2instance recipe to install a ZCML slug:

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    zcml =
        mazu.theme
      
* Re-run buildout, e.g. with:

    $ ./bin/buildout
        
You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.

First Time Customization
------------------------

Visit site home and append /@@manage-viewlets to the site home URL,
that will lead you to Viewlet Management Interface.
Hide the viewlets you want to disable.
Move up or down the viewlets to fit your needs.

