# python3 -m venv -p /home/thiago/micromamba/bin/python3 venv
# virtualenv venv -p /usr/bin/python3.9
# python3 -m pip install wheel
# python3 -m pip install --force git+https://github.com/tercen/tercen_python_client@0.1.6
# python3 -m tercen.util.requirements . > requirements.txt

from tercen.client import context as ctx
import numpy as np
from operator_funcs import calc_mean

tercenCtx = ctx.TercenContext()

df = calc_mean(tercenCtx)
df = tercenCtx.add_namespace(df) 
resDf = tercenCtx.save(df)


