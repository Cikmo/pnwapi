===============
 Pnwapi
===============

Pnwapi is an easy to use async API wrapper for the Politics and War API.

Installation
------------
.. code-block:: bash

    pip install pnwapi

Usage
-----
.. code-block:: python

   import asyncio
   from pnwapi import Pnwapi

   async def main():
      pnw = await Pnwapi.init(
         pnw_api_key="your_api_key",
         pnw_bot_key="your_bot_key", # Optional
         db_url="postgresql://user:password@localhost:5432/pnwapi",
      )
      nation = await pnw.get.nation(1)
      print(nation.name)

      for alliance_member in nation.get.alliance().members:
         print(alliance_member.name)
      
   if __name__ == "__main__":
         asyncio.run(main())

.. class:: center

hello, how are you?

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   api/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
