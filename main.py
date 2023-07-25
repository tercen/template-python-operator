from tercen.client import context as ctx
import numpy as np
from operator_funcs import calc_mean

tercenCtx = ctx.TercenContext()

tercenCtx = ctx.TercenContext(
    workflowId="066a65dced98e7c2458cfbb1e30038d3",
    stepId="307f7d8a-efdd-45e7-99cc-e128d792bb84",
    username="admin",
    password="admin",
    serviceUri = "http://127.0.0.1:5400/" 
)
df = (
tercenCtx.select(['.y', '.ci', '.ri'])
    .groupby(['.ci','.ri'], as_index=False)
    .mean()
    .rename(columns={".y":"mean"})
    .astype({".ci": np.int32, ".ri": np.int32})
)

df = tercenCtx.add_namespace(df) 
tercenCtx.save(df)
