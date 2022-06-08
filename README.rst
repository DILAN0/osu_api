osu_api
===========
Install:

.. code:: sh
    
    pip install osu_api-0.1.tar.gz

Example:

.. code:: py
    
    from osu_api import core

    token = core.osu.get_token('token...')

    pp = core.osu.pp(token,"DILAN_NAXUY") #get pp
    scores = core.score.get_scores(token,23764407,"best",0) #json score

 



    
