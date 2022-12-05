# python3 -m venv -p /home/thiago/micromamba/bin/python3 venv
# virtualenv venv -p /usr/bin/python3.9
# python3 -m pip install wheel
# python3 -m pip install git+https://github.com/tercen/tercen_python_client
# python3 -m pip install --force https://raw.githubusercontent.com/tercen/tercen_python_client/main/dist/tercen-0.0.1-py3-none-any.whl
from tercen.client import context as ctx
import numpy as np

# http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
# tercenCtx = ctx.TercenContext(workflowId = '9b611b90f412969d6f617f559f005bc6', 
#                           stepId = '2ca54ff5-5b7f-44e9-870b-48facabc41ae')

tercenCtx = ctx.TercenContext()

df = tercenCtx.select(['.y', '.ci', '.ri'])

df = df.groupby(['.ci','.ri'], as_index=False).mean()
df = df.rename(columns={".y":"mean"})

df = tercenCtx.add_namespace(df) 
tercenCtx.save(df)

