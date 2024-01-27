Usage
=====

Installation
------------
1. Clone the repository:

.. code-block:: console

    git clone git@github.com:JohanCarlsen/PyTools.git

2. Navigate to the root directory:

.. code-block:: console 

    cd PyTools

3. Install using ``pip``:

.. code-block:: console 

    pip install -e . 

.. note::

    For :code:`pylance` to be able to resolve the package, installing
    with
    
    .. code-block:: console 

        pip install -e . --config-settings editable_mode=compat

    ensures this.

Import package
--------------

To import :code:`pytools` to your :code:`python` project:

.. code-block:: python

    import pytools